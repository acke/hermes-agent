---
name: remotion
description: Build programmatic videos with Remotion (React).
version: 4.0.535
author: Remotion (remotion-dev/skills)
license: Remotion License
platforms: [linux, macos, windows]
prerequisites:
  commands: [node, npx]
metadata:
  hermes:
    tags: [creative, video, animation, react, motion-graphics, captions]
    related_skills: [hyperframes, manim-video]
    category: creative
    requires_toolsets: [terminal]
    credits:
      - "Reference docs vendored from remotion-dev/skills (https://github.com/remotion-dev/skills)"
---

# Remotion Skill

Remotion makes videos from React components: a composition is a function of
the current frame, previewed in Remotion Studio and rendered to MP4/WebM with
`npx remotion render`. This skill routes to Remotion's official agent guidance
(vendored under `references/`). It does not install Remotion itself; projects
are scaffolded with `npx create-video@latest`.

## When to Use

- User asks to make, edit, or render a video with Remotion or React.
- Animated captions, motion graphics, data/map explainers, audio-reactive visuals.
- Building a SaaS or app around `<Player>` or server-side/Lambda rendering.

Prefer `hyperframes` for HTML/GSAP compositions and `manim-video` for math explainers.

## Prerequisites

- Node.js and `npx` on PATH (FFmpeg is bundled by Remotion for rendering).
- Network access for `npm install` and, in some references, Remotion docs lookup.

## How to Run

1. Read `references/ROUTER.md` first: it lists which reference to load per task.
2. Load only the reference(s) that match the task via `read_file`.

## Quick Reference

| Task | Load |
|------|------|
| New video / project | `references/remotion-create/REFERENCE.md` |
| Writing compositions, animation, effects | `references/remotion-markup/REFERENCE.md` |
| Captions / subtitles | `references/remotion-captions/REFERENCE.md` |
| Maps and geo flyovers | `references/remotion-maps/REFERENCE.md` |
| Trimming, cropping, metadata (Mediabunny) | `references/remotion-multimedia/REFERENCE.md` |
| Studio-editable props | `references/remotion-interactivity/REFERENCE.md` |
| Preview in Studio | `references/remotion-studio/REFERENCE.md` |
| Rendering / export | `references/remotion-render/REFERENCE.md` |
| Player, Lambda, SaaS apps | `references/remotion-saas/REFERENCE.md` |
| API lookup | `references/remotion-docs/REFERENCE.md` |
| Upgrading Remotion | `references/remotion-upgrade/REFERENCE.md` |

## Procedure

1. Scaffold or detect the project (`remotion-create`).
2. Start Studio with `terminal(background=true)` (`npx remotion studio --no-open`)
   and share the URL so the user can watch progress.
3. Write the composition following `remotion-markup`.
4. Render only when the user explicitly asks to export.

## Pitfalls

- Users may edit files between turns; never overwrite surprising changes.
- Don't render by default; preview first.
- Remotion has its own license terms (free for individuals/small teams, paid
  for larger companies); mention it when setting up commercial projects.

## Verification

- Studio loads and the composition renders a frame at `/<composition-id>`.
- `npx remotion render <id> out.mp4` exits 0 when an export was requested.
