from django.db import models

class ImageUpload(models.Model):
    original = models.ImageField()
    processed = models.ImageField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
