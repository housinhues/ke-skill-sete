---
name: study-timetable
description: "Maintain and publish a static study timetable on GitHub Pages. Use when creating, revising, checking, or deploying a personal exam-study schedule from the bundled HTML timetable template."
---

# Study Timetable

Maintain the timetable as a small, dependency-free static site and publish it from the repository's `study-timetable/site/` directory.

## Use the bundled site

- Treat `site/index.html` as the canonical timetable document.
- Keep `site/support.js` and `site/vendor/` unchanged unless the runtime itself needs repair; they are the local rendering runtime.
- Serve the site over HTTP during checks; do not test it with `file://` because the runtime loads scripts and resources.
- Keep all asset references relative so the site works at the repository's GitHub Pages path.

## Update the schedule

1. Read the existing `site/index.html` before editing.
2. Preserve the visual system: Plus Jakarta Sans, white canvas, dark navy text, muted gray metadata, orange Municipal emphasis, gray exam blocks, and yellow appointment callout.
3. Update dates, subjects, study actions, exams, venues, and personal reminders directly in the semantic HTML blocks. Keep the four study columns in chronological order: `08:00 to 11:00`, `11:30 to 13:30`, `15:00 to 17:00`, `18:30 to 19:30`.
4. Keep uncertain venues explicitly marked `(Guess)` rather than presenting them as confirmed.
5. Update the heading/subtitle when the schedule window changes; do not leave stale dates in the document title or visible subtitle.
6. Avoid adding external JavaScript or build dependencies. If fonts are unavailable, the system font fallback must still render acceptably.

## Validate and publish

Run the bundled validator from the repository root:

```bash
python study-timetable/scripts/validate_site.py
```

Then serve and smoke-test the site:

```bash
python3 -m http.server 4173 --bind 127.0.0.1 --directory study-timetable/site
curl -fsS http://127.0.0.1:4173/ | grep -q 'N6 Study Timetable'
```

Commit changes to `main`. The repository workflow `.github/workflows/pages.yml` deploys `study-timetable/site/` to GitHub Pages after every push to `main`. The public URL is:

`https://housinhues.github.io/ke-skill-sete/`

If the repository name or owner changes, update the URL in this instruction and in the repository documentation.

## Scope and safety

This skill edits only the timetable site and its deployment workflow. Do not invent exam dates, venues, or personal appointments. Preserve user-provided names and schedule facts exactly, including capitalization and uncertainty labels.
