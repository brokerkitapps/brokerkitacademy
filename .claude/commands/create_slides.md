Time to create an amazing Gamma presentation for Brokerkit Academy!

We want to create slides about:
$ARGUMENTS

**Your Task:**

1. **Understand the Request**
   - If the user provided a topic/idea, you'll need to generate the content
   - If the user referenced an existing file (e.g., `slides/filename.md`), read that file
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
   - Save the markdown content to `slides/` directory
   - Use a descriptive filename (e.g., `slides/agent-recruiting-strategies-q1.md`)
   - Ensure the content is well-formatted and ready for Gamma to process

4. **Determine Presentation Parameters**
   - **Title**: Extract or create a clear title
   - **Number of Cards**: Based on content length
     - Short presentation (10-15 slides)
     - Standard presentation (15-25 slides)
     - Long presentation/training (25-40 slides)
   - **Theme**: Suggest using "Berlin" or "Cape" for professional content (optional)
   - **Format**: Usually "presentation" (but could be "document" or "social")

5. **Create Gamma Presentation**
   - Run the Python script using:
   ```bash
   python3 scripts/gamma/create_slides.py --file slides/[filename].md --title "[Title]" --num-cards [number] --verbose
   ```
   - Optional: Add `--theme [theme-name]` if you want a specific theme
   - The script will:
     - Create the presentation in Gamma using AI
     - Track metadata in `slides/gamma_metadata.json`
     - Return the Gamma URL

6. **Present Results to User**
   - Show the Gamma URL prominently
   - Confirm the local file location
   - Mention the number of slides created
   - Suggest that the user can now view and edit the presentation in Gamma
   - Gamma will automatically:
     - Format the content professionally
     - Add relevant stock images
     - Apply the chosen theme
     - Create visual layouts

**Important Notes:**
- The Gamma API uses AI to enhance your content with:
  - Professional layouts and design
  - Relevant stock images from AI generation
  - Smart formatting and visual hierarchy
  - Theme-based color schemes
- After creation, the user can edit the presentation in Gamma's web interface
- The local markdown file serves as version control for the content
- All presentations are tracked in `slides/gamma_metadata.json`

**Example Workflow:**

```
User: /create_slides Agent recruiting strategies for Q1 2025

Claude: I'll create a comprehensive presentation about agent recruiting strategies for Q1 2025.

[Generates markdown content covering recruiting strategies]

[Saves to slides/agent-recruiting-strategies-q1-2025.md]

[Runs: python3 scripts/gamma/create_slides.py --file slides/agent-recruiting-strategies-q1-2025.md --title "Agent Recruiting Strategies Q1 2025" --num-cards 20 --verbose]

✅ Presentation created successfully!

📊 Title: Agent Recruiting Strategies Q1 2025
🎴 Cards: 20 slides
📄 Local File: slides/agent-recruiting-strategies-q1-2025.md

🔗 View your presentation:
   https://gamma.app/docs/xxxxxxxxxx

The presentation is now ready to view in Gamma! The AI has formatted your content,
added relevant images, and applied professional styling. You can further edit and
customize it in the Gamma web interface.
```

**Tips:**
- Be thorough but concise in your content
- Use clear headings and structure
- Include actionable advice and examples
- Consider the audience (brokerages and team leaders)
- Focus on practical implementation with Brokerkit
- Don't overload slides - let Gamma's AI help with layout

Remember: Your job is to create great content. Gamma's AI will handle the visual design, images, and formatting to make it presentation-ready!
