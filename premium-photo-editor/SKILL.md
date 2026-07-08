---
name: premium-photo-editor
description: "High-end photo editing for premium brand aesthetics (e.g., Nike, streetwear, luxury nightlife) with a focus on Instagram (4:5) optimization. Strictly preserves human features and anatomical integrity. Use for: cinematic color grading, studio cleanup, lighting enhancement, and professional-grade branding."
---

# Premium Photo Editor

This skill provides a specialized workflow for transforming raw or standard camera captures into premium, brand-ready assets. It prioritizes visual impact and professional lighting while enforcing a strict "no-alteration" policy for human subjects and technical integrity.

## Core Principles

1. **Anatomical Integrity**: NEVER alter human features. No facial reshaping, body proportion changes, or "AI smoothing" that erases natural skin texture, moles, or unique marks. Retain subject identity 100%.
2. **Technical Integrity**: Preserve the original scene's orientation. Do not rotate, flip, mirror, or invert the image. Output orientation must exactly match input orientation.
3. **Premium Aesthetics**: Focus on high-contrast, cinematic color grading. For nightlife, use a warm-to-cool tonal balance (e.g., amber highlights, blue-teal shadows) to mimic high-end club photography.
4. **Flexible Delivery**: Results should be delivered directly to the user in the current communication channel (e.g., chat) by default. Cloud storage (Google Drive) uploads are performed ONLY when explicitly requested.

## Workflow

### 1. Scene Analysis
Analyze the image to determine the environment and lighting:
- **Outdoor/Dynamic**: High contrast, vibrant skies, natural light play.
- **Indoor/Nightlife**: Vibrant ambient/neon colors, deep contrast, ethereal atmosphere.

### 2. Style Application
Apply the appropriate style logic:

| Style | Key Characteristics | Best For |
| :--- | :--- | :--- |
| **Streetwear Peak** | Gritty yet polished, deep blacks, saturated accent colors, high texture sharpening. | Fashion, urban lifestyle. |
| **Cinematic Nightlife** | Subtle professional color grade, amber highlights, blue-teal shadows, enhanced lighting. | Clubs, luxury events. |

### 3. Professional Finishing
- **Instagram Portrait Optimization**: Default to **4:5 aspect ratio**. Crop only where necessary to preserve the main subject fully in frame.
- **Virtual Dodge & Burn**: Enhance the subject's natural contours by subtly brightening highlights and deepening shadows.
- **Branding (OPTIONAL)**: Embed logos or watermarks ONLY when explicitly requested. If branding is requested, place as a clean watermark in corners (default top right) with appropriate margins. Reproduce logos exactly as provided—no distortion or redesign.

## Tool Guidance (media_generation)
When invoking photo editing tools, use the following prompt structure:
> "Apply a [Style Name] edit to this photo. Enhance lighting and color grading to a premium brand standard. **CRITICAL: Do not alter any human features, body shape, or skin texture. Preserve the subject's identity and anatomical integrity 100%.** Do not rotate or flip the image. Focus on [specific element like amber highlights/teal shadows or texture sharpening]. Output at [Aspect Ratio] for [Platform]. [Optional: Embed branding as a clean watermark in the top right corner]."
