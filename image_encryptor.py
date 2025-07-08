from PIL import Image
import random

def encrypt_image(image_path, key=50, output_path="encrypted.png"):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    # Apply a mathematical operation to each pixel (e.g., add a key)
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    # Swap random pixel values (as a simple obfuscation)
    for _ in range(1000):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")


def decrypt_image(image_path, key=50, output_path="decrypted.png"):
    # This decryption assumes the pixel swap step is skipped for simplicity.
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    # Reverse the mathematical operation
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print(f"Decrypted image saved as {output_path}")


if __name__ == "__main__":
    encrypt_image("images/images.jpg", key=50, output_path="encrypted.png")
    decrypt_image("encrypted.png", key=50, output_path="decrypted.png")

