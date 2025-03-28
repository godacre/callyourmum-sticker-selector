import customtkinter as ctk
import tkinter as tk
from tkinter import font as tkFont
import math
from typing import Dict, List, Tuple, Any, Optional
import webbrowser # <-- IMPORTED webbrowser

# --- CYBERPUNK PINBALL THEME COLORS (Unchanged) ---
COLOR_BG = "#0d021a"
COLOR_BG_LIGHT = "#210b38"
COLOR_FRAME_BG = "transparent"
COLOR_WIDGET_BG = "#1a072e"
COLOR_ENTRY_BG = "#08010f"
COLOR_PINK = "#ff00ff"
COLOR_TEAL = "#00ffff"
COLOR_LIME = "#a8ff00"
COLOR_PURPLE = "#9d00ff"
COLOR_ORANGE = "#ff8000"
COLOR_TEXT = "#f0f0f0"
COLOR_TEXT_DIM = "#887cad"
COLOR_TEXT_NEON = COLOR_TEAL
COLOR_BORDER = COLOR_PURPLE
COLOR_BORDER_WIDGET = COLOR_PINK
COLOR_BORDER_FOCUS = COLOR_LIME
COLOR_BUTTON = COLOR_TEAL
COLOR_BUTTON_HOVER = COLOR_PINK
COLOR_BUTTON_TEXT = "#000000"
COLOR_SCORE_TEXT = COLOR_LIME
COLOR_GRAFFITI = COLOR_LIME
COLOR_LINK = COLOR_TEAL # <-- ADDED Color for clickable links

