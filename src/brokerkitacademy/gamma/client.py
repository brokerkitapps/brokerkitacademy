"""
Gamma API Client

This module provides a Python client for interacting with the Gamma Generate API.
It handles presentation creation, status polling, and error handling.

API Documentation: https://developers.gamma.app/
"""

import os
import time
import requests
from typing import Dict, Optional, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GammaAPIError(Exception):
    """Custom exception for Gamma API errors"""

    pass


class GammaClient:
    """
    Client for interacting with the Gamma Generate API.

    Features:
    - Create presentations, documents, and social content
    - Poll generation status until completion
    - Retrieve gamma URLs and IDs
    - Support for all API parameters
    """

    BASE_URL = "https://public-api.gamma.app/v0.2"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gamma API client.

        Args:
            api_key: Gamma API key. If not provided, reads from GAMMA_API_KEY env var
        """
        self.api_key = api_key or os.getenv("GAMMA_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Gamma API key is required. "
                "Provide it via api_key parameter or GAMMA_API_KEY environment variable."
            )

    def _get_headers(self) -> Dict[str, str]:
        """Get HTTP headers for API requests"""
        return {"X-API-KEY": self.api_key, "Content-Type": "application/json"}

    def create_presentation(
        self,
        input_text: str,
        format: str = "presentation",
        num_cards: int = 15,
        theme_name: Optional[str] = None,
        image_source: str = "unsplash",
        image_model: Optional[str] = None,
        image_style: Optional[str] = None,
        additional_instructions: Optional[str] = None,
        export_as: Optional[str] = None,
        wait_for_completion: bool = True,
        poll_interval: int = 5,
        max_wait_time: int = 300,
    ) -> Dict[str, Any]:
        """
        Create a new Gamma presentation.

        Args:
            input_text: Content for the presentation (1-100,000 tokens)
            format: "presentation", "document", or "social"
            num_cards: Number of slides/cards (1-60 for Pro, 1-75 for Ultra)
            theme_name: Name of the theme to use (must be pre-created in Gamma)
            image_source: Image source - "unsplash" (default, professional stock photos),
                         "aiGenerated" (requires image_model), or "giphy" (animated GIFs)
            image_model: Specific AI image model to use (only for aiGenerated source)
            image_style: Visual style for images (e.g., "photorealistic")
            additional_instructions: Extra guidance for content generation
            export_as: Export format ("pdf" or "pptx")
            wait_for_completion: If True, poll until generation completes
            poll_interval: Seconds between status checks
            max_wait_time: Maximum seconds to wait for completion

        Returns:
            Dictionary containing:
            - generation_id: The unique generation ID
            - status: "pending" or "completed"
            - gamma_url: URL to view the presentation (if completed)
            - credits: Credits information

        Raises:
            GammaAPIError: If the API request fails
            ValueError: If input validation fails
        """
        # Validate inputs
        if not input_text or not input_text.strip():
            raise ValueError("input_text cannot be empty")

        valid_formats = ["presentation", "document", "social"]
        if format not in valid_formats:
            raise ValueError(f"format must be one of {valid_formats}, got '{format}'")

        if num_cards < 1:
            raise ValueError(f"num_cards must be at least 1, got {num_cards}")
        if num_cards > 75:
            raise ValueError(f"num_cards cannot exceed 75 (Ultra tier limit), got {num_cards}")

        valid_image_sources = ["aiGenerated", "unsplash", "giphy"]
        if image_source not in valid_image_sources:
            raise ValueError(f"image_source must be one of {valid_image_sources}, got '{image_source}'")

        if export_as and export_as not in ["pdf", "pptx"]:
            raise ValueError(f"export_as must be 'pdf' or 'pptx', got '{export_as}'")

        # Build request payload
        payload = {
            "inputText": input_text,
            "format": format,
            "numCards": num_cards,
            "imageOptions": {"source": image_source},
        }

        # Add optional parameters
        if theme_name:
            payload["themeName"] = theme_name

        if image_model:
            payload["imageOptions"]["model"] = image_model

        if image_style:
            payload["imageOptions"]["style"] = image_style

        if additional_instructions:
            payload["additionalInstructions"] = additional_instructions

        if export_as:
            payload["exportAs"] = export_as

        # Make the API request
        try:
            response = requests.post(
                f"{self.BASE_URL}/generations",
                headers=self._get_headers(),
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()

            generation_id = result.get("generationId")
            if not generation_id:
                raise GammaAPIError("No generation ID returned from API")

            # If wait_for_completion is False, return immediately
            if not wait_for_completion:
                return result

            # Poll for completion
            return self._poll_until_complete(
                generation_id, poll_interval=poll_interval, max_wait_time=max_wait_time
            )

        except requests.exceptions.HTTPError as e:
            # Extract error details from API response
            error_msg = f"Failed to create presentation: {str(e)}"
            try:
                if e.response is not None:
                    error_body = e.response.json()
                    if "message" in error_body:
                        error_msg = f"Failed to create presentation: {error_body['message']}"
                    else:
                        error_msg = f"Failed to create presentation: {e.response.text}"
            except Exception:
                # If we can't parse the response, use the original error
                pass
            raise GammaAPIError(error_msg)
        except requests.exceptions.RequestException as e:
            raise GammaAPIError(f"Failed to create presentation: {str(e)}")

    def get_generation_status(self, generation_id: str) -> Dict[str, Any]:
        """
        Get the status of a generation request.

        Args:
            generation_id: The generation ID to check

        Returns:
            Dictionary containing:
            - generation_id: The generation ID
            - status: "pending" or "completed"
            - gamma_url: URL to view the presentation (if completed)
            - credits: Credits information

        Raises:
            GammaAPIError: If the API request fails
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/generations/{generation_id}",
                headers=self._get_headers(),
                timeout=30,
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            raise GammaAPIError(f"Failed to get generation status: {str(e)}")

    def _poll_until_complete(
        self, generation_id: str, poll_interval: int = 5, max_wait_time: int = 300
    ) -> Dict[str, Any]:
        """
        Poll the generation status until completion or timeout.

        Args:
            generation_id: The generation ID to poll
            poll_interval: Seconds between status checks
            max_wait_time: Maximum seconds to wait

        Returns:
            Final status dictionary when completed

        Raises:
            GammaAPIError: If timeout occurs or polling fails
        """
        start_time = time.time()

        while True:
            elapsed = time.time() - start_time
            if elapsed > max_wait_time:
                raise GammaAPIError(
                    f"Timeout waiting for generation to complete after {max_wait_time}s"
                )

            status = self.get_generation_status(generation_id)

            if status.get("status") == "completed":
                return status

            if status.get("status") == "failed":
                raise GammaAPIError(
                    f"Generation failed: {status.get('message', 'Unknown error')}"
                )

            # Wait before next poll
            time.sleep(poll_interval)

    def get_themes(self) -> Dict[str, Any]:
        """
        Get available Gamma themes.

        Note: This endpoint may not be publicly available yet.
        Check the Gamma API documentation for availability.

        Returns:
            Dictionary containing available themes

        Raises:
            GammaAPIError: If the API request fails
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/themes", headers=self._get_headers(), timeout=30
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            raise GammaAPIError(f"Failed to get themes: {str(e)}")


# Convenience function for quick presentation creation
def create_quick_presentation(input_text: str, num_cards: int = 15, **kwargs) -> str:
    """
    Quickly create a presentation and return its URL.

    Args:
        input_text: Content for the presentation
        num_cards: Number of slides
        **kwargs: Additional arguments passed to create_presentation

    Returns:
        URL to the created Gamma presentation

    Raises:
        GammaAPIError: If creation fails
    """
    client = GammaClient()
    result = client.create_presentation(
        input_text=input_text, num_cards=num_cards, **kwargs
    )

    gamma_url = result.get("gammaUrl")
    if not gamma_url:
        raise GammaAPIError("No gamma URL returned from API")

    return gamma_url
