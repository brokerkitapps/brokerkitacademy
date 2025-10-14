Time to create an amazing Gamma presentation for Brokerkit Academy!

We want to create slides about:
$ARGUMENTS

**Your Task:**

1. **Understand the Request**
   - If the user provided a topic/idea, you'll need to generate the content
   - If the user referenced an existing file (e.g., `assets/slides/filename.md`), read that file
   - If unclear, ask the user for clarification

2. **Generate Content (if needed)**
   - Review `CLAUDE.md` for context about:
     - Brokerkit platform capabilities
     - Relitix MLS data integration
     - Brokerboost lead generation services
     - Real estate recruiting best practices
     - Target audience (residential real estate brokerages and team leaders)

   - Create comprehensive markdown content appropriate for the presentation type:
     - **For presentations**: Clear sections with bullet points, key concepts, examples
     - **For webinars**: Include poll questions, demo moments, engagement prompts
     - **For bootcamp training**: Progressive learning, hands-on exercises, practice tasks

   - Structure the content with:
     - Clear headings using `#` and `##` markdown syntax
     - Bullet points for key information
     - Examples and use cases
     - Call-outs for important points
     - Suggested visual elements (e.g., "screenshot of dashboard here")

3. **Save Content Locally**
   - Save the markdown content to `assets/slides/` directory
   - Use a descriptive filename (e.g., `assets/slides/agent-recruiting-strategies-q1.md`)
   - Ensure the content is well-formatted and ready for Gamma to process

4. **Determine Presentation Parameters**

   ⚠️ **IMPORTANT - Gamma API Limits (We're on Pro Plan):**
   - **Our limit**: Maximum 60 cards per presentation (Pro plan)
   - **Daily limit**: 50 presentations per day (Pro tier during beta)
   - For presentations requiring more slides, consider splitting into multiple parts
   - Note: Ultra accounts have a 75-card limit if we upgrade in the future

   - **Title**: Extract or create a clear title
   - **Number of Cards**: Based on content length (stay within API limits)
     - Short presentation (10-15 slides)
     - Standard presentation (15-25 slides)
     - Long presentation/training (25-50 slides)
     - Extra-long training (50-60 slides for Pro, 50-75 for Ultra)
   - **Theme**: Suggest using "Berlin" or "Cape" for professional content (optional)
   - **Format**: Usually "presentation" (but could be "document" or "social")

5. **Create Gamma Presentation**
   - Run the Python script using:
   ```bash
   # Default: Uses professional Unsplash stock photos
   python3 src/brokerkitacademy/gamma/cli/create_slides.py --file assets/slides/[filename].md --title "[Title]" --num-cards [number] --verbose
   ```

   - Optional parameters:
     - `--theme [theme-name]` - Specific theme to use
     - `--image-source unsplash` - Professional stock photos (default)
     - `--image-source aiGenerated` - AI-generated images (if you prefer)
     - `--image-source giphy` - Animated GIFs

   - The script will:
     - Create the presentation in Gamma using AI
     - Track metadata in `assets/slides/gamma_metadata.json`
     - Return the Gamma URL

6. **Present Results to User**
   - Show the Gamma URL prominently
   - Confirm the local file location
   - Mention the number of slides created
   - Suggest that the user can now view and edit the presentation in Gamma
   - Gamma will automatically:
     - Format the content professionally
     - Add professional stock photos from Unsplash (curated, high-quality images)
     - Apply the chosen theme
     - Create visual layouts

**Important Notes:**
- The Gamma API uses AI to enhance your content with:
  - Professional layouts and design
  - Professional stock photos from Unsplash (default for polished, credible presentations)
  - Smart formatting and visual hierarchy
  - Theme-based color schemes
- **Image Preference:** We default to Unsplash stock photos because they look more professional
  and credible than AI-generated images for business presentations
- After creation, the user can edit the presentation in Gamma's web interface
- The local markdown file serves as version control for the content
- All presentations are tracked in `assets/slides/gamma_metadata.json`

**Example Workflow:**

```
User: /create_slides Agent recruiting strategies for Q1 2025

Claude: I'll create a comprehensive presentation about agent recruiting strategies for Q1 2025.

[Generates markdown content covering recruiting strategies]

[Saves to assets/slides/agent-recruiting-strategies-q1-2025.md]

[Runs: python3 src/brokerkitacademy/gamma/cli/create_slides.py --file assets/slides/agent-recruiting-strategies-q1-2025.md --title "Agent Recruiting Strategies Q1 2025" --num-cards 20 --verbose]

✅ Presentation created successfully!

📊 Title: Agent Recruiting Strategies Q1 2025
🎴 Cards: 20 slides
📄 Local File: assets/slides/agent-recruiting-strategies-q1-2025.md

🔗 View your presentation:
   https://gamma.app/docs/xxxxxxxxxx

The presentation is now ready to view in Gamma! The AI has formatted your content,
added professional stock photos from Unsplash, and applied professional styling.
You can further edit and customize it in the Gamma web interface.
```

**Tips:**
- Be thorough but concise in your content
- Use clear headings and structure
- Include actionable advice and examples
- Consider the audience (brokerages and team leaders)
- Focus on practical implementation with Brokerkit
- Don't overload slides - let Gamma's AI help with layout
- **For large content**: If your content would require 60+ slides, consider:
  - Splitting into multiple presentations (Part 1, Part 2)
  - Creating a "core concepts" presentation and separate deep-dive modules
  - Using a more condensed approach with Gamma's "condense" text mode

Remember: Your job is to create great content. Gamma's AI will handle the visual design, images, and formatting to make it presentation-ready!
