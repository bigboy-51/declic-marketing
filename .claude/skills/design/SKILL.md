---
description: "Guide design direction for Declic. Visual systems, asset creation, design principles. Ensure consistency and clarity in all visuals."
keywords:
  - design
  - visual design
  - design systems
  - graphics
  - visual hierarchy
  - user experience
---

# Design Skill

## Purpose
Create a cohesive visual language for Declic that communicates trust, clarity, and results through every design.

## Before Designing

**Challenge:**
- [ ] What feeling should this design evoke? (Trust? Confidence? Warmth?)
- [ ] Who sees this? (First-time user? Power user? Investor?)
- [ ] What's the ONE thing they should notice?
- [ ] Does this reinforce brand (colors, fonts, tone)?
- [ ] Can it be understood in 3 seconds?

If you can't answer these, you're not ready to design.

---

## Design Principles (Karpathy-Style)

### 1. Clarity First
**Problem:** "That looks cool but I don't know what it does"

**Principle:** Visual hierarchy guides the eye. Clear is better than clever.

```
Weak: Five colors, multiple fonts, no clear focal point
Strong: One primary element (dark blue), supports (gray), clarity
```

### 2. Simplicity
**Problem:** "We're confusing users by showing everything"

**Principle:** Every element earns its place.

```
❌ Landing page: Hero image + 5 sections + testimonials + pricing + FAQ
✅ Landing page: Hero image + 1 CTA section + testimonial + CTA button
```

### 3. Consistency
**Problem:** "Our ads don't look like our website"

**Principle:** Same colors, fonts, photography style across all channels.

```
Brand system:
  Colors: 2 primary (blue, green)
  Fonts: 1 family (Inter)
  Photos: Real people, warm lighting
  Buttons: Consistent shape and size
```

### 4. Contrast
**Problem:** "Is that clickable? I can't tell"

**Principle:** Important elements stand out.

```
CTA Button: Bold blue on white (high contrast)
Secondary button: Blue text on white (low contrast)
Text on image: White with dark shadow (readable)
```

---

## Design System (Template)

### Color System
```
Primary (Trust, Action): #2563EB (Blue)
Secondary (Growth): #10B981 (Green)
Accent (Attention): #F59E0B (Amber)
Text (Dark): #1F2937
Background (Light): #F3F4F6
Border (Subtle): #E5E7EB
```

**Usage Rules:**
- Primary: CTAs, headers, key UI
- Secondary: Positive states, growth metrics
- Accent: Warnings, alerts, emphasis
- Neutral: Everything else

### Typography
```
Headlines: Inter Bold (700), #1F2937
  H1: 48px, line-height: 1.2
  H2: 32px, line-height: 1.3
  H3: 24px, line-height: 1.4

Body: Inter Regular (400), #374151
  Size: 16px
  Line-height: 1.6
  Letter-spacing: 0

Small: Inter Regular (400), #6B7280
  Size: 14px
  Line-height: 1.5
```

**Rules:**
- Max 2 font sizes in any layout
- Bold for emphasis, not for styling
- Line-height 1.6+ for readability

### Spacing System
```
8px base unit (multiply: 8, 16, 24, 32, 40, 48...)

Margins between sections: 40px (mobile) → 64px (desktop)
Padding inside containers: 16px (mobile) → 24px (desktop)
Gap between elements: 8px or 16px
```

**Rule:** Consistent spacing = professional appearance

### Buttons
```
Primary CTA:
  Background: #2563EB
  Text: White
  Padding: 12px 24px
  Border-radius: 6px
  Font: Inter Bold, 16px
  Hover: #1D4ED8 (darker blue)

Secondary Button:
  Background: Transparent
  Border: 1px #2563EB
  Text: #2563EB
  Same padding and radius
  Hover: Light blue background
```

### Cards & Containers
```
Background: White (#FFFFFF)
Border: 1px #E5E7EB
Border-radius: 8px
Padding: 24px
Shadow: 0 1px 3px rgba(0, 0, 0, 0.1)
```

**Rule:** Subtle shadows create depth without distraction

---

## Design Application

### Landing Page
```
Hero Section:
  Image (real investor or portfolio)
  Headline: One benefit
  Subheading: Proof or specificity
  CTA button: Clear action

Section 1 (Problem):
  Image (relatable)
  Headline: What customers struggle with
  2-3 bullet points

Section 2 (Solution):
  Product screenshot or animation
  Headline: How Declic solves it
  List of features

Section 3 (Proof):
  Testimonials (3 cards)
  Or data (case study metrics)

CTA Section:
  Headline: Clear benefit
  Button: "Try Free for 30 Days"
```

### Email
```
Header: Logo only (50px height)
Hero image: Tight crop, benefit-focused
Body: 
  Headline (benefit-driven)
  2-3 short paragraphs
  CTA button (primary color)
Footer: Social links, unsubscribe
```

**Mobile:** Stack vertically, tap targets 44px+ (clickable)

### Dashboard/UI
```
Sidebar: Dark (#1F2937), white text, 64px width
Header: Light background (#F3F4F6), logo + user menu
Main content: White background
Cards: Show data with visual indicators
  Green: Good (up, winning)
  Red: Bad (down, loss)
  Blue: Neutral (holding)

Spacing: 16px grid
Colors: Use system colors only
```

---

## Quality Checklist

**Before submitting design:**
- [ ] Hierarchy is clear (eye knows where to look)
- [ ] Colors match brand system
- [ ] Typography uses 2 sizes max
- [ ] Mobile responsive (stacks, readable)
- [ ] Spacing is consistent (8px grid)
- [ ] Buttons are obviously clickable
- [ ] Images are high-quality and on-brand
- [ ] No ornamental elements (earn their place)

---

## Common Mistakes

| ❌ Mistake | ✅ Fix |
|-----------|--------|
| Too many colors | Stick to system (5 colors max) |
| Ornamental graphics | Every graphic serves a purpose |
| Small CTAs | Buttons 44px minimum height, high contrast |
| Inconsistent spacing | Use 8px grid, stick to it |
| Stock photos that don't fit | Real people, real Declic context |
| Small text on image | White text + dark shadow = readable |
| No mobile version | Design mobile first, scale up |
| Looks cool but unclear | Ask: "Can my mom use this?" |

---

## Accessibility (Non-Negotiable)

- **Color contrast**: Text 4.5:1 ratio (dark on light)
- **Touch targets**: 44px minimum (mobile clicks)
- **Text size**: 16px minimum (readability)
- **Alt text**: Every image described for screen readers
- **Labels**: Every input field has a label
- **Motion**: Avoid flashy animations (can cause seizures)

---

## Success Metrics

Your design is working if:
- Users know what to do in < 3 seconds
- CTAs get > 2% click rate
- Mobile usability score > 90
- Accessibility score > 90
- Brand recognition (visual consistency)

---

## Output

When asked for design direction, provide:

1. **Design system** (colors, fonts, spacing)
2. **Component library** (buttons, cards, forms)
3. **Layout templates** (landing page, email, dashboard)
4. **Brand application** (how to use across channels)
5. **Accessibility checklist** (readability, contrast, mobility)
