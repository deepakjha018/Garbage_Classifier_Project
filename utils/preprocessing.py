import os
from PIL import Image
import shutil

# Constants
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
IMG_SIZE = (128, 128)

def preprocess_images():
    if os.path.exists(PROCESSED_DIR):
        shutil.rmtree(PROCESSED_DIR)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    for category in os.listdir(RAW_DIR):
        input_folder = os.path.join(RAW_DIR, category)

        # ✅ Skip files
        if not os.path.isdir(input_folder):
            continue

        output_folder = os.path.join(PROCESSED_DIR, category)
        os.makedirs(output_folder, exist_ok=True)

        for file in os.listdir(input_folder):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            try:
                print(f"📂 Processing: {input_path} → {output_path}")  # 🔍 Debug line
                img = Image.open(input_path).convert("RGB")
                img = img.resize(IMG_SIZE)
                img.save(output_path)
            except Exception as e:
                print(f"❌ Failed to process {input_path}: {e}")

    print(f"\n✅ Preprocessing complete. Processed images saved in '{PROCESSED_DIR}'")


if __name__ == "__main__":
    preprocess_images()
