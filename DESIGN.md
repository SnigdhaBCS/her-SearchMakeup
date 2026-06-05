---
name: Cosmic Bloom
colors:
  surface: '#181213'
  surface-dim: '#181213'
  surface-bright: '#3f3738'
  surface-container-lowest: '#120d0e'
  surface-container-low: '#201a1b'
  surface-container: '#241e1f'
  surface-container-high: '#2f2829'
  surface-container-highest: '#3a3334'
  on-surface: '#ecdfe0'
  on-surface-variant: '#d5c2c4'
  inverse-surface: '#ecdfe0'
  inverse-on-surface: '#362f30'
  outline: '#9d8d8f'
  outline-variant: '#504445'
  surface-tint: '#f3b7c2'
  primary: '#f3b7c2'
  on-primary: '#4c242e'
  primary-container: '#8e5d67'
  on-primary-container: '#ffe6e9'
  inverse-primary: '#80515b'
  secondary: '#ecb9c4'
  on-secondary: '#48272f'
  secondary-container: '#613c45'
  on-secondary-container: '#d9a8b2'
  tertiary: '#e8bbc2'
  on-tertiary: '#45282e'
  tertiary-container: '#866168'
  on-tertiary-container: '#ffe7e9'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9df'
  primary-fixed-dim: '#f3b7c2'
  on-primary-fixed: '#321019'
  on-primary-fixed-variant: '#653a44'
  secondary-fixed: '#ffd9e0'
  secondary-fixed-dim: '#ecb9c4'
  on-secondary-fixed: '#2f121a'
  on-secondary-fixed-variant: '#613c45'
  tertiary-fixed: '#ffd9df'
  tertiary-fixed-dim: '#e8bbc2'
  on-tertiary-fixed: '#2d1419'
  on-tertiary-fixed-variant: '#5e3e44'
  background: '#181213'
  on-background: '#ecdfe0'
  surface-variant: '#3a3334'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md-mobile:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  title-lg:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style
The brand personality is sophisticated yet approachable, blending the vastness of a "space" aesthetic with the intimate, tactile nature of high-end cosmetics. The target audience includes beauty enthusiasts and developers looking for a refined search experience.

The design style is **Modern Glassmorphism with Tonal Layering**. It avoids the harshness of pure black by using deep berry and charcoal-rose foundations. The interface should feel atmospheric and immersive, evoking a "midnight garden in orbit" emotional response—calm, focused, and premium.

## Colors
The palette is rooted in a dark, desaturated environment to ensure high legibility and reduced eye strain.

- **Primary (Deep Dusty Rose):** Used for key actions and primary brand moments.
- **Secondary (Muted Blush):** Used for interactive elements that require high visibility against dark backgrounds.
- **Tertiary (Dark Berry):** Used for surface-level containers and subtle depth variations.
- **Neutral (Charcoal Rose):** The foundation for backgrounds, providing a warmer alternative to pure black.
- **Accent (Soft Glow):** A pale pink used exclusively for highlights and glow effects to simulate starlight or luminescence.

## Typography
This design system employs a dual-personality typographic scale. **Playfair Display** provides an elegant, editorial feel for headers and brand moments. **Manrope** ensures the UI remains highly functional and modern. **JetBrains Mono** is used sparingly for labels and metadata to lean into the "search/data" aspect of the platform.

All serif headings should use slightly tighter letter-spacing to maintain a "high-fashion" look. Body text must maintain a generous line height for readability against dark backgrounds.

## Layout & Spacing
The layout follows a **Fluid Grid** model with a maximum container width to prevent line lengths from becoming unreadable on ultra-wide monitors.

A 12-column system is used for desktop, collapsing to 4 columns for mobile. Spacing is strictly based on a 4px baseline grid to ensure mathematical harmony. Elements should utilize generous negative space (whitespace) to allow the "space" aesthetic to breathe, preventing the UI from feeling cluttered.

## Elevation & Depth
Depth is created through **Glassmorphism and Tonal Layering**. Instead of traditional black shadows, use:

1.  **Backdrop Blurs:** Background surfaces should use a `20px` blur with a semi-transparent `tertiary` color fill (30-50% opacity).
2.  **Inner Glows:** Instead of drop shadows, use a 1px inner border in a lighter shade of the surface color to simulate a "rim light" effect.
3.  **Soft Outer Glows:** For primary "Go" buttons, use a diffused drop shadow that matches the `accent_glow_hex` color with 0px offset and a large blur radius (15-20px) at low opacity (20%).

## Shapes
The shape language is consistently **Rounded**, reflecting the soft edges of makeup palettes and organic cosmic forms. 

Standard components use a `0.5rem` radius. Cards and large containers utilize `rounded-xl` (`1.5rem`) to feel more welcoming and approachable. Search inputs should be fully pill-shaped (rounded-full) to distinguish them as the primary interaction point.

## Components
- **Search Inputs:** Pill-shaped with a subtle `1px` border using the primary color at 30% opacity. Upon focus, the border opacity increases to 100% with a soft internal glow.
- **Go Buttons:** High-contrast buttons using the `secondary` color for the background and `neutral` for the text. They feature a soft outer glow in the same hue to indicate interactivity.
- **Company Cards:** Use the Glassmorphism style—a dark berry background with a 15% opacity, a 1px top-border highlight, and a background blur. 
- **Chips/Tags:** Minimalist outlines using the `label-sm` typography style. No fill, just a subtle border.
- **Lists:** Clean rows separated by a horizontal rule in a faint `primary` color (10% opacity). Hover states should trigger a subtle background tint.
- **Checkboxes/Radios:** Softly rounded squares/circles using the primary color for the "checked" state, featuring a small "spark" or "star" icon instead of a standard checkmark if possible.