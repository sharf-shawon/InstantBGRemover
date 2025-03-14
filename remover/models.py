from PIL import Image
from django.db import models
from django.forms import ValidationError


def validate_image_resolution(image):
    max_width = 5000
    max_height = 5000

    # Open the image using Pillow
    img = Image.open(image)

    width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(
            f"Image resolution exceeds limits. Maximum allowed is {max_width}x{max_height} pixels."
        )
        
def validate_image_size(image):
    max_size = 10 * 1024 * 1024  # 10MB
    if image.size > max_size:
        raise ValidationError(
            f"Image file size exceeds limit. Maximum allowed size is 10MB."
        )

class ImageUpload(models.Model):
    original = models.ImageField(validators=[validate_image_resolution, validate_image_size])
    processed = models.ImageField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
