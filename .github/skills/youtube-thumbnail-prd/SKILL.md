---
name: youtube-thumbnail-prd
description: "Create or revise the PRD for the YouTube subtitle-based thumbnail title generator using Lean Startup Build-Measure-Learn. Use when planning MVP scope, validating creator needs, defining experiments or metrics, or updating prd.md."
argument-hint: "Describe the PRD change, product question, or Build-Measure-Learn experiment"
---

# YouTube Thumbnail PRD

Create and maintain a practical product requirements document for this repository's app: a tool that turns user-provided YouTube subtitles into short, evidence-based thumbnail title candidates.

## When to Use

- Create, review, or update `prd.md`.
- Define MVP scope, target users, hypotheses, experiments, metrics, or product risks.
- Decide what to build next based on Build-Measure-Learn evidence.

## Procedure

1. Read the current `prd.md` and relevant project documentation before proposing changes. Preserve established decisions unless the user asks to revisit them.
2. Identify the user problem, target segment, and the riskiest assumption. Separate verified evidence from assumptions; do not invent research findings, user quotes, or product capabilities.
3. Keep the MVP focused on the smallest test that can validate the riskiest assumption. Avoid adding features merely because they are technically possible.
4. Describe each Build-Measure-Learn loop explicitly:
   - **Build:** the smallest prototype or product change.
   - **Measure:** observable behaviors, qualitative feedback, cohort/sample context, and a hypothesis-level success threshold.
   - **Learn:** the decision to continue, change, or stop based on the evidence.
5. Define metrics with operational definitions. Distinguish usage signals (such as copying a candidate) from business outcomes (such as CTR); do not claim CTR impact without a controlled experiment and suitable data.
6. Address reliability and trust for generated copy: candidates must be grounded in subtitle content, distinguishable from one another, editable, and presented as drafts rather than guaranteed performance.
7. Respect the product's data boundaries: the MVP accepts user-provided subtitle text or `.srt`/`.vtt` files. Do not assume URL-based subtitle extraction, access to private captions, or permission to store/transmit source content. Flag policy, privacy, retention, and provider questions for validation.
8. Update only the relevant PRD sections. Use Korean for user-facing product documentation, concise headings and tables, and keep MVP requirements separate from future ideas.
9. Review the final document for contradictions, untestable goals, unsupported claims, scope creep, and consistency between features, metrics, and experiments. Report unresolved assumptions clearly.

## Default Product Context

- Initial users: solo YouTube creators and small channels producing educational, informational, or review videos with available subtitles.
- Core workflow: provide subtitles, optionally add video context, generate several thumbnail-copy options, inspect subtitle evidence, edit, copy, and give lightweight feedback.
- Core product value to test: reduce the effort of finding and expressing a video hook without making claims unsupported by the video.
- Out of initial scope: thumbnail image editing/generation, channel analytics, guaranteed views or CTR, publishing, and automatic subtitle collection from YouTube URLs.
- Initial hypotheses and thresholds in `prd.md` are provisional. Treat small-sample results as directional, not proof of product-market fit.

## Output

When editing the PRD, save changes to `prd.md` unless the user specifies another destination. Summarize the sections changed, the key product decision, and any assumptions still requiring validation.
