from PIL import Image, ImageDraw
import os

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

# HIGH CONTRAST gradients for ALL 25 categories (Danish names)
category_colors = {
    'Motivation': [(138, 43, 226), (75, 0, 130), (255, 20, 147), (147, 112, 219)],  # Purple → Pink
    'Kærlighed': [(255, 0, 100), (139, 0, 0), (255, 105, 180), (255, 192, 203)],  # Red → Pink
    'Succes': [(255, 215, 0), (0, 100, 0), (255, 140, 0), (34, 139, 34)],  # Gold → Green
    'Visdom': [(0, 0, 139), (255, 215, 0), (70, 130, 180), (255, 255, 0)],  # Blue → Yellow
    'Lykke': [(255, 255, 0), (255, 0, 255), (255, 165, 0), (147, 112, 219)],  # Yellow → Purple
    'Selvudvikling': [(0, 128, 0), (255, 215, 0), (0, 255, 0), (255, 140, 0)],  # Green → Gold
    'Taknemmelighed': [(255, 127, 80), (75, 0, 130), (255, 160, 122), (138, 43, 226)],  # Coral → Purple
    'Venskab': [(255, 192, 203), (0, 100, 80), (255, 105, 180), (0, 200, 160)],  # Pink → Teal
    'Håb': [(0, 0, 100), (255, 255, 0), (70, 130, 180), (255, 215, 0)],  # Blue → Yellow
    'Kreativitet': [(255, 0, 127), (0, 0, 139), (255, 20, 147), (75, 0, 130)],  # Pink → Blue
    'Indre Ro': [(135, 206, 235), (0, 0, 100), (176, 224, 230), (75, 0, 130)],  # Blue → Purple
    'Selvtillid': [(255, 69, 0), (0, 0, 139), (255, 140, 0), (70, 130, 180)],  # Orange → Blue
    'Udholdenhed': [(139, 69, 19), (255, 215, 0), (160, 82, 45), (255, 140, 0)],  # Brown → Gold
    'Inspiration': [(255, 0, 255), (75, 0, 130), (255, 20, 147), (0, 0, 139)],  # Magenta → Blue
    'Positivt Liv': [(50, 205, 50), (255, 0, 127), (144, 238, 144), (255, 20, 147)],  # Green → Pink
    'Mod': [(178, 34, 34), (255, 215, 0), (220, 20, 60), (255, 140, 0)],  # Red → Gold
    'Venlighed': [(255, 182, 193), (138, 43, 226), (255, 160, 122), (75, 0, 130)],  # Pink → Purple
    'Tålmodighed': [(34, 139, 34), (255, 255, 0), (60, 179, 113), (255, 215, 0)],  # Green → Yellow
    'Tilgivelse': [(230, 230, 250), (75, 0, 130), (216, 191, 216), (138, 43, 226)],  # Lavender → Purple
    'Styrke': [(100, 100, 100), (255, 69, 0), (150, 150, 150), (255, 140, 0)],  # Gray → Orange
    'Glæde': [(255, 255, 0), (255, 0, 127), (255, 215, 0), (147, 112, 219)],  # Yellow → Purple
    'Balance': [(60, 179, 113), (138, 43, 226), (152, 251, 152), (75, 0, 130)],  # Green → Purple
    'Vækst': [(0, 100, 0), (255, 215, 0), (34, 139, 34), (255, 140, 0)],  # Green → Gold
    'Formål': [(75, 0, 130), (255, 215, 0), (138, 43, 226), (255, 140, 0)],  # Purple → Gold
    'Achtsomhed': [(210, 180, 140), (75, 0, 130), (245, 245, 220), (138, 43, 226)],  # Tan → Purple
}

all_categories = [
    'Motivation', 'Kærlighed', 'Succes', 'Visdom', 'Lykke',
    'Selvudvikling', 'Taknemmelighed', 'Venskab', 'Håb', 'Kreativitet',
    'Indre Ro', 'Selvtillid', 'Udholdenhed', 'Inspiration', 'Positivt Liv',
    'Mod', 'Venlighed', 'Tålmodighed', 'Tilgivelse', 'Styrke',
    'Glæde', 'Balance', 'Vækst', 'Formål', 'Achtsomhed'
]

os.makedirs('output/backgrounds', exist_ok=True)

for category in all_categories:
    colors = category_colors.get(category, [(15, 10, 40), (48, 43, 99), (36, 36, 62), (72, 61, 139)])

    img = Image.new('RGB', (VIDEO_WIDTH, VIDEO_HEIGHT))
    draw = ImageDraw.Draw(img)

    # Create gradient
    for y in range(VIDEO_HEIGHT):
        ratio = y / VIDEO_HEIGHT
        if ratio < 0.33:
            r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * (ratio * 3))
            g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * (ratio * 3))
            b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * (ratio * 3))
        elif ratio < 0.66:
            r = int(colors[1][0] + (colors[2][0] - colors[1][0]) * ((ratio - 0.33) * 3))
            g = int(colors[1][1] + (colors[2][1] - colors[1][1]) * ((ratio - 0.33) * 3))
            b = int(colors[1][2] + (colors[2][2] - colors[1][2]) * ((ratio - 0.33) * 3))
        else:
            r = int(colors[2][0] + (colors[3][0] - colors[2][0]) * ((ratio - 0.66) * 3))
            g = int(colors[2][1] + (colors[3][1] - colors[2][1]) * ((ratio - 0.66) * 3))
            b = int(colors[2][2] + (colors[3][2] - colors[2][2]) * ((ratio - 0.66) * 3))
        draw.rectangle([(0, y), (VIDEO_WIDTH, y + 1)], fill=(r, g, b))

    # Add geometric pattern (circles)
    for i in range(0, VIDEO_WIDTH, 120):
        for j in range(0, VIDEO_HEIGHT, 120):
            draw.ellipse(
                [(i + 30, j + 30), (i + 90, j + 90)],
                outline=(255, 255, 255, 20),
                width=1
            )

    # Add radial glow
    glow = Image.new('RGBA', (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for radius in range(800, 0, -50):
        alpha = int(30 * (1 - radius / 800))
        glow_draw.ellipse(
            [(VIDEO_WIDTH//2 - radius, VIDEO_HEIGHT//3 - radius),
             (VIDEO_WIDTH//2 + radius, VIDEO_HEIGHT//3 + radius)],
            fill=(255, 255, 255, alpha)
        )

    img = img.convert('RGBA')
    img = Image.alpha_composite(img, glow)
    img = img.convert('RGB')

    output_path = f'output/backgrounds/{category.replace(" ", "_")}.jpg'
    img.save(output_path, quality=95)
    print(f'Generated: {category}')

print('\nAll 25 background samples generated in output/backgrounds/ folder!')
print('Velocity Danish - Background Generator')
