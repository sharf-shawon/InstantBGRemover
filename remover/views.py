import os
import uuid
from rembg import remove
from remover.forms import ImageUploadForm
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

def index(request):
    return render(request, "remover/index.html")

def tos(request):
    return render(request, "remover/tos.html")

def about(request):
    return render(request, "remover/about.html")

def faq(request):
    return render(request, "remover/faq.html")

@csrf_protect  # Add CSRF protection
def remove_background(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save(commit=False)  # Don't save yet

            # Generate a random UUID and rename the file
            ext = os.path.splitext(image_obj.original.name)[1]  # Get file extension
            new_filename = f"{uuid.uuid4().hex}{ext}"  # Generate unique filename with extension

            # Define the new path for the uploaded image (relative to MEDIA_ROOT)
            new_upload_path = os.path.join("uploads/", new_filename)

            # Save the file with the new name in the uploads directory
            image_obj.original.name = new_upload_path
            image_obj.save()  # Save it with the updated name

            # Full path to the uploaded file
            input_path = os.path.join(settings.MEDIA_ROOT, new_upload_path)

            # Define the output path for the processed image (relative to MEDIA_ROOT)
            output_filename = f"{uuid.uuid4().hex}.png"
            output_path = os.path.join("processed/", output_filename)

            # Process Image
            with open(input_path, "rb") as f:
                input_image = f.read()
                output_image = remove(input_image)

            # Save processed image
            os.makedirs(os.path.dirname(os.path.join(settings.MEDIA_ROOT, output_path)), exist_ok=True)  # Ensure the directory exists
            with open(os.path.join(settings.MEDIA_ROOT, output_path), "wb") as f:
                f.write(output_image)

            # Update model with processed image path
            image_obj.processed.name = output_path
            image_obj.save()
            # Return the JSON response
            return JsonResponse({
                'input_url': os.path.join(settings.MEDIA_URL, new_upload_path),
                'output_url': os.path.join(settings.MEDIA_URL, output_path)
            })

    return JsonResponse({"error": "Invalid request"}, status=400)