import base64


def format_image_prompt(image):
    """_summary_

    Args:
        image (Streamlit UploadedFile): See
            - https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
    """
    image_type = image.type
    base64_image = get_base64_encoded_image(image.getvalue())

    return {
        "type": "image",
        "source": {"type": "base64", "media_type": image_type, "data": base64_image},
    }


def get_base64_encoded_image(image_bytes):
    base_64_encoded_data = base64.b64encode(image_bytes)
    base64_string = base_64_encoded_data.decode("utf-8")
    return base64_string
