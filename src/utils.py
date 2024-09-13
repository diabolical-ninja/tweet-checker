import base64
from dataclasses import dataclass, field
from typing import Dict, Literal

from streamlit.runtime.uploaded_file_manager import UploadedFile


@dataclass
class ImageUrlData:
    url: str


@dataclass
class ImageUrlResponse:
    image_url: ImageUrlData
    type: Literal["image_url"] = field(default="image_url")


def format_image_url_prompt(image: UploadedFile) -> ImageUrlResponse:
    """Converts an image to a base64 encoded string and returns a dictionary with the image URL.

    Args:
        image (UploadedFile): See
            - https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
    """
    image_type = image.type
    base64_image = get_base64_encoded_image(image.getvalue())

    url = f"data:{image_type};base64,{base64_image}"
    return ImageUrlResponse(image_url=ImageUrlData(url=url))


def get_base64_encoded_image(image_bytes: bytes) -> str:
    """Convert an image (as bytes) to a base64 encoded string.

    Args:
        image_bytes (bytes): Bytes representation of an image

    Returns:
        str: Images as a base64 encoded string
    """
    base_64_encoded_data = base64.b64encode(image_bytes)
    base64_string = base_64_encoded_data.decode("utf-8")
    return base64_string
