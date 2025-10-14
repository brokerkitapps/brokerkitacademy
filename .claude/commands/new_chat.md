# Context Window Handoff

Gracefully transition to a new chat when approaching context limits by saving progress, committing changes, and creating a detailed handoff comment on the current GitHub issue.

## Process

### 1. Analyze Current State

**Check for uncommitted changes:**
- Run `git status` to see what has been modified
- Review current branch and recent commits with `git log -3`
- Identify which GitHub issue is being worked on from:
  - Branch name (e.g., `fix-issue-12`)
  - Recent commit messages
  - Current conversation context

**Summarize accomplishments:**
- List all files that were created or modified
- Document key decisions made
- Note any discoveries or insights
- Identify completed tasks and remaining work

### 2. Commit and Push Changes

**Create comprehensive commit:**
- Stage all relevant changes with `git add`
- Write descriptive commit message including:
  - What was accomplished in this session
  - Reference to GitHub issue number
  - Note that this is a context handoff: `(context handoff)`
- Example format:
  ```
  Progress on Issue #XX: [brief summary]

  - Accomplishment 1
  - Accomplishment 2
  - Accomplishment 3

  (context handoff)

  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

**Push to remote:**
- Use `git push` to sync changes
- If branch doesn't have upstream, use `git push -u origin <branch-name>`

### 3. Create Handoff Comment

**Determine issue number:**
- If not already identified, ask user which issue number to comment on
- Or extract from branch name/recent commits

**Draft comprehensive handoff comment with these sections:**

```markdown
## 🔄 Context Window Handoff

This chat session is approaching context limits. Here's a handoff summary for the next session.

### ✅ What Was Accomplished

[Detailed bullet list of:
- Files created/modified with brief description
- Features implemented
- Bugs fixed
- Tests written
- Documentation updated
- Refactorings completed
]

### 🔍 Analysis & Findings

[Key insights discovered during this session:
- Technical discoveries
- API limitations or gotchas
- Architecture decisions made
- Patterns established
- Issues encountered and how they were resolved
]

### 📋 Current State

**Working branch:** `<branch-name>`
**Last commit:** `<commit-sha>`
**Status:** <Brief status - e.g., "In progress", "Ready for testing", "Blocked">

**Modified files:**
- `path/to/file1.py` - [brief description]
- `path/to/file2.json` - [brief description]

### 🎯 Next Steps

Priority-ordered list of remaining tasks:

1. **[Task 1]** - [Brief description and context]
2. **[Task 2]** - [Brief description and context]
3. **[Task 3]** - [Brief description and context]

### 💡 Important Context for Next Session

[Critical information to remember:
- Decisions that shouldn't be revisited
- Approaches that were tried and didn't work
- External constraints or requirements
- Related issues or PRs
- Links to relevant documentation
]

### 🔗 References

- Commit: <commit-link>
- Files changed: [link to GitHub comparison]
- Related issues: #XX, #YY
- Documentation referenced: [links]

---

**To continue:** Start a new chat with this comment URL as context.
```

**Post comment using GitHub CLI:**
```bash
gh issue comment <issue-number> --body "<comment-content>"
```

### 4. Return Handoff Information

**Provide to user:**
- ✅ Confirmation that changes were committed and pushed
- 📝 Issue number that was commented on
- 🔗 Direct URL to the comment (get from gh CLI output)
- 📋 Quick summary of next steps

**Example output:**
```
✅ Changes committed and pushed
📝 Handoff comment posted to Issue #12
🔗 Comment URL: https://github.com/brokerkitapps/brokerkitacademy/issues/12#issuecomment-123456

Next Steps Summary:
1. Implement error handling for API calls
2. Add unit tests for new functionality
3. Update documentation

To start your next chat, copy the comment URL above and include it in your first message.
```

## Usage

Simply type `/new_chat` when your conversation is getting long or approaching context limits.

The command will:
1. Commit and push all current changes
2. Analyze what was accomplished
3. Create a detailed handoff comment on the relevant issue
4. Provide you with a URL to start the next chat

## Notes

- If you need to specify a particular issue number, use: `/new_chat <issue-number>`
- The command will try to auto-detect the issue from your branch name or commits
- All changes must be in a valid state (code should at least not break things)
- Consider running tests before using this command if appropriate
