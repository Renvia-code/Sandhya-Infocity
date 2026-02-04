#!/usr/bin/env python3
"""
QR Code Generator for Back Gate Guide
Run this after setting up your GitHub Pages to generate a QR code with your actual URL.

Usage:
    pip install qrcode[pil] pillow
    python generate_qr.py
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image, ImageDraw, ImageFont

# ========================================
# 🔧 CUSTOM DOMAIN
# ========================================
DOMAIN = "sandhyainfocity.support"
# ========================================

def generate_qr():
    url = f"https://{DOMAIN}/?src=qr"
    
    print(f"🔗 Generating QR code for: {url}")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create styled QR code
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        fill_color="#1e3a8a",
        back_color="white"
    )
    img = img.convert('RGBA')

    # Create canvas
    canvas_width = img.width + 100
    canvas_height = img.height + 200
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))
    
    draw = ImageDraw.Draw(canvas)
    
    # Paste QR code
    qr_x = (canvas_width - img.width) // 2
    qr_y = 50
    canvas.paste(img, (qr_x, qr_y), img)

    # Add text (using default font for compatibility)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        try:
            # Try Windows fonts
            title_font = ImageFont.truetype("arial.ttf", 28)
            subtitle_font = ImageFont.truetype("arial.ttf", 16)
            small_font = ImageFont.truetype("arial.ttf", 12)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

    # Title
    title = "SCAN FOR DIRECTIONS"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_x = (canvas_width - (title_bbox[2] - title_bbox[0])) // 2
    draw.text((title_x, img.height + 70), title, fill=(30, 58, 138), font=title_font)

    # Subtitle
    subtitle = "Back Gate & Pedestrian Guide"
    sub_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sub_x = (canvas_width - (sub_bbox[2] - sub_bbox[0])) // 2
    draw.text((sub_x, img.height + 108), subtitle, fill=(100, 116, 139), font=subtitle_font)

    # Footer
    footer = "Sandhya Infocity • Facility Management"
    foot_bbox = draw.textbbox((0, 0), footer, font=small_font)
    foot_x = (canvas_width - (foot_bbox[2] - foot_bbox[0])) // 2
    draw.text((foot_x, img.height + 145), footer, fill=(148, 163, 184), font=small_font)

    # Line
    draw.line([(50, img.height + 135), (canvas_width - 50, img.height + 135)], fill=(226, 232, 240), width=1)

    # Save
    output_file = "backgate-qr-code.png"
    canvas.save(output_file, 'PNG', dpi=(300, 300))
    
    print(f"✅ QR code saved as: {output_file}")
    print(f"📱 Test by scanning with your phone!")

if __name__ == "__main__":
    generate_qr()