# --- VENDOR DATA (Illustrative Estimates for Vancouver, BC - ADDED URLs) ---
# *** DISCLAIMER: These are ROUGH, ILLUSTRATIVE ESTIMATES for Vancouver, BC ONLY. NOT LIVE/ACCURATE. ***
websites_data: Dict[str, Dict[str, Any]] = {
    "StickerMule": {
        "url": "https://www.stickermule.com/", # <-- ADDED URL
        "notes": "Quality focus, fast US option.",
        "sizes": {"1x1": {10: 20, 50: 48, 100: 60, 500: 190, 1000: 245}, "2x2": {10: 27, 50: 55, 100: 68, 500: 205, 1000: 270}, "3x3": {10: 34, 50: 60, 100: 80, 500: 215, 1000: 340}, "4x4": {10: 40, 50: 68, 100: 95, 500: 245, 1000: 400}, "5x5": {10: 48, 50: 75, 100: 100, 500: 255, 1000: 430}, "6x4": {10: 43, 50: 70, 100: 98, 500: 250, 1000: 420}, "2x3": {10: 30, 50: 57, 100: 75, 500: 210, 1000: 295}, "2x4": {10: 32, 50: 59, 100: 78, 500: 215, 1000: 310}, "3x5": {10: 38, 50: 65, 100: 88, 500: 230, 1000: 350}, "4x6": {10: 46, 50: 78, 100: 105, 500: 265, 1000: 430}, "5x7": {10: 52, 50: 84, 100: 110, 500: 275, 1000: 460}},
        "quantities": [10, 50, 100, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.1, "Satin": 1.15}, "shapes": {"Square": 1.0, "Circle": 1.05, "Rectangle": 1.0, "Oval": 1.1, "Triangle": 1.08, "Hexagon": 1.12, "Star": 1.15}, "colors": {"Full Color": 1.0, "Black & White": 0.95}, "delivery_speeds": {"Standard": 1.0, "Express": 1.2, "Rush": 1.5}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0, "Back Printing": 1.2}, "materials": {"Vinyl": 1.0, "Paper": 0.9, "Clear": 1.1, "Holographic": 1.3}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.05}, "discounts": {100: 0.95, 500: 0.9, 1000: 0.85},
        "shipping_est_bc": 20.00, "tax_rate_bc": 0.00, "duty_handling_est": 15.00
    },
    "Vistaprint": {
        "url": "https://www.vistaprint.ca/", # <-- ADDED URL (.ca for Canada)
        "notes": "Budget basics, watch add-ons.",
         "sizes": {"1x1": {10: 19, 50: 40, 100: 55, 500: 160, 1000: 215}, "2x2": {10: 24, 50: 48, 100: 60, 500: 175, 1000: 245}, "3x3": {10: 30, 50: 55, 100: 75, 500: 195, 1000: 295}, "4x4": {10: 35, 50: 65, 100: 88, 500: 215, 1000: 365}, "5x5": {10: 40, 50: 70, 100: 95, 500: 235, 1000: 390}, "6x4": {10: 38, 50: 68, 100: 92, 500: 230, 1000: 380}, "2x3": {10: 26, 50: 52, 100: 68, 500: 180, 1000: 265}, "2x4": {10: 27, 50: 55, 100: 70, 500: 190, 1000: 275}, "3x5": {10: 32, 50: 60, 100: 80, 500: 210, 1000: 315}, "4x6": {10: 39, 50: 75, 100: 98, 500: 245, 1000: 395}, "5x7": {10: 45, 50: 80, 100: 105, 500: 255, 1000: 415}},
        "quantities": [10, 50, 100, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.05}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.05}, "colors": {"Full Color": 1.0, "Black & White": 0.9}, "delivery_speeds": {"Standard": 1.0, "Express": 1.25, "Rush": 1.6}, "extras": {"Waterproof": 1.1, "UV Coating": 1.1}, "materials": {"Vinyl": 1.1, "Paper": 1.0}, "adhesive_types": {"Permanent": 1.0}, "discounts": {100: 0.98, 500: 0.92, 1000: 0.88},
        "shipping_est_bc": 15.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "StickerYou": {
        "url": "https://www.stickeryou.com/en-ca/", # <-- ADDED URL (.ca)
        "notes": "Canadian! Die-cut specialist.",
         "sizes": {"1x1": {10: 18, 50: 40, 100: 55, 500: 160, 1000: 220}, "2x2": {10: 22, 50: 45, 100: 60, 500: 170, 1000: 250}, "3x3": {10: 26, 50: 50, 100: 70, 500: 180, 1000: 300}, "4x4": {10: 32, 50: 60, 100: 80, 500: 200, 1000: 350}},
        "quantities": [10, 50, 100, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0, "Clear": 1.1}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0, "Custom": 1.1}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.3, "Rush": 1.7}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0, "Back Printing": 1.25}, "materials": {"Vinyl": 1.0, "Paper": 0.85, "Clear": 1.1, "Holographic": 1.4, "Glitter": 1.4}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.1}, "discounts": {100: 0.96, 500: 0.90, 1000: 0.85},
        "shipping_est_bc": 12.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "Jukebox Print": {
        "url": "https://www.jukeboxprint.com/", # <-- ADDED URL
        "notes": "Vancouver Local! Premium options.",
         "sizes": {"1x1": {100: 50, 500: 150, 1000: 200}, "2x2": {100: 60, 500: 170, 1000: 250}, "3x3": {100: 75, 500: 200, 1000: 300}, "4x4": {100: 90, 500: 240, 1000: 380}},
        "quantities": [100, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0, "Silk": 1.1}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.05, "Custom": 1.15}, "colors": {"Full Color": 1.0, "Spot Color": 1.2}, "delivery_speeds": {"Standard": 1.0, "Express": 1.3, "Rush": 1.6}, "extras": {"Waterproof": 1.0, "UV Coating": 1.05, "Foil": 1.5}, "materials": {"Vinyl": 1.0, "Paper": 0.95, "Clear": 1.1, "Textured Paper": 1.2, "Wood": 2.0}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.1}, "discounts": {250: 0.97, 500: 0.93, 1000: 0.88},
        "shipping_est_bc": 15.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "GotPrint": {
        "url": "https://www.gotprint.com/", # <-- ADDED URL
        "notes": "Budget US option.",
         "sizes": {"1x1": {100: 48, 500: 120, 1000: 175}, "2x2": {100: 55, 500: 135, 1000: 200}, "3x3": {100: 68, 500: 160, 1000: 255}, "4x4": {100: 80, 500: 190, 1000: 310}},
        "quantities": [100, 250, 500, 1000, 5000],
        "textures": {"Matte": 1.0, "Glossy": 1.0, "UV Gloss": 1.05}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.35, "Rush": 1.7}, "extras": {"Waterproof": 1.1, "UV Coating": 1.0}, "materials": {"Vinyl": 1.1, "Paper": 1.0, "BOPP": 1.05}, "adhesive_types": {"Permanent": 1.0}, "discounts": {500: 0.92, 1000: 0.88, 5000: 0.80},
        "shipping_est_bc": 25.00, "tax_rate_bc": 0.00, "duty_handling_est": 20.00
      },
    "StickerApp": {
        "url": "https://stickerapp.com/", # <-- ADDED URL
        "notes": "Specialty materials focus.",
         "sizes": {"1x1": {50: 55, 100: 75, 500: 215, 1000: 285}, "2x2": {50: 60, 100: 80, 500: 235, 1000: 350}, "3x3": {50: 68, 100: 95, 500: 255, 1000: 420}, "4x4": {50: 80, 100: 108, 500: 285, 1000: 485}},
        "quantities": [10, 50, 100, 500, 1000],
        "textures": {"Matte": 1.05, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0, "Custom": 1.05}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.4, "Rush": 1.8}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0, "Back Printing": 1.2}, "materials": {"Vinyl": 1.0, "Paper": 0.9, "Clear": 1.1, "Holographic": 1.3, "Mirror": 1.3, "Prism": 1.35}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.1}, "discounts": {100: 0.97, 500: 0.92, 1000: 0.87},
        "shipping_est_bc": 22.00, "tax_rate_bc": 0.00, "duty_handling_est": 18.00
      },
    "Moo": {
        "url": "https://www.moo.com/ca/", # <-- ADDED URL (.ca)
        "notes": "Premium feel, higher price.",
         "sizes": {"1x1": {50: 60, 100: 80, 500: 245, 1000: 380}, "2x2": {50: 68, 100: 95, 500: 270, 1000: 430}, "3x3": {50: 75, 100: 108, 500: 325, 1000: 510}, "4x4": {50: 88, 100: 128, 500: 380, 1000: 600}},
        "quantities": [50, 100, 500, 1000],
        "textures": {"Matte": 1.05, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Custom": 1.2}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.4, "Rush": 1.8}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0}, "adhesive_types": {"Permanent": 1.0}, "discounts": {100: 0.98, 500: 0.94, 1000: 0.90},
        "shipping_est_bc": 25.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "Stickeryeti": {
        "url": "https://www.stickeryeti.com/", # <-- ADDED URL
        "notes": "EU based, wide range, ships intl.",
        "sizes": {"1x1": {50: 50, 100: 65, 500: 180, 1000: 240}, "2x2": {50: 55, 100: 70, 500: 200, 1000: 280}, "3x3": {50: 65, 100: 85, 500: 230, 1000: 330}, "4x4": {50: 75, 100: 100, 500: 260, 1000: 390}},
        "quantities": [50, 100, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0, "Custom": 1.1}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.35}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0, "Clear": 1.1, "Holographic": 1.25, "Paper": 0.9}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.1}, "discounts": {250: 0.95, 500: 0.9, 1000: 0.85},
        "shipping_est_bc": 30.00, "tax_rate_bc": 0.00, "duty_handling_est": 25.00
      },
    "Awesome Merch": {
        "url": "https://www.awesomemerchandise.com/", # <-- ADDED URL
        "notes": "UK based, merch focus, ships intl.",
         "sizes": {"1x1": {50: 58, 100: 78, 500: 220, 1000: 300}, "2x2": {50: 65, 100: 85, 500: 250, 1000: 350}, "3x3": {50: 75, 100: 100, 500: 290, 1000: 410}, "4x4": {50: 88, 100: 120, 500: 340, 1000: 490}},
        "quantities": [25, 50, 100, 250, 500, 1000],
        "textures": {"Matte": 1.05, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0, "Custom": 1.1}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.4}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0, "Paper": 0.9, "Glitter": 1.4, "Clear": 1.15}, "adhesive_types": {"Permanent": 1.0}, "discounts": {250: 0.96, 500: 0.91, 1000: 0.86},
        "shipping_est_bc": 35.00, "tax_rate_bc": 0.00, "duty_handling_est": 25.00
      },
    "Signs.com": {
        "url": "https://www.signs.com/", # <-- ADDED URL
        "notes": "US based, focus on signs but does stickers.",
         "sizes": {"2x2": {50: 50, 100: 65, 500: 190, 1000: 260}, "3x3": {50: 60, 100: 80, 500: 220, 1000: 310}, "4x4": {50: 70, 100: 95, 500: 250, 1000: 370}},
        "quantities": [10, 25, 50, 100, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.05, "Custom": 1.15}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.3, "Rush": 1.6}, "extras": {"Waterproof": 1.0, "UV Coating": 1.05}, "materials": {"Vinyl": 1.0, "Clear": 1.1}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.1}, "discounts": {250: 0.95, 500: 0.9, 1000: 0.85},
        "shipping_est_bc": 28.00, "tax_rate_bc": 0.00, "duty_handling_est": 20.00
      },
    "Rockin' Monkey": {
        "url": "https://rockinmonkey.com/", # <-- ADDED URL
        "notes": "US based, custom shape experts.",
        "sizes": {"2x2": {50: 60, 100: 75, 500: 210, 1000: 290}, "3x3": {50: 70, 100: 90, 500: 240, 1000: 340}, "4x4": {50: 80, 100: 110, 500: 280, 1000: 400}},
        "quantities": [25, 50, 100, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0, "Custom": 1.05}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.3}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0, "Clear": 1.1, "Holographic": 1.3}, "adhesive_types": {"Permanent": 1.0}, "discounts": {250: 0.96, 500: 0.91, 1000: 0.86},
        "shipping_est_bc": 25.00, "tax_rate_bc": 0.00, "duty_handling_est": 20.00
      },
    "Sticker Beaver": {
        "url": "https://stickerbeaver.com/", # <-- ADDED URL
        "notes": "Canadian! Simple process.",
        "sizes": {"2x2": {50: 45, 100: 58, 500: 175, 1000: 240}, "3x3": {50: 55, 100: 72, 500: 195, 1000: 290}, "4x4": {50: 65, 100: 88, 500: 230, 1000: 350}},
        "quantities": [50, 100, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0, "Custom": 1.1}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.25}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0, "Clear": 1.1}, "adhesive_types": {"Permanent": 1.0}, "discounts": {250: 0.97, 500: 0.92, 1000: 0.87},
        "shipping_est_bc": 14.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "Make My Stickers": {
        "url": "https://makemystickers.com/", # <-- ADDED URL
        "notes": "Canadian? Basic options, maybe cheaper.",
         "sizes": {"2x2": {50: 40, 100: 55, 500: 165, 1000: 225}, "3x3": {50: 50, 100: 68, 500: 185, 1000: 270}, "4x4": {50: 60, 100: 80, 500: 215, 1000: 320}},
        "quantities": [50, 100, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.0}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0, "Express": 1.3}, "extras": {"Waterproof": 1.05, "UV Coating": 1.05}, "materials": {"Vinyl": 1.0}, "adhesive_types": {"Permanent": 1.0}, "discounts": {250: 0.96, 500: 0.91, 1000: 0.86},
        "shipping_est_bc": 15.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "My Sticker Face": {
        "url": "https://mystickerface.com/", # <-- ADDED URL
        "notes": "Canadian! Face stickers focus, but does custom.",
         "sizes": {"2x2": {50: 70, 100: 90}, "3x3": {50: 80, 100: 110}},
        "quantities": [10, 25, 50, 100],
        "textures": {"Glossy": 1.0}, "shapes": {"Circle": 1.0, "Custom": 1.0}, "colors": {"Full Color": 1.0}, "delivery_speeds": {"Standard": 1.0}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0}, "adhesive_types": {"Permanent": 1.0}, "discounts": {},
        "shipping_est_bc": 10.00, "tax_rate_bc": 0.12, "duty_handling_est": 0.00
      },
    "eStickers": {
        "url": "https://www.estickers.com/", # <-- ADDED URL
        "notes": "US Based, long history.",
         "sizes": {"1x1": {125: 60, 500: 130, 1000: 180}, "2x2": {125: 70, 500: 150, 1000: 210}, "3x3": {125: 85, 500: 180, 1000: 260}},
        "quantities": [125, 250, 500, 1000],
        "textures": {"Matte": 1.0, "Glossy": 1.0, "UV Gloss": 1.05}, "shapes": {"Square": 1.0, "Circle": 1.0, "Rectangle": 1.0, "Oval": 1.05, "Custom": 1.1}, "colors": {"Full Color": 1.0, "Spot Color": 1.1}, "delivery_speeds": {"Standard": 1.0, "Rush": 1.5}, "extras": {"Waterproof": 1.0, "UV Coating": 1.0}, "materials": {"Vinyl": 1.0, "Paper": 0.9, "Polyester": 1.1}, "adhesive_types": {"Permanent": 1.0, "Removable": 1.05}, "discounts": {500: 0.93, 1000: 0.88},
        "shipping_est_bc": 26.00, "tax_rate_bc": 0.00, "duty_handling_est": 20.00
      },
}

