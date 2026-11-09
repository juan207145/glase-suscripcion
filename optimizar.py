from PIL import Image
import os

ajustes = {"Barcelona_Champions.jpg": 1600, "Barcelona_Logo.jpg": 300}

for nombre, ancho in ajustes.items():
    if not os.path.exists(nombre):
        print(f"No encontré {nombre}")
        continue
    antes = os.path.getsize(nombre) / 1024
    img = Image.open(nombre).convert("RGB")
    if img.width > ancho:
        img = img.resize((ancho, round(img.height * ancho / img.width)), Image.LANCZOS)
    img.save(nombre, "JPEG", quality=72, optimize=True, progressive=True)
    print(f"{nombre}: {antes:.0f} KB -> {os.path.getsize(nombre)/1024:.0f} KB")
