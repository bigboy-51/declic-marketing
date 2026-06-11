"""Design skill agent for visual systems and component libraries."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class DesignAgent(BaseAgent):
    """Creates visual systems, design guidelines, and component libraries."""

    DESIGN_PROMPT = """You are the Design Agent. Your role is to create scalable visual systems.

Responsibility:
- Design system definition (tokens, components, patterns)
- Accessibility first (WCAG 2.2 compliance)
- Typography & color systems
- Component library specifications
- Design principles & guidelines
- Responsive design patterns
- Dark/light mode support

Think in terms of:
- Design tokens (colors, spacing, typography)
- Reusable components (buttons, cards, forms)
- Layouts & grid systems
- Interactive patterns (hover, focus, active states)
- Accessibility (contrast, focus indicators, semantic HTML)
- Performance (file size, rendering)
- Scalability (how to extend the system)

Your output should be:
- Color palette with contrast ratios
- Typography system (font families, sizes, weights, line-heights)
- Component specifications (states, variations, usage)
- Layout guidelines (spacing, grid, breakpoints)
- Accessibility checklist
- Implementation guide (HTML, CSS, code examples)
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.DESIGN,
            system_prompt=self.DESIGN_PROMPT
        )
        self.skill_file = SKILLS_DIR / "design" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute design system creation task.

        Args:
            plan: {
                "brand_name": str,
                "brand_colors": list,
                "primary_audience": str,
                "accessibility_level": str,  # "WCAG A", "AA", "AAA"
                "design_style": str,  # "minimalist", "playful", "corporate"
                "platforms": list,  # ["web", "mobile", "desktop"]
                "components_needed": list  # ["buttons", "forms", "cards", etc]
            }
        """
        colors_str = ", ".join(plan.get('brand_colors', ['#000', '#FFF'])) if plan.get('brand_colors') else "To be defined"
        components_str = ", ".join(plan.get('components_needed', [])) if plan.get('components_needed') else "Core set"

        request = f"""
Brand: {plan.get('brand_name', 'Company')}
Brand Colors: {colors_str}
Primary Audience: {plan.get('primary_audience', 'Not specified')}
Design Style: {plan.get('design_style', 'Modern')}
Accessibility Target: {plan.get('accessibility_level', 'WCAG AA')}
Platforms: {', '.join(plan.get('platforms', ['web']))}
Components to Define: {components_str}

Please create a comprehensive design system:

1. Design Tokens
   - Color palette (primary, secondary, neutral, semantic)
   - Typography (font families, scale, line-heights)
   - Spacing system (unit-based)
   - Shadows/elevation
   - Border radius scale
   - Z-index scale

2. Color System
   - Primary color + variations (5-7 shades)
   - Secondary color + variations
   - Neutrals (grays, blacks, whites)
   - Semantic colors (success, error, warning, info)
   - Contrast ratios (all meeting WCAG {plan.get('accessibility_level', 'AA')})
   - Dark mode variations

3. Typography
   - Font family choices + fallbacks
   - Font scales (H1-H6, body, caption, small, etc)
   - Line heights for readability
   - Letter spacing
   - Font weights used

4. Component Library

   Core Components (define each with states):
   - Button (default, hover, active, disabled, loading)
   - Input field (empty, filled, error, disabled, focused)
   - Card (default, hover, selected)
   - Navigation (active, hover, disabled)
   - Modal/Dialog (open, close, overlay)
   - Alert/Toast (success, error, warning, info)
   - Badge (default, variants)
   - Dropdown/Select
   - Checkbox
   - Radio button
   - Toggle switch
   - Form validation (error message styling)

   For each component:
   - Visual specification
   - All states + variations
   - Spacing & sizing
   - Accessibility requirements
   - Usage guidelines
   - Code example (HTML/CSS)

5. Patterns

   Common Patterns:
   - Form patterns (login, signup, password reset)
   - Landing page layout
   - Navigation patterns (top nav, side nav, breadcrumbs)
   - Empty states
   - Loading states
   - Error handling
   - Success confirmation

6. Layout System
   - Grid (breakpoints: mobile, tablet, desktop, wide)
   - Spacing rules (margin, padding scale)
   - Container widths
   - Responsive behavior
   - Safe areas for mobile

7. Accessibility Specifications
   - Color contrast requirements (all color pairs)
   - Focus indicators (visible, consistent)
   - Keyboard navigation (tab order, shortcuts)
   - Semantic HTML structure
   - ARIA labels where needed
   - Alternative text for images
   - Form labels & error messages

8. Animation & Interaction
   - Transition timing (duration, easing)
   - Hover effects (subtle, not distracting)
   - Focus indicators (clear, accessible)
   - Loading animations (reassuring, not annoying)
   - Microcopy (button feedback, form hints)

9. Implementation Guide
   - Design tokens format (CSS variables, SCSS, JSON)
   - Component code structure
   - HTML/CSS best practices
   - JavaScript interaction patterns
   - Testing checklist (accessibility, responsiveness, browsers)

10. Maintenance & Evolution
    - How to add new components
    - How to request changes
    - Version control strategy
    - Design review process
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "design"
        }
