# 🎨 Design System & DTCG Design Tokens
### *LITTLE BLUEPRINT: Scandinavian / Montessori Warmth Interface Architecture*
*Conforming to `ui-ux-pro-max` Standards: W3C DTCG Tokens, 8-State Component Specs, WCAG 2.2 AA*

---

## 1. Aesthetic Archetype & Psychology

* **Aesthetic Theme:** Warm Organic Scandinavian / Montessori Nursery.
* **Psychological Goal:** Evoke immediate calm, emotional safety, and cognitive relief for overstimulated parents. Zero harsh high-contrast neon or cold clinical blues.
* **Typography Pairing:**
  * **Display / Headline:** *Editorial New* / *Playfair Display* (Evokes literary heirlooms, storybooks, and emotional permanence).
  * **Body / System:** *Inter* / *SF Pro Display* (Tabular numbers, crisp readability at 14–16px, minimum 1.5 line height).

---

## 2. Official W3C DTCG Design Tokens (`design-tokens.json`)

```json
{
  "color": {
    "background": {
      "canvas": { "$value": "#FDFBF7", "$type": "color" },
      "surface": { "$value": "#FFFFFF", "$type": "color" },
      "subtle": { "$value": "#F4EFE6", "$type": "color" },
      "card": { "$value": "#FAF7F2", "$type": "color" }
    },
    "brand": {
      "terracotta": { "$value": "#D97D64", "$type": "color" },
      "terracotta-dark": { "$value": "#B85C45", "$type": "color" },
      "sage": { "$value": "#8A9A86", "$type": "color" },
      "soft-gold": { "$value": "#DFB15B", "$type": "color" },
      "oatmeal": { "$value": "#EFE9DE", "$type": "color" }
    },
    "text": {
      "primary": { "$value": "#2A2927", "$type": "color" },
      "secondary": { "$value": "#6B6862", "$type": "color" },
      "muted": { "$value": "#9B978F", "$type": "color" },
      "inverse": { "$value": "#FFFFFF", "$type": "color" }
    },
    "state": {
      "calm-green": { "$value": "#5A8A68", "$type": "color" },
      "caution-amber": { "$value": "#D9933B", "$type": "color" },
      "overload-rose": { "$value": "#C85A5A", "$type": "color" }
    }
  },
  "spacing": {
    "scale-1": { "$value": "4px", "$type": "dimension" },
    "scale-2": { "$value": "8px", "$type": "dimension" },
    "scale-3": { "$value": "12px", "$type": "dimension" },
    "scale-4": { "$value": "16px", "$type": "dimension" },
    "scale-6": { "$value": "24px", "$type": "dimension" },
    "scale-8": { "$value": "32px", "$type": "dimension" },
    "scale-12": { "$value": "48px", "$type": "dimension" }
  },
  "radii": {
    "button": { "$value": "9999px", "$type": "dimension" },
    "card": { "$value": "20px", "$type": "dimension" },
    "pill": { "$value": "12px", "$type": "dimension" }
  }
}
```

---

## 3. The 8-State Interactive Component Specification

Every interactive component (such as the **"Unlock My Child's Blueprint"** CTA or the **"Crisis Script"** button) adheres to the `plugin87` 8-state model:

1. **Default (`idle`)**: Background `#D97D64`, Text `#FFFFFF`, soft shadow `0 4px 14px rgba(217, 125, 100, 0.25)`.
2. **Hover (`pointer-over`)**: Background `#B85C45`, elevation scale `1.01`, smooth 150ms transition.
3. **Focus-Visible (`keyboard`)**: Crisp 2px outer focus ring in `#2A2927` with 2px offset (`ring-2 ring-offset-2`).
4. **Active (`pressed`)**: Scale `0.98`, subtle recessed shadow, immediate haptic response on iOS (`UIImpactFeedbackGenerator(style: .medium)`).
5. **Loading (`in-flight`)**: Text replaced by soft oatmeal-tinted pulsing spinner, `pointer-events-none`.
6. **Disabled (`inactive`)**: Background `#EFE9DE`, text `#9B978F`, `cursor-not-allowed`, `aria-disabled="true"`.
7. **Error (`invalid`)**: Terracotta border switches to `#C85A5A`, inline warning icon + descriptive text linked via `aria-describedby`.
8. **Empty (`zero-data`)**: Whimsical nursery woodcut illustration + reassuring 1-sentence prompt + 1 primary action button (never a blank void).

---

## 4. Accessibility & Touch Ergonomics (WCAG 2.2 AA)
* Minimum 44x44pt touch targets on all tap zones.
* Minimum 4.5:1 color contrast ratio on all body text against `#FDFBF7` canvas.
* Respects `prefers-reduced-motion` across all chart transitions and sensory gauge animations.