# --- App Constants (Unchanged) ---
APP_WIDTH = 1800
APP_HEIGHT = 1000

# --- CTk Settings (Unchanged) ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Helper (Unchanged)
def get_all_options(category_key: str) -> List[str]:
    options = set()
    for data in websites_data.values():
        options.update(data.get(category_key, {}).keys())
    if category_key == 'extras':
        options.update(["Waterproof", "UV Coating", "Back Printing"]) # Ensure these base extras are always options
    return sorted(list(options))

# --- Main Application Class ---
class StickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("⚡ callyourmumslaps ⚡")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.configure(fg_color=COLOR_BG)

        # --- Fonts (Unchanged) ---
        try:
            self.title_font = ctk.CTkFont(family="Impact", size=48, weight="bold")
            self.label_font = ctk.CTkFont(family="Lucida Console", size=18, weight="bold")
            self.widget_font = ctk.CTkFont(family="Consolas", size=16)
            self.small_font = ctk.CTkFont(family="Consolas", size=14)
            self.button_font = ctk.CTkFont(family="Impact", size=36, weight="bold")
            self.result_font = ctk.CTkFont(family="Courier New", size=16, weight="bold")
            self.result_small_font = ctk.CTkFont(family="Courier New", size=14)
            self.graffiti_font = ctk.CTkFont(family="Impact", size=90, weight="bold", slant="italic")
            self.small_graffiti_font = ctk.CTkFont(family="Impact", size=60, weight="bold", slant="italic")
        except Exception as e:
            print(f"Warning: Font loading error ({e}). Using fallback fonts.")
            self.title_font = ctk.CTkFont(family="Arial Black", size=44)
            self.label_font = ctk.CTkFont(family="Arial", size=17, weight="bold")
            self.widget_font = ctk.CTkFont(family="Arial", size=15)
            self.small_font = ctk.CTkFont(family="Arial", size=13)
            self.button_font = ctk.CTkFont(family="Arial Black", size=32)
            self.result_font = ctk.CTkFont(family="Courier New", size=15, weight="bold")
            self.result_small_font = ctk.CTkFont(family="Courier New", size=13)
            self.graffiti_font = ctk.CTkFont(family="Arial Black", size=80, weight="bold", slant="italic")
            self.small_graffiti_font = ctk.CTkFont(family="Arial Black", size=55, weight="bold", slant="italic")

        # --- Data & State Variables (Unchanged) ---
        self.size_var = ctk.StringVar(value="3x3")
        self.quantity_var = ctk.StringVar(value="100")
        self.quantity_preset_var = ctk.StringVar(value="100")
        self.texture_var = ctk.StringVar(value="Glossy")
        self.shape_var = ctk.StringVar(value="Square")
        self.color_var = ctk.StringVar(value="Full Color")
        self.delivery_speed_var = ctk.StringVar(value="Standard")
        self.material_var = ctk.StringVar(value="Vinyl")
        self.adhesive_type_var = ctk.StringVar(value="Permanent")
        self.extras_vars = {name: ctk.BooleanVar() for name in get_all_options('extras')}
        self.result_data: List[Tuple[str, float, float, float, float, float, float, str]] = []
        self.appearance_mode_var = ctk.StringVar(value="dark")

        # --- Background Canvas (Unchanged) ---
        self.canvas = tk.Canvas(self, width=APP_WIDTH, height=APP_HEIGHT, bg=COLOR_BG, highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self._draw_canvas_background()

        # --- Create and Place UI Elements (Unchanged Structure) ---
        self._create_title_area()
        self._create_config_area() # Contains the layout fixes
        self._create_results_area()
        self._create_go_button_area()

        # --- Bind quantity update (Unchanged) ---
        self.quantity_preset_var.trace_add("write", self._update_quantity_from_preset)
        self._update_results_display()


    # --- Drawing methods (Unchanged) ---
    def _draw_canvas_background(self):
        """Draws the static cyberpunk pinball background elements for 1080p - MkII Layout."""
        self.canvas.delete("all")
        # Outer border with padding from edge
        border_pad = 8
        self.canvas.create_rectangle(border_pad, border_pad, APP_WIDTH - border_pad, APP_HEIGHT - border_pad, outline=COLOR_PURPLE, width=5)

        grid_spacing = 40
        for x in range(0, APP_WIDTH, grid_spacing):
             self.canvas.create_line(x, 0, x, APP_HEIGHT, fill=COLOR_BG_LIGHT, width=1, dash=(2, 4))
        for y in range(0, APP_HEIGHT, grid_spacing):
             self.canvas.create_line(0, y, APP_WIDTH, y, fill=COLOR_BG_LIGHT, width=1, dash=(2, 4))

        # --- Zone Definitions for 1080p (No Options Zone) ---
        cfg_x, cfg_y, cfg_w, cfg_h = 0.02, 0.10, 0.30, 0.75
        cfg_title_y_offset = 20
        res_x, res_y, res_w, res_h = 0.34, 0.10, 0.64, 0.75
        res_title_y_offset = 20
        go_x, go_y, go_w, go_h = 0.02, cfg_y + cfg_h + 0.01, 0.96, 1.0 - (cfg_y + cfg_h + 0.01) - 0.02
        go_title_y_offset = 15

        # --- Draw Zones ---
        cfg_points = [ APP_WIDTH * cfg_x, APP_HEIGHT * cfg_y, APP_WIDTH * (cfg_x + cfg_w), APP_HEIGHT * cfg_y, APP_WIDTH * (cfg_x + cfg_w - 0.01), APP_HEIGHT * (cfg_y + cfg_h), APP_WIDTH * (cfg_x + 0.01), APP_HEIGHT * (cfg_y + cfg_h) ]
        self.canvas.create_polygon(cfg_points, outline=COLOR_PINK, width=4, fill="")
        self.canvas.create_text(APP_WIDTH * (cfg_x + cfg_w / 2), APP_HEIGHT * cfg_y - cfg_title_y_offset, text=">> CONFIG DECK <<", font=self.label_font, fill=COLOR_PINK, anchor="s")
        self.canvas.create_rectangle(APP_WIDTH * res_x, APP_HEIGHT * res_y, APP_WIDTH * (res_x + res_w), APP_HEIGHT * (res_y + res_h), outline=COLOR_LIME, width=4)
        for i in range(int(APP_HEIGHT * res_y + 10), int(APP_HEIGHT * (res_y + res_h) - 10), 8):
            self.canvas.create_line(APP_WIDTH * res_x + 5, i, APP_WIDTH * (res_x + res_w) - 5, i, fill=COLOR_BG_LIGHT, width=2)
        self.canvas.create_text(APP_WIDTH * (res_x + res_w / 2), APP_HEIGHT * res_y - res_title_y_offset, text="!! SCORE FEED !!", font=self.label_font, fill=COLOR_LIME, anchor="s")
        cx, cy = APP_WIDTH * 0.5, APP_HEIGHT * (go_y + go_h / 2)
        radius = min(APP_WIDTH * go_w * 0.2, APP_HEIGHT * go_h * 0.8) * 0.5
        self.canvas.create_oval(cx - radius * 2.0, cy - radius * 2.0, cx + radius * 2.0, cy + radius * 2.0, fill="", outline=COLOR_TEAL, width=6)
        self.canvas.create_oval(cx - radius * 1.4, cy - radius * 1.4, cx + radius * 1.4, cy + radius * 1.4, fill="", outline=COLOR_PINK, width=4)
        self.canvas.create_oval(cx - radius * 0.8, cy - radius * 0.8, cx + radius * 0.8, cy + radius * 0.8, fill=COLOR_TEAL, outline="")
        self.canvas.create_text(cx, cy - radius * 2.5, text="LAUNCH!", font=self.label_font, fill=COLOR_TEAL, anchor="s")
        graffiti_x = cx
        graffiti_y = cy - radius * 3.5
        self.canvas.create_text(graffiti_x, graffiti_y, text="FAKR", font=self.graffiti_font, fill=COLOR_GRAFFITI, anchor="center", angle=-10)

        # --- Decorative Elements ---
        self._draw_glitch_shape(0.5, 0.04, 0.03, COLOR_LIME, COLOR_PINK)
        self._draw_glitch_shape(0.05, 0.06, 0.02, COLOR_TEAL, COLOR_PURPLE)
        self._draw_glitch_shape(0.95, 0.06, 0.02, COLOR_TEAL, COLOR_PURPLE)
        self.canvas.create_line(APP_WIDTH*0.15, APP_HEIGHT*0.08, APP_WIDTH*0.08, APP_HEIGHT*0.4, APP_WIDTH*0.18, APP_HEIGHT*0.80, fill=COLOR_PURPLE, width=4, smooth=True)
        self.canvas.create_line(APP_WIDTH*0.85, APP_HEIGHT*0.08, APP_WIDTH*0.92, APP_HEIGHT*0.4, APP_WIDTH*0.82, APP_HEIGHT*0.80, fill=COLOR_PINK, width=4, smooth=True)

        # --- Bottom Left Graffiti ---
        graffiti_bl_x = border_pad + 20
        graffiti_bl_y = APP_HEIGHT - border_pad - 15
        self.canvas.create_text(graffiti_bl_x, graffiti_bl_y, text="FAKR", font=self.small_graffiti_font, fill=COLOR_GRAFFITI, anchor="sw", angle=5)

    def _draw_glitch_shape(self, rel_x, rel_y, rel_size, fill_color, outline_color):
        # --- Unchanged ---
        cx, cy = APP_WIDTH * rel_x, APP_HEIGHT * rel_y
        r = min(APP_WIDTH, APP_HEIGHT) * rel_size
        points = []
        num_points = 6
        for i in range(num_points):
            angle_rad = math.pi / num_points * i * 2 + (math.pi / 6)
            offset_x = (math.cos(angle_rad + i) * r * 0.2)
            offset_y = (math.sin(angle_rad * 2) * r * 0.2)
            points.extend([ cx + r * math.cos(angle_rad) + offset_x, cy - r * math.sin(angle_rad) + offset_y ])
        try: self.canvas.create_polygon(points, fill=fill_color, outline=outline_color, width=1)
        except tk.TclError: pass

    # --- UI Creation methods ---
    def _create_title_area(self):
        # --- Unchanged ---
        title_label = ctk.CTkLabel(self, text="< callyourmumslaps >", font=self.title_font, text_color=COLOR_PINK, fg_color="transparent")
        title_label.place(relx=0.5, rely=0.05, anchor="center")

    def _create_config_area(self): # <-- THIS METHOD CONTAINS THE LAYOUT FIXES
        # Use zone definitions from _draw_canvas_background
        cfg_x, cfg_y, cfg_w, cfg_h = 0.02, 0.10, 0.30, 0.75 # Updated height
        frame = ctk.CTkFrame(self, fg_color=COLOR_FRAME_BG, border_width=0)
        # Place with more padding
        frame.place(relx=cfg_x + 0.01, rely=cfg_y + 0.01, relwidth=cfg_w - 0.02, relheight=cfg_h - 0.02, anchor="nw")

        frame.grid_columnconfigure(0, weight=1)
        # Adjust row weights - give groups weight, less for switch/info
        frame.grid_rowconfigure((0,1,2), weight=2) # Groups 1, 2, 3
        frame.grid_rowconfigure(3, weight=1)       # Row for switch/info (Misc Frame)

        pad_x = 15; pad_y = 8; widget_corner_radius = 5; label_pad_y = 4

        # --- Groups 1, 2 (Content Unchanged) ---
        group1 = ctk.CTkFrame(frame, fg_color=COLOR_WIDGET_BG, corner_radius=widget_corner_radius, border_width=2, border_color=COLOR_BORDER_WIDGET)
        group1.grid(row=0, column=0, padx=pad_x, pady=pad_y, sticky="nsew"); group1.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(group1, text="SIZE:", font=self.label_font, text_color=COLOR_TEXT).grid(row=0, column=0, padx=pad_x, pady=label_pad_y, sticky="w")
        size_combo = ctk.CTkComboBox(group1, variable=self.size_var, values=get_all_options('sizes'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius); size_combo.grid(row=0, column=1, padx=pad_x, pady=label_pad_y, sticky="ew")
        ctk.CTkLabel(group1, text="SHAPE:", font=self.label_font, text_color=COLOR_TEXT).grid(row=1, column=0, padx=pad_x, pady=label_pad_y, sticky="w")
        shape_combo = ctk.CTkComboBox(group1, variable=self.shape_var, values=get_all_options('shapes'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius); shape_combo.grid(row=1, column=1, padx=pad_x, pady=label_pad_y, sticky="ew")
        ctk.CTkLabel(group1, text="MATERIAL:", font=self.label_font, text_color=COLOR_TEXT).grid(row=2, column=0, padx=pad_x, pady=label_pad_y, sticky="w")
        material_combo = ctk.CTkComboBox(group1, variable=self.material_var, values=get_all_options('materials'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius); material_combo.grid(row=2, column=1, padx=pad_x, pady=label_pad_y, sticky="ew")

        group2 = ctk.CTkFrame(frame, fg_color=COLOR_WIDGET_BG, corner_radius=widget_corner_radius, border_width=2, border_color=COLOR_BORDER_WIDGET)
        group2.grid(row=1, column=0, padx=pad_x, pady=pad_y, sticky="nsew"); group2.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(group2, text="TEXTURE:", font=self.label_font, text_color=COLOR_TEXT).grid(row=0, column=0, padx=pad_x, pady=label_pad_y, sticky="w")
        texture_combo = ctk.CTkComboBox(group2, variable=self.texture_var, values=get_all_options('textures'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius); texture_combo.grid(row=0, column=1, padx=pad_x, pady=label_pad_y, sticky="ew")
        ctk.CTkLabel(group2, text="COLOR:", font=self.label_font, text_color=COLOR_TEXT).grid(row=1, column=0, padx=pad_x, pady=label_pad_y, sticky="w")
        color_combo = ctk.CTkComboBox(group2, variable=self.color_var, values=get_all_options('colors'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius); color_combo.grid(row=1, column=1, padx=pad_x, pady=label_pad_y, sticky="ew")
        ctk.CTkLabel(group2, text="ADHESIVE:", font=self.label_font, text_color=COLOR_TEXT).grid(row=2, column=0, padx=pad_x, pady=label_pad_y, sticky="w")
        adhesive_combo = ctk.CTkComboBox(group2, variable=self.adhesive_type_var, values=get_all_options('adhesive_types'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius); adhesive_combo.grid(row=2, column=1, padx=pad_x, pady=label_pad_y, sticky="ew")

        # --- Group 3 - Layout Adjustments Implemented ---
        group3 = ctk.CTkFrame(frame, fg_color=COLOR_WIDGET_BG, corner_radius=widget_corner_radius, border_width=2, border_color=COLOR_BORDER_WIDGET)
        group3.grid(row=2, column=0, padx=pad_x, pady=pad_y, sticky="nsew")
        # Give column 0 (labels, segmented button) more weight than column 1 (entry, combobox)
        group3.grid_columnconfigure(0, weight=3)
        group3.grid_columnconfigure(1, weight=2) # Adjusted weight for column 1 as well

        # -- QTY Row --
        ctk.CTkLabel(group3, text="QTY:", font=self.label_font, text_color=COLOR_TEXT).grid(row=0, column=0, padx=pad_x, pady=(label_pad_y*2, 0), sticky="w") # Increased top padding
        # Segmented button takes up most of column 0
        qty_presets = ["50", "100", "250", "500", "1000"]
        qty_segmented_button = ctk.CTkSegmentedButton(group3, values=qty_presets, variable=self.quantity_preset_var, font=self.widget_font, selected_color=COLOR_PINK, selected_hover_color=COLOR_ORANGE, unselected_color=COLOR_ENTRY_BG, unselected_hover_color=COLOR_BG_LIGHT, fg_color=COLOR_ENTRY_BG, border_width=1, corner_radius=widget_corner_radius)
        qty_segmented_button.grid(row=1, column=0, padx=(pad_x, 5), pady=(0, label_pad_y), sticky="ew")
        # Entry field in column 1, slightly reduced width
        qty_entry = ctk.CTkEntry(group3, textvariable=self.quantity_var, font=self.widget_font, width=70, border_color=COLOR_BORDER, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, justify='center', corner_radius=widget_corner_radius)
        qty_entry.grid(row=1, column=1, padx=(0, pad_x), pady=(0, label_pad_y), sticky="w") # Ensure it sticks left in its column

        # -- EXTRAS Row --
        # Label above, spanning both columns
        ctk.CTkLabel(group3, text="EXTRAS:", font=self.label_font, text_color=COLOR_TEXT).grid(row=2, column=0, columnspan=2, padx=pad_x, pady=(label_pad_y*2, 0), sticky="w") # Increased top padding
        # Inner frame below label, spanning both columns
        extras_inner_frame = ctk.CTkFrame(group3, fg_color="transparent")
        extras_inner_frame.grid(row=3, column=0, columnspan=2, padx=pad_x, pady=(0, label_pad_y), sticky="ew")
        # Configure columns inside the inner frame to allow wrapping
        extras_inner_frame.grid_columnconfigure((0, 1, 2), weight=1) # Allow 3 checkboxes per row

        col, row_num = 0, 0
        max_cols = 3 # Max checkboxes per row in the inner frame
        sorted_extras = get_all_options('extras') # Get sorted list to ensure consistent order
        self.extras_vars = {name: self.extras_vars.get(name, ctk.BooleanVar()) for name in sorted_extras} # Ensure vars exist for all possible extras
        for extra_name in sorted_extras:
            var = self.extras_vars[extra_name]
            cb = ctk.CTkCheckBox(extras_inner_frame, text=extra_name, variable=var, font=self.small_font, checkbox_height=18, checkbox_width=18, border_color=COLOR_BORDER, hover_color=COLOR_ORANGE, fg_color=COLOR_PINK, corner_radius=3)
            cb.grid(row=row_num, column=col, padx=3, pady=2, sticky='w') # Reduced padx, added pady
            col += 1
            if col >= max_cols: # Move to next row if max columns reached
                col = 0
                row_num += 1

        # -- DELIVERY Row -- (Now row 4+ effectively, due to extras layout taking row 3)
        # Find the next available row after extras
        delivery_row_start = 4 + row_num # Start DELIVERY label on the row after the last checkbox row
        ctk.CTkLabel(group3, text="DELIVERY:", font=self.label_font, text_color=COLOR_TEXT).grid(row=delivery_row_start, column=0, padx=pad_x, pady=(label_pad_y*2, label_pad_y), sticky="w") # Increased top padding
        delivery_combo = ctk.CTkComboBox(group3, variable=self.delivery_speed_var, values=get_all_options('delivery_speeds'), font=self.widget_font, state="readonly", border_color=COLOR_BORDER, button_color=COLOR_PURPLE, button_hover_color=COLOR_PINK, dropdown_fg_color=COLOR_ENTRY_BG, fg_color=COLOR_ENTRY_BG, text_color=COLOR_TEXT_NEON, corner_radius=widget_corner_radius)
        delivery_combo.grid(row=delivery_row_start, column=1, padx=(0, pad_x), pady=(label_pad_y*2, label_pad_y), sticky="ew") # Use ew sticky


        # --- ADDED Switch/Info Frame at the bottom (Unchanged Placement relative to main frame) ---
        misc_frame = ctk.CTkFrame(frame, fg_color=COLOR_WIDGET_BG, corner_radius=5, border_width=1, border_color=COLOR_ORANGE)
        # Ensure this frame is placed relative to the outer 'frame', not 'group3'
        misc_frame.grid(row=3, column=0, padx=pad_x, pady=(pad_y * 2, pad_y), sticky="sew") # Place in outer frame's row 3
        misc_frame.grid_columnconfigure(0, weight=1) # Configure columns inside misc_frame
        misc_frame.grid_columnconfigure(1, weight=1)

        appearance_switch = ctk.CTkSwitch(misc_frame, text="Light Mode?", variable=self.appearance_mode_var, onvalue="light", offvalue="dark", command=self._toggle_appearance_mode, font=self.small_font, progress_color=COLOR_LIME, fg_color=COLOR_PURPLE, button_color=COLOR_PINK, button_hover_color=COLOR_ORANGE)
        appearance_switch.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        info_button = ctk.CTkButton(misc_frame, text="INFO", font=self.small_font, width=70, command=self._show_help_info, fg_color=COLOR_ENTRY_BG, border_width=1, border_color=COLOR_TEAL, hover_color=COLOR_BG_LIGHT, text_color=COLOR_TEAL, corner_radius=5)
        info_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")


    def _create_go_button_area(self):
        # --- Unchanged ---
        go_x, go_y, go_w, go_h = 0.02, 0.87, 0.96, 0.11
        cx, cy = APP_WIDTH * 0.5, APP_HEIGHT * (go_y + go_h / 2)
        radius = min(APP_WIDTH * go_w * 0.2, APP_HEIGHT * go_h * 0.8) * 0.5
        go_button = ctk.CTkButton(self, text="LAUNCH!", font=self.button_font, command=self._calculate_cheapest,
                                   fg_color=COLOR_TEAL, hover_color=COLOR_PINK, text_color=COLOR_BUTTON_TEXT,
                                   border_width=4, border_color=COLOR_LIME,
                                   corner_radius=100,
                                   width=radius * 1.6, height=radius * 1.6)
        go_button.place(x=cx, y=cy, anchor="center")

    def _create_results_area(self):
        # --- Unchanged ---
        res_x, res_y, res_w, res_h = 0.34, 0.10, 0.64, 0.75
        self.results_display_frame = ctk.CTkFrame(self, fg_color=COLOR_FRAME_BG, border_width=0)
        self.results_display_frame.place(relx=res_x + 0.01, rely=res_y + 0.01, relwidth=res_w - 0.02, relheight=res_h - 0.02, anchor="nw")
        self.results_display_frame.grid_rowconfigure(0, weight=0)
        self.results_display_frame.grid_rowconfigure(1, weight=0)
        self.results_display_frame.grid_rowconfigure(2, weight=1)
        self.results_display_frame.grid_columnconfigure(0, weight=1)
        disclaimer_label = ctk.CTkLabel(self.results_display_frame,
                                         text="Base estimates ONLY. Ship/Tax/Duty are ROUGH FIXED GUESSES for Vancouver, BC. NOT LIVE/ACCURATE. CHECK VENDOR SITE!",
                                         font=self.small_font, text_color=COLOR_ORANGE, wraplength=APP_WIDTH*res_w*0.95,
                                         fg_color=COLOR_BG_LIGHT, corner_radius=5, justify="center", pady=4)
        disclaimer_label.grid(row=0, column=0, padx=10, pady=(5, 3), sticky="ew")
        header_frame = ctk.CTkFrame(self.results_display_frame, fg_color=COLOR_BG_LIGHT, corner_radius=5)
        header_frame.grid(row=1, column=0, padx=10, pady=(3, 3), sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1, minsize=30)
        header_frame.grid_columnconfigure(1, weight=10)
        header_frame.grid_columnconfigure(2, weight=3, minsize=90)
        header_frame.grid_columnconfigure(3, weight=3, minsize=80)
        header_frame.grid_columnconfigure(4, weight=3, minsize=90)
        header_frame.grid_columnconfigure(5, weight=4, minsize=100)
        header_frame.grid_columnconfigure(6, weight=3, minsize=90)
        ctk.CTkLabel(header_frame, text="#", font=self.small_font, text_color=COLOR_TEXT_DIM).grid(row=0, column=0, padx=(5,0), pady=3, sticky="e")
        ctk.CTkLabel(header_frame, text="Vendor // Notes", font=self.small_font, text_color=COLOR_TEXT_DIM).grid(row=0, column=1, padx=5, pady=3, sticky="w")
        ctk.CTkLabel(header_frame, text="Base", font=self.small_font, text_color=COLOR_TEXT_DIM).grid(row=0, column=2, padx=5, pady=3, sticky="e")
        ctk.CTkLabel(header_frame, text="Ship", font=self.small_font, text_color=COLOR_TEXT_DIM).grid(row=0, column=3, padx=5, pady=3, sticky="e")
        ctk.CTkLabel(header_frame, text="Tax/Duty", font=self.small_font, text_color=COLOR_TEXT_DIM).grid(row=0, column=4, padx=5, pady=3, sticky="e")
        ctk.CTkLabel(header_frame, text="TOTAL", font=self.small_font, text_color=COLOR_LIME).grid(row=0, column=5, padx=5, pady=3, sticky="e")
        ctk.CTkLabel(header_frame, text="Per Unit", font=self.small_font, text_color=COLOR_TEXT_DIM).grid(row=0, column=6, padx=(5,10), pady=3, sticky="e")
        self.results_list_frame = ctk.CTkScrollableFrame(self.results_display_frame, fg_color="transparent", label_text="", border_width=0)
        self.results_list_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.results_list_frame.grid_columnconfigure(0, weight=1)


    # --- Results Display - Includes Clickable Links ---
    def _update_results_display(self):
        """Populates the results list frame with clickable vendor links"""
        for widget in self.results_list_frame.winfo_children():
            widget.grid_forget()
            widget.destroy()

        if not self.result_data:
            ctk.CTkLabel(self.results_list_frame, text="< Hit LAUNCH! to get score feed >", font=self.widget_font, text_color=COLOR_TEXT_DIM).pack(pady=50, padx=20)
            return

        rank = 1
        col_configs = {
            0: {"weight": 1, "minsize": 30},
            1: {"weight": 10, "minsize": 150},
            2: {"weight": 3, "minsize": 90},
            3: {"weight": 3, "minsize": 80},
            4: {"weight": 3, "minsize": 90},
            5: {"weight": 4, "minsize": 100},
            6: {"weight": 3, "minsize": 90}
        }

        for vendor, base_price, ship_est, tax_est, duty_est, total_est, pps_total, notes in self.result_data[:20]:
            result_row = ctk.CTkFrame(self.results_list_frame, fg_color="transparent")
            result_row.grid(row=rank - 1, column=0, pady=(0, 8), padx=2, sticky="ew")
            self.results_list_frame.grid_rowconfigure(rank - 1, weight=0)

            for col, config in col_configs.items():
                 result_row.grid_columnconfigure(col, weight=config["weight"], minsize=config["minsize"])

            # --- Row 0: Rank, Vendor (Clickable), Prices ---
            rank_color = COLOR_LIME if rank == 1 else (COLOR_PINK if rank == 2 else (COLOR_ORANGE if rank == 3 else COLOR_TEAL))
            rank_label = ctk.CTkLabel(result_row, text=f"{rank}>", font=self.result_font, text_color=rank_color, width=col_configs[0]["minsize"], anchor="e")
            rank_label.grid(row=0, column=0, padx=(0, 5), pady=(1,0), sticky="ne")

            # --- Vendor Label as Clickable Link ---
            vendor_url = websites_data.get(vendor, {}).get("url", None) # Get URL safely
            vendor_label = ctk.CTkLabel(result_row, text=vendor, font=self.widget_font, text_color=COLOR_LINK, anchor="w") # Use Link Color
            vendor_label.grid(row=0, column=1, padx=5, pady=(1,0), sticky="nw")

            if vendor_url: # Only make it clickable if URL exists
                vendor_label.bind("<Enter>", lambda e, label=vendor_label: label.configure(cursor="hand2")) # Change cursor on hover
                vendor_label.bind("<Leave>", lambda e, label=vendor_label: label.configure(cursor=""))     # Change cursor back
                # Use lambda to pass the specific URL to the handler
                vendor_label.bind("<Button-1>", lambda event, url=vendor_url: self._open_url(url))
            else:
                # Optional: Style differently if no URL is found (e.g., default text color)
                vendor_label.configure(text_color=COLOR_TEXT) # Use default text color if no link

            # --- Other price labels (Unchanged) ---
            base_price_text = f"${base_price:.2f}"
            base_price_label = ctk.CTkLabel(result_row, text=base_price_text, font=self.small_font, text_color=COLOR_TEXT_DIM, anchor="e")
            base_price_label.grid(row=0, column=2, padx=5, pady=(1,0), sticky="ne")

            ship_text = f"${ship_est:.2f}"
            ship_label = ctk.CTkLabel(result_row, text=ship_text, font=self.small_font, text_color=COLOR_TEXT_DIM, anchor="e")
            ship_label.grid(row=0, column=3, padx=5, pady=(1,0), sticky="ne")

            tax_duty_est = tax_est + duty_est
            tax_duty_text = f"${tax_duty_est:.2f}"
            tax_duty_label = ctk.CTkLabel(result_row, text=tax_duty_text, font=self.small_font, text_color=COLOR_TEXT_DIM, anchor="e")
            tax_duty_label.grid(row=0, column=4, padx=5, pady=(1,0), sticky="ne")

            total_text = f"~${total_est:.2f}"
            total_label = ctk.CTkLabel(result_row, text=total_text, font=self.result_font, text_color=rank_color, anchor="e")
            total_label.grid(row=0, column=5, padx=5, pady=(1,0), sticky="ne")

            pps_text = f"${pps_total:.3f}/ea"
            pps_label = ctk.CTkLabel(result_row, text=pps_text, font=self.small_font, text_color=COLOR_TEXT_DIM, anchor="e")
            pps_label.grid(row=0, column=6, padx=(5, 10), pady=(1,0), sticky="ne")

            # --- Row 1: Notes (Unchanged) ---
            if notes:
                notes_wrap = max(150, int(col_configs[1]['minsize'] * 0.9))
                note_label = ctk.CTkLabel(result_row, text=f"// {notes}", font=self.small_font, text_color=COLOR_TEXT_DIM, anchor="nw", justify="left", wraplength=notes_wrap)
                note_label.grid(row=1, column=1, padx=5, pady=(0,2), sticky="nw")

            rank += 1


    # --- Utility Methods ---
    def _update_quantity_from_preset(self, *args):
        # --- Unchanged ---
        preset_value = self.quantity_preset_var.get();
        if preset_value: self.quantity_var.set(preset_value)

    def _toggle_appearance_mode(self):
        # --- Unchanged ---
        new_mode = self.appearance_mode_var.get(); ctk.set_appearance_mode(new_mode)

    # --- NEW Method to Open URL ---
    def _open_url(self, url: Optional[str]):
        """Opens the given URL in the default web browser."""
        if url:
            try:
                print(f"Opening URL: {url}") # Optional: Log which URL is being opened
                webbrowser.open_new_tab(url)
            except Exception as e:
                print(f"Error opening URL {url}: {e}")
                # Optionally show an error popup to the user
                error_win = ctk.CTkToplevel(self); error_win.geometry("300x100"); error_win.title("!! LINK ERROR !!");
                ctk.CTkLabel(error_win, text=f"Cannot open link:\n{url}", text_color=COLOR_ORANGE, wraplength=280, font=self.small_font).pack(pady=10, padx=10);
                ctk.CTkButton(error_win, text="<// ACKNOWLEDGED //>", command=error_win.destroy, fg_color=COLOR_PINK, text_color=COLOR_BUTTON_TEXT, corner_radius=5).pack(pady=5);
                error_win.transient(self); error_win.grab_set();

    # --- Help Info (Updated) ---
    def _show_help_info(self):
        help_win = ctk.CTkToplevel(self); help_win.geometry("600x550"); help_win.title("callyourmumslaps - INFO")
        help_win.configure(fg_color=COLOR_BG_LIGHT); help_win.transient(self); help_win.grab_set()
        help_text = """**⚡ callyourmumslaps ⚡**
>> 
>>     price estimates for custom slappedy slap slaps! 
>> 
>>      Matthew Goodacre is the best brother in the whole world. <3 
>> 
>> - **BASE PRICES ARE ESTIMATES ONLY!** Not live quotes. Data snapshot ~Mar 2025.
>> - **SHIPPING / TAX / DUTY ARE *FIXED PLACEHOLDERS* FOR VANCOUVER, BC!**
>>     - Real costs WILL vary significantly. International orders especially involve complex, often unpredictable duties/brokerage.
>>   ALWAYS check the vendor's website directly using their checkout process for the final, accurate quote including ALL costs for YOUR order and location!**
>>
>> **>>> USER DIRECTIVE <<<**
>> - Dial in sticker specs (size, shape, etc) in CONFIG DECK.
>> - Set quantity via presets or direct input.
>> - Hit LAUNCH! to get the SCORE FEED (lowest *estimated total* first). (All vendors included automatically).
>> - Results show: Est. Base Price | Est. Ship | Est. Tax/Duty | Est. TOTAL | Est. Price Per Unit (based on total).
>> - 'Light Mode?' switch provided.
>>
>>
>> **Tag:** FAKR FAKR 'Til The End!
"""
        textbox = ctk.CTkTextbox(help_win, wrap="word", font=self.widget_font, fg_color=COLOR_WIDGET_BG, text_color=COLOR_TEXT, border_width=2, border_color=COLOR_PURPLE, corner_radius=5)
        textbox.pack(expand=True, fill="both", padx=20, pady=15)
        textbox.insert("0.0", help_text); textbox.configure(state="disabled")
        close_button = ctk.CTkButton(help_win, text="<// I Read The Fine Print //>", command=help_win.destroy, fg_color=COLOR_PINK, hover_color=COLOR_ORANGE, text_color=COLOR_BUTTON_TEXT, font=self.widget_font, corner_radius=5)
        close_button.pack(pady=(0, 15))


    # --- Price Calculation Methods (Unchanged) ---
    def _calculate_base_price(self, website: str, size: str, qty: int, texture: str, shape: str, color: str, delivery: str, selected_extras: Dict[str, bool], material: str, adhesive: str) -> float:
        if website not in websites_data: return float('inf')
        data = websites_data[website];
        if size not in data["sizes"]: return float('inf')
        if not data["sizes"][size]: return float('inf')
        if material not in data.get("materials", {}): return float('inf')
        possible_quantities = sorted(data["quantities"]); base_qty = qty
        if qty not in data["sizes"][size]:
            found_tier = False
            for q_tier in possible_quantities:
                if q_tier >= qty:
                    if q_tier in data["sizes"][size]: base_qty = q_tier; found_tier = True; break
            if not found_tier:
                suitable_lower_tiers = [q for q in possible_quantities if q <= qty and q in data["sizes"][size]]
                if not suitable_lower_tiers: return float('inf')
                base_qty = max(suitable_lower_tiers)
        base_price_at_tier = data["sizes"][size].get(base_qty, float('inf'))
        if base_price_at_tier == float('inf'): return float('inf')
        price_per_sticker_at_base = base_price_at_tier / base_qty;
        price = price_per_sticker_at_base * qty
        price *= data.get("textures", {}).get(texture, 1.0)
        price *= data.get("shapes", {}).get(shape, 1.0)
        price *= data.get("colors", {}).get(color, 1.0)
        price *= data.get("delivery_speeds", {}).get(delivery, 1.0)
        price *= data.get("materials", {}).get(material, 1.0)
        price *= data.get("adhesive_types", {}).get(adhesive, 1.0)
        for extra, is_selected in selected_extras.items():
            # Only apply multiplier if the extra is selected AND offered by the vendor
             if is_selected and extra in data.get("extras", {}):
                 price *= data.get("extras", {}).get(extra, 1.0) # Default to 1.0 just in case, though it should exist
        applicable_discount_tier = 0
        for tier_qty in sorted(data.get("discounts", {}).keys()):
             if qty >= tier_qty: applicable_discount_tier = tier_qty
             else: break
        discount_multiplier = data.get("discounts", {}).get(applicable_discount_tier, 1.0)
        price *= discount_multiplier
        return price

    def _calculate_final_details(self, website: str, base_price: float) -> Tuple[float, float, float, float]:
        # --- Unchanged ---
        if website not in websites_data or base_price == float('inf'):
            return (0.0, 0.0, 0.0, base_price)
        data = websites_data[website]
        ship_est = data.get("shipping_est_bc", 0.0)
        tax_rate = data.get("tax_rate_bc", 0.0)
        duty_handling_est = data.get("duty_handling_est", 0.0)
        tax_est = base_price * tax_rate
        total_est = base_price + ship_est + tax_est + duty_handling_est
        return (ship_est, tax_est, duty_handling_est, total_est)


    # --- Main Calculation Trigger (Unchanged) ---
    def _calculate_cheapest(self):
        try:
            qty_str = self.quantity_var.get()
            if not qty_str.isdigit() or int(qty_str) <= 0:
                error_win = ctk.CTkToplevel(self); error_win.geometry("350x120"); error_win.title("!! INPUT ERROR !!");
                ctk.CTkLabel(error_win, text="SYSTEM SHOCK! Quantity must be a positive whole number, data slug!", text_color=COLOR_ORANGE, wraplength=330, font=self.widget_font).pack(pady=10, padx=10);
                ctk.CTkButton(error_win, text="<// REBOOT INPUT //>", command=error_win.destroy, fg_color=COLOR_PINK, text_color=COLOR_BUTTON_TEXT, corner_radius=5).pack(pady=5);
                error_win.transient(self); error_win.grab_set(); return
            qty = int(qty_str)
        except ValueError:
            error_win = ctk.CTkToplevel(self); error_win.geometry("300x100"); error_win.title("!! INPUT ERROR !!");
            ctk.CTkLabel(error_win, text="CORRUPTED QTY DATA!", text_color=COLOR_ORANGE, wraplength=280, font=self.widget_font).pack(pady=10, padx=10);
            ctk.CTkButton(error_win, text="<// OVERRIDE //>", command=error_win.destroy, fg_color=COLOR_PINK, text_color=COLOR_BUTTON_TEXT, corner_radius=5).pack(pady=5);
            error_win.transient(self); error_win.grab_set(); return

        current_size=self.size_var.get(); current_texture=self.texture_var.get(); current_shape=self.shape_var.get(); current_color=self.color_var.get(); current_delivery=self.delivery_speed_var.get(); current_material=self.material_var.get(); current_adhesive=self.adhesive_type_var.get();
        # Ensure current_extras only contains extras that are actually available options
        available_extras = get_all_options('extras')
        current_extras={extra: var.get() for extra, var in self.extras_vars.items() if extra in available_extras}


        results_list: List[Tuple[str, float, float, float, float, float, float, str]] = []
        for website in websites_data.keys():
            base_price = self._calculate_base_price(website, current_size, qty, current_texture, current_shape, current_color, current_delivery, current_extras, current_material, current_adhesive)
            if base_price != float('inf') and base_price > 0:
                ship_est, tax_est, duty_est, total_est = self._calculate_final_details(website, base_price)
                pps_total = total_est / qty if qty > 0 else 0
                notes = websites_data[website].get("notes", "")
                results_list.append((website, base_price, ship_est, tax_est, duty_est, total_est, pps_total, notes))

        self.result_data = sorted(results_list, key=lambda item: item[5])
        self._update_results_display()

        print("\n--- Calculation Sequence Complete (w/ ILLUSTRATIVE Ship/Tax Est. for Vancouver, BC) ---")
        if self.result_data:
             print(f"Top Score Feed (Est. Total): {self.result_data[0][0]} ~CAD ${self.result_data[0][5]:.2f} "
                   f"(Base: ${self.result_data[0][1]:.2f}, Ship: ${self.result_data[0][2]:.2f}, Tax: ${self.result_data[0][3]:.2f}, Duty/H: ${self.result_data[0][4]:.2f})")
        else: print("Output Buffer Empty: No valid results found.")
        print("*** WARNING: Ship/Tax/Duty are ROUGH FIXED ESTIMATES for Vancouver, BC ONLY - NOT LIVE/ACCURATE ***")
        print("----------------------------------------------------------------------------------------\n")


# --- Run ---
if __name__ == "__main__":
    app = StickerApp()
    app.mainloop()