import base64
from io import BytesIO


def encode_image(image):
    bytes_data = BytesIO(image.getvalue())
    base64_image = base64.b64encode(bytes_data.getvalue()).decode()
    data_uri = f"data:image/{image.type.split('/')[-1]};base64,{base64_image}"
    return {"type": "image_url", "image_url": data_uri}
