import json
import os
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image

# Initialize Gemini Client (automatically reads GEMINI_API_KEY env var)
client = genai.Client()

def generate_alt_text_for_folder(
    pdf_guide_path: str,
    images_dir: str,
    user_prompt: str,
    output_file: str = "alt_texts.json",
    model_name: str = "gemini-2.5-flash"
):
    """
    AI Agent that reads a PDF style guide, iterates through local images,
    and generates compliant Alt Text using Google Gemini.
    """
    pdf_path = Path(pdf_guide_path)
    images_path = Path(images_dir)

    # Validation
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF style guide not found at: {pdf_path}")
    if not images_path.exists():
        raise FileNotFoundError(f"Images directory not found at: {images_path}")

    print(f"📄 Uploading style guide PDF to Gemini Files API: {pdf_path.name}...")
    # Upload PDF once so Gemini can reference it across requests
    pdf_file_ref = client.files.upload(file=str(pdf_path))
    print(f"✅ Style guide uploaded successfully.\n")

    # Find valid image files
    valid_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    image_files = [f for f in images_path.iterdir() if f.suffix.lower() in valid_extensions]

    if not image_files:
        print("⚠️ No valid image files found in the directory.")
        return

    print(f"🖼️ Found {len(image_files)} image(s) to process.\n")
    results = {}

    for idx, img_file in enumerate(image_files, 1):
        print(f"[{idx}/{len(image_files)}] Processing: {img_file.name}...")

        try:
            # Load the image using PIL
            img = Image.open(img_file)

            # System/Instruction prompt
            system_instruction = f"""
            You are an expert digital accessibility agent.
            Generate concise, clear, and descriptive Alt Text for the attached image.

            USER SPECIFIC CONTEXT / REQUEST:
            {user_prompt}

            COMPLIANCE GUIDELINES:
            You must follow all rules, formatting recommendations, and tone guidelines 
            described in the attached PDF style guide document.

            OUTPUT FORMAT:
            Provide ONLY the final alt text string. Do not wrap in quotes or add conversational filler.
            """

            # Call Gemini with PDF reference, Image object, and Prompt instructions
            response = client.models.generate_content(
                model=model_name,
                contents=[
                    pdf_file_ref,
                    img,
                    system_instruction
                ]
            )

            alt_text = response.text.strip()
            results[img_file.name] = alt_text
            print(f"   ↳ Alt Text: \"{alt_text}\"\n")

        except Exception as e:
            print(f"   ❌ Error processing {img_file.name}: {e}\n")
            results[img_file.name] = f"Error: {str(e)}"

    # Export results to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"🎉 Process completed! Output written to '{output_file}'.")

    # Clean up uploaded PDF from Gemini cloud storage
    try:
        client.files.delete(name=pdf_file_ref.name)
        print("🧹 Cleaned up temporary PDF file from Gemini API.")
    except Exception as e:
        print(f"Notice: Could not delete remote file: {e}")


if __name__ == "__main__":
    # Context & instructions for the agent
    CUSTOM_PROMPT = (
        "Focus on details relevant for e-commerce web accessibility. "
        "Highlight key visual features, materials, and actions, but keep descriptions "
        "under 125 characters unless the image contains detailed diagrammatic text."
    )

    generate_alt_text_for_folder(
        pdf_guide_path="accessibility_guide.pdf",
        images_dir="./input_images",
        user_prompt=CUSTOM_PROMPT,
        output_file="image_alt_texts.json"
    )