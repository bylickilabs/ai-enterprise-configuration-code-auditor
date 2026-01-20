BADGE_COLORS = {
    "LOW": "#4caf50",
    "MEDIUM": "#ff9800",
    "HIGH": "#ff5722",
    "CRITICAL": "#f44336"
}

def generate_badge(risk_level: str) -> str:
    color = BADGE_COLORS.get(risk_level, "#9e9e9e")

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="140" height="20">
  <rect width="70" height="20" fill="#555"/>
  <rect x="70" width="70" height="20" fill="{color}"/>
  <text x="35" y="14" fill="#fff" font-size="11" text-anchor="middle">risk</text>
  <text x="105" y="14" fill="#fff" font-size="11" text-anchor="middle">{risk_level}</text>
</svg>
"""
