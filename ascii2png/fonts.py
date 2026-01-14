import os
import sys
from PIL import ImageFont

# Windows default font paths
WIN_FONT_PATHS = {
    "serif": [
        "C:\\Windows\\Fonts\\times.ttf",
        "C:\\Windows\\Fonts\\simsun.ttc",  # Songti
    ],
    "sans": [
        "C:\\Windows\\Fonts\\msyh.ttc",    # Microsoft YaHei (First priority)
        "C:\\Windows\\Fonts\\msyh.ttf",
        "C:\\Windows\\Fonts\\simhei.ttf",
        "C:\\Windows\\Fonts\\arial.ttf"
    ],
    "mono": [
        "C:\\Windows\\Fonts\\consola.ttf",
        "C:\\Windows\\Fonts\\cour.ttf"
    ]
}

# MacOS default font paths
MAC_FONT_PATHS = {
    "serif": [
        "/System/Library/Fonts/Supplemental/Times.ttc",
        "/System/Library/Fonts/Songti.ttc",
    ],
    "sans": [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf"
    ],
    "mono": [
        "/System/Library/Fonts/Menlo.ttc",
        "/Library/Fonts/Courier New.ttf"
    ]
}

def get_font_paths():
    if sys.platform == "darwin":
        return MAC_FONT_PATHS
    return WIN_FONT_PATHS

def get_font(style: str = "sans", size: int = 20) -> ImageFont.FreeTypeFont:
    """
    Load a font by style (serif/sans/mono) and size.
    """
    paths_dict = get_font_paths()
    candidates = paths_dict.get(style, paths_dict["sans"])
    
    for path in candidates:
        if os.path.exists(path):
            try:
                # Try to load with high resolution for better quality
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    
    # Fallback
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

def get_title_font(size: int) -> ImageFont.FreeTypeFont:
    # Use Sans for title as it usually looks cleaner on screens
    return get_font("sans", size)

def get_body_font(size: int) -> ImageFont.FreeTypeFont:
    return get_font("sans", size)
