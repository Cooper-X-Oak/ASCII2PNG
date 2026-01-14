from typing import Dict, Tuple, Any


def get_theme(name: str, font_size: int) -> Dict[str, Any]:
    n = (name or "minimal").lower()
    
    # Base configuration
    base = {
        "font_size": font_size,
        "bg_style": "plain", # plain, grid, dots, circle, gradient
    }

    if n == "minimal" or n == "简约":
        # 简约风格：白底黑字，无冗余装饰
        return {
            **base,
            "bg": (255, 255, 255),
            "text": (33, 33, 33),
            "line": (100, 100, 100), # Darker line for better visibility
            "accent": (50, 50, 50),
            "bg_style": "plain",
        }
    
    if n == "business" or n == "商务":
        # 商务风格：深蓝/灰配色，网格背景
        return {
            **base,
            "bg": (240, 242, 245),
            "text": (44, 62, 80),
            "line": (160, 174, 192),
            "accent": (41, 128, 185),
            "bg_style": "grid",
            "grid_color": (220, 222, 225),
        }
        
    if n == "art" or n == "艺术":
        # 艺术风格：暖色调，圆形装饰 (用户喜欢的风格)
        return {
            **base,
            "bg": (253, 250, 245), # Creamy white
            "text": (93, 64, 55),  # Brownish
            "line": (180, 160, 150),
            "accent": (230, 81, 0),
            "bg_style": "circle",
            "circle_colors": [(255, 224, 178), (255, 204, 188)],
        }
        
    if n == "dark" or n == "暗黑":
        # 暗黑风格：类似 IDE 的高对比度
        return {
            **base,
            "bg": (30, 30, 30),
            "text": (220, 220, 220),
            "line": (80, 80, 80),
            "accent": (86, 156, 214), # VS Code Blue
            "bg_style": "plain",
        }

    # Fallback to Minimal
    return {
        **base,
        "bg": (255, 255, 255),
        "text": (33, 33, 33),
        "line": (100, 100, 100),
        "accent": (50, 50, 50),
        "bg_style": "plain",
    }
