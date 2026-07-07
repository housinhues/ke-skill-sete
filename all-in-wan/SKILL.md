---
name: all-in-wan
description: "Pro-level all-in-one photo editor for New Age Lounge. Features: Multi-mode editing (Nightclub/Studio/Outdoor), Carousel Continuity, Caption & Hashtag Kit, Story-Ready (9:16) variants, Film Textures, and Multi-Logo support."
---

# All-In-Wan Pro Editor v5

This is the definitive, pro-level automation for New Age Lounge. It handles end-to-end content creation, from batch editing and branding to caption generation and multi-platform optimization.

## Core Principles

1. **Background & Subject Integrity**: **STRICT.** Never change, replace, or reimagine any part of the background or human features. Use the gold standard references in `references/gold-standard/` for quality benchmarks.
2. **Carousel Continuity**: When processing a batch, maintain identical color grading across all images to ensure a seamless swipe experience.
3. **Orientation Protection**: **CRITICAL.** Maintain exact original orientation. No flips or rotations.
4. **Conditional Branding**: **OFF BY DEFAULT.** Add logos only when requested. Support for multiple logos via the `templates/logo-library/`.
5. **Multi-Platform Ready**: Generate 4:5 Feed posts and optional 9:16 Story variants.

## Modes & Visual References

| Mode | Scene Type | Benchmark Reference |
| :--- | :--- | :--- |
| **Nightclub** | Indoor club, dark | `nightclub_reference.png` |
| **Studio** | Controlled light | `studio_reference.png` |
| **Outdoor** | Street, natural light | `outdoor_reference.png` |

## Pro Features & Workflow

### 1. Carousel Continuity
When a user provides a "batch" or "carousel," apply a locked-in color profile. Use the first edited photo as the reference for all subsequent photos in that batch to ensure visual unity.

### 2. Film Textures & Aesthetics
- **Nightclub/Outdoor**: Offer a "Film Texture" toggle to add subtle analog grain and vintage glow.
- **Studio**: Keep textures sharp and clean unless "Vintage Studio" is requested.

### 3. Story-Ready (9:16) Variants
Upon request, generate 9:16 variants. Use AI to intelligently expand or crop the scene so the subject remains centered and the background integrity is maintained.

### 4. Caption & Hashtag Kit
- **Resource**: `references/caption-kit.md`
- For every batch, provide 3 caption options (Moody, Engaging, Hype) and the relevant hashtag set.

### 5. Multi-Logo Support
- **Resource**: `templates/logo-library/`
- Standard logo: `standard-logo.jpg`.
- If user requests a specific event logo, check the library before applying.

## Tool Guidance (media_generation)

> "I am processing a [Carousel/Single] for New Age Lounge in [Mode] mode. 
> 
> **CRITICAL GUARDRAILS:** 
> 1. Background Integrity: Keep background identical to original.
> 2. Orientation: Do not rotate or flip.
> 3. Subject: 100% feature preservation.
> 4. Continuity: [If Carousel: Ensure color grading is identical to the first photo in the batch.]
> 
> **STYLE & LOGO:**
> - Mode: [Nightclub/Studio/Outdoor] using [Reference Name] benchmark.
> - [Optional: Apply subtle analog film grain/texture.]
> - [Optional: Place [Logo Name] watermark in top right corner. DO NOT alter logo.]
> 
> **OUTPUT:**
> - [4:5 Feed Post / 9:16 Story Variant]"

## Resources

- **Logo Library**: `templates/logo-library/`
- **Caption Kit**: `references/caption-kit.md`
- **Gold Standard References**: `references/gold-standard/`
