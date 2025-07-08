from PIL import Image
import random

def encrypt_image(image_path, key=50, output_path="encrypted.png", swap_file="swaps.txt"):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    # Step 1: Apply key to each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    # Step 2: Record swaps
    swaps = []
    for _ in range(1000):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
        swaps.append((x1, y1, x2, y2))

    # Save swaps to a file
    with open(swap_file, 'w') as f:
        for s in swaps:
            f.write(f"{s[0]},{s[1]},{s[2]},{s[3]}\n")

    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")
    print(f"Swaps saved to {swap_file}")


def decrypt_image(image_path, key=50, output_path="decrypted.png", swap_file="swaps.txt"):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    # Step 1: Reverse key from each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    # Step 2: Load and reverse the swaps
    with open(swap_file, 'r') as f:
        swaps = [line.strip().split(',') for line in f.readlines()]
        swaps = [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in swaps]

    # Reverse the swaps in reverse order
    for x1, y1, x2, y2 in reversed(swaps):
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    encrypt_image("images/images.jpg", key=50, output_path="encrypted.png", swap_file="swaps.txt")
    decrypt_image("encrypted.png", key=50, output_path="decrypted.png", swap_file="swaps.txt")
