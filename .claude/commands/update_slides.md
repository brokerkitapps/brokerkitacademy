Time to update an existing Gamma presentation for Brokerkit Academy!

We want to update slides:
$ARGUMENTS

**Understanding Gamma API Limitations:**
⚠️ The Gamma API currently only supports **creating** presentations, not editing existing ones.
Therefore, "updating" means we'll **regenerate** the presentation with updated content and
provide you with a new URL. The metadata will be updated to track the new version.

**Your Task:**

1. **Identify the Presentation**
   - User may provide:
     - Local file path (e.g., `slides/agent-recruiting-q1.md`)
     - Gamma URL (e.g., `https://gamma.app/docs/xxxxxxxxxx`)
     - Presentation title or partial title

   - Look up the presentation in `slides/gamma_metadata.json` to find:
     - The corresponding local file
     - Current Gamma URL
     - Existing metadata

   - If not found, ask the user for clarification

2. **Read Current Content**
   - Read the local markdown file
   - Show the user the current content structure
   - Ask what changes they want to make, or:
   - If they already specified changes, proceed with editing

3. **Update the Content**
   - Make the requested changes to the markdown file
   - This could involve:
     - Adding new sections
     - Updating existing content
     - Removing outdated information
     - Restructuring slides
     - Adding new examples or data
     - Updating statistics or screenshots

   - Save the updated content back to the same local file
   - Use the Edit tool to make precise changes

4. **Regenerate the Gamma Presentation**
   - Use the same parameters as the original (or user-specified changes):
     - Title (same or updated)
     - Number of cards (adjust if content changed significantly)
     - Theme (same or different)
     - Format (usually same)

   - Run the Python script:
   ```bash
   python3 scripts/gamma/create_slides.py --file slides/[filename].md --title "[Title]" --num-cards [number] --verbose
   ```

5. **Update Metadata**
   - The script will automatically add the new presentation to metadata
   - Manually note in `slides/gamma_metadata.json` that this is an updated version
   - Keep track of both the old and new Gamma URLs for reference

6. **Present Results to User**
   - ✅ Show the NEW Gamma URL prominently
   - 📄 Confirm the local file has been updated
   - 📝 List the changes made
   - ℹ️ Explain that this is a new version (due to API limitations)
   - 🗑️ Optionally mention they can delete the old version in Gamma if desired
   - 🔗 Provide both old and new URLs for comparison

**Example Workflow:**

```
User: /update_slides slides/agent-recruiting-q1-2025.md - add a section about social media recruiting

Claude: I'll update the agent recruiting presentation to add social media recruiting content.

[Reads current file: slides/agent-recruiting-q1-2025.md]

Current structure:
- Introduction to Agent Recruiting
- Traditional Recruiting Methods
- Using Brokerkit for Pipeline Management
- Data-Driven Recruiting with Relitix
- Best Practices and Tips

[Edits file to add new section after "Data-Driven Recruiting"]
- Introduction to Agent Recruiting
- Traditional Recruiting Methods
- Using Brokerkit for Pipeline Management
- Data-Driven Recruiting with Relitix
- Social Media Recruiting Strategies (NEW)
- Best Practices and Tips

✅ Content updated in slides/agent-recruiting-q1-2025.md

[Runs: python3 scripts/gamma/create_slides.py --file slides/agent-recruiting-q1-2025.md --title "Agent Recruiting Strategies Q1 2025" --num-cards 22 --verbose]

🎉 Presentation regenerated successfully!

📊 Title: Agent Recruiting Strategies Q1 2025
🎴 Cards: 22 slides (increased from 20)
📄 Local File: slides/agent-recruiting-q1-2025.md ✨ UPDATED

🔗 NEW Presentation URL:
   https://gamma.app/docs/yyyyyyyyyy

📜 Previous version (for reference):
   https://gamma.app/docs/xxxxxxxxxx

Changes made:
• Added new section: "Social Media Recruiting Strategies"
• Included content about LinkedIn, Facebook, and Instagram recruiting
• Updated total slide count from 20 to 22

The new presentation is ready to view! Due to Gamma API limitations, this is a
new presentation rather than an edit of the existing one. You may want to delete
the old version from your Gamma dashboard.
```

**Important Notes:**
- Always read the current file first before making changes
- Use the Edit tool for precise, surgical updates
- Track both old and new URLs for user reference
- Adjust slide count if content length changed significantly
- The local markdown file is the source of truth
- Git commit the content changes for version control

**Alternative Approach - Reference Existing:**
If the user says something like "Update slides using this new content I'll provide":
1. Ask them to provide or point to the new content
2. Replace the relevant sections in the markdown file
3. Regenerate the presentation

**When User Provides Gamma URL Only:**
```
User: /update_slides https://gamma.app/docs/xxxxxxxxxx - update the statistics

Claude: Let me look up that presentation in our metadata...

[Searches slides/gamma_metadata.json for the URL]
Found: slides/agent-recruiting-q1-2025.md

[Reads the file and proceeds with updates]
```

Remember: The local markdown file is your source of truth. Always edit that first,
then regenerate the Gamma presentation. This maintains version control and ensures
consistency between local and Gamma versions.
