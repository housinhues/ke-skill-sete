---
name: talent-contracts
description: Generates custom Housing Hues talent contracts (management, event/media coverage, photoshoots, campaigns, studio shoots with 018 Productions, service agreements) plus the post-signing onboarding package (welcome guide, fit assessment, Drive folder). Use this skill whenever the user asks to draft, generate, or prepare a contract, agreement, or onboarding package for new or existing Housing Hues talent, or mentions onboarding a new artist/model/creator, drafting a brand partnership or collab agreement, or setting up a talent's folder. Trigger even if the user just says "let's onboard [name]" or "draft an agreement for [name]" without using the word "contract."
---

# Housing Hues Talent Contracts

## What this skill produces

For a single talent engagement, this skill walks through an interview, then produces up to four deliverables:

1. **The contract itself** — a branded PDF, tailored to the engagement type
2. **A post-signing welcome guide** — plain-language next steps for the talent
3. **A fit assessment** — a short form/checklist covering availability and working style, either filled in during the interview or sent to the talent
4. **A designated Google Drive folder** for that talent's documents and media

Not every engagement needs all four — see "Deciding what to produce" below.

## Why this skill is meticulous by design

Housing Hues contracts sit between the agency, the talent, and (often) a paying brand or client. A vague or copy-pasted clause here isn't just sloppy — it can cost someone money or leave Housing Hues exposed. So this skill:

- Never silently guesses at deal terms. If a term isn't provided, it's asked for.
- Always distinguishes **negotiable** terms (fee, usage duration, exclusivity scope) from **non-negotiable** ones (brand-safety conduct, confidentiality, IP ownership defaults) — see `references/clause-library.md`.
- Always states assumptions back to the user before generating the final PDF, so nothing goes out uncaught.

This is not a place to be fast at the expense of being right. Take the extra turn to confirm details rather than filling gaps with plausible-sounding text.

## Step 1 — Identify the engagement type

Ask (if not already clear from context) which of these the contract is for. Each maps to a reference file with type-specific clauses:

| Engagement type | Reference file |
|---|---|
| Talent management agreement (Housing Hues ↔ talent, ongoing representation) | `references/contract-management.md` |
| Event / media coverage (talent covering or appearing at an event) | `references/contract-event-coverage.md` |
| Photoshoot (including studio shoots via 018 Productions) | `references/contract-photoshoot.md` |
| Campaign (brand or business partnership, sponsored content) | `references/contract-campaign.md` |
| Collab (talent-to-talent or talent-to-individual creative collaboration) | `references/contract-collab.md` |
| Service agreement (Housing Hues providing a defined service to a client) | `references/contract-service.md` |
| Event curation partnership (Housing Hues curates lineup/vendors/talent for a client's event, rather than talent being booked to appear) | `references/contract-event-curation.md` |
| Vendor / media partner engagement (Housing Hues or talent brings in an outside media company or production house to shoot/produce content — the reverse direction from a service agreement) | `references/contract-vendor-media.md` |
| Social media management (Housing Hues runs a talent's or client's social accounts — content calendar, posting, engagement, analytics reporting — distinct from the posting-conduct clause below, which covers approval rights over the talent's own posts) | `references/contract-social-media-mgmt.md` |

If the engagement blends types (e.g. a campaign that includes a studio shoot, or a photoshoot where an outside media company is also being engaged as a vendor), say so — combine the relevant reference files rather than forcing one template. A single shoot often needs **two** contracts running in parallel: one with the talent (`contract-photoshoot.md`) and one with the media company covering it (`contract-vendor-media.md`) — draft both if both parties are new to the engagement.

## Step 2 — Interview for details

Read `references/interview-checklist.md` for the full field list. In short, always confirm:

- **Parties**: full legal/stage names, and which entity is contracting (Housing Hues on talent's behalf, or talent directly)
- **Scope**: exactly what's being delivered (shots, posts, appearances, hours, deliverable count)
- **Term & dates**: start/end dates, any renewal terms
- **Compensation**: amount, currency, payment schedule, who pays whom
- **Usage rights**: where content can be used, for how long, exclusivity
- **018 Productions involvement**: if a studio shoot, confirm 018 Productions is the media partner and note their standard credit/attribution terms if any
- **Social media posting terms**: see the Managed vs Independent tiers in `references/clause-library.md#social-media-conduct` — ask which tier the talent is on, or flag it as a term to negotiate
- **Account access/credentials** (social media management contracts only): who holds login credentials, how access is revoked at contract end, and what happens to the account's content/following if the relationship ends
- **Jurisdiction**: default to South African law unless told otherwise

Before drafting, check whether the talent already has info on file — search Google Drive (talente-sqeta onboarding submissions, Talent-Dashboard repo) for their name first, and only ask the user to re-supply what isn't already there.

## Step 3 — Draft and confirm

Summarize the filled-in terms back to the user in plain language (not full legal text yet) and get explicit confirmation before generating the PDF. Flag anything you defaulted or assumed. Cross-check against `references/clause-library.md` — in particular, never leave governing law, payment terms, or the social media tier unset or vague; these three are where most real-world disputes originate.

## Step 4 — Generate the PDF

Use the `pdf` skill (`/mnt/skills/public/pdf/SKILL.md`) to produce the final document. Apply the branding spec in `references/branding.md` (Housing Hues logo, black/gold/navy palette, fonts) for the letterhead and footer. Include signature blocks for both parties, laid out cleanly enough to drop straight into DocuSign, Adobe Sign, or a similar e-signature tool — this skill does not send documents for e-signature itself; see `references/esignature-notes.md` for why and what to suggest instead.

## Step 5 — Decide what else to produce

Ask the user which of the following they want alongside the contract (default: all three for a *new* talent signing their first agreement; contract-only for an existing talent's repeat/updated agreement):

- **Welcome guide** — build from `references/onboarding-guide-template.md`. Covers bio setup, posting conduct under whichever social media tier they picked, who to contact for what, and what happens next.
- **Fit assessment** — build from `references/fit-assessment-template.md`. This is a form for the talent to fill in (availability, working style, equipment/location constraints), not something to interrogate the user about live. Offer to add it as a talente-sqeta style page if the user wants it hosted like their other onboarding forms.
- **Drive folder** — create via the Google Drive connector, named `Talent/<Talent Name>/`, with subfolders `Contracts`, `Media`, `Docs`. Share it with the talent's email at `commenter` or `editor` per the user's instruction (default: don't share automatically — ask first, since Drive sharing sends the person an email).

## Step 6 — Deliver

Present the finished PDF(s) via `present_files`. Summarize what was produced and what's still outstanding (e.g. "waiting on 018 Productions' shot list before the studio shoot annex can be finalized").

## Reference index

- `references/clause-library.md` — negotiable vs non-negotiable clause bank, including the social media conduct tiers
- `references/interview-checklist.md` — full field checklist by engagement type
- `references/branding.md` — Housing Hues visual identity spec for documents
- `references/onboarding-guide-template.md` — welcome guide structure
- `references/fit-assessment-template.md` — fit assessment form structure
- `references/esignature-notes.md` — why this skill can't e-sign directly and what to suggest
- `references/contract-*.md` — one file per engagement type (management, event coverage, photoshoot, campaign, collab, service, event curation, vendor/media partner, social media management), each with type-specific clauses and a full example
