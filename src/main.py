import io
import ollama
from utils import load_thumbnails_from_folder

folder_path = "test_images"

images = load_thumbnails_from_folder(folder_path)

keyword = "flowers"

for image in images:
    # convert the Pillow images into bytes
    img_byte_arr = io.BytesIO()
    images[image].save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()

    response = {"message": {"content": ""}}

    # ask until the model respond with either a 1 or 0
    while (
        response["message"]["content"].find("1") == -1
        and response["message"]["content"].find("0") == -1
    ):
        response = ollama.chat(
            model="llava:7b",
            messages=[
                {
                    "role": "user",
                    "content": f"Does this image contains {keyword}? Write '0' if not, '1' if yes. Do not write responses longer than one char.",
                    "images": [img_byte_arr],
                },
            ],
        )

    print(f"{image}: {response['message']['content']}")
