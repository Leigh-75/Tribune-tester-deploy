from django.forms import ModelForm
from .models import Image
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
from cloudinary.forms import CloudinaryFileField

class ImageForm(ModelForm):
    image = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'media'
        }
    )
    class Meta:
        model = Image
        fields = ['image','image_name','image_location', 'image_category']