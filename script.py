import requests
import os
from pathlib import Path

DIRETORIO_DOWNLOAD = Path().resolve() / "imagens"

def download_images(file_path):
    # Create the output directory if it doesn't exist
    if not os.path.exists(DIRETORIO_DOWNLOAD):
        os.makedirs(DIRETORIO_DOWNLOAD)

    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    for index, url in enumerate(urls, start=1):
        try:
            # Get the file extension from the URL (default to .jpg if not found)
            ext = os.path.splitext(url)[1]
            if not ext or len(ext) > 5:
                ext = ".jpg"
            
            # Define the new filename
            # filename = f"{index}_{url.split('/')[-1]}"
            filename = f"{index}"
            if not filename.endswith(ext):
                filename += ext
                
            save_path = DIRETORIO_DOWNLOAD / filename

            # Download the image
            print(f"Downloading {index}/{len(urls)}: {url}")
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Saved to: {save_path}")

        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    # Ensure 'urls.txt' exists in the same directory
    download_images("urls.txt")