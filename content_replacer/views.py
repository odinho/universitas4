# Create your views here.
import json

from armstrong.apps.images.models import Image
from django.conf import settings
from django.http import HttpResponse
from sorl.thumbnail import get_thumbnail

def get_images(request, type, id):
    sizes = settings.ARMSTRONG_PRESETS
    imgs = Image.objects.all()
    json_list = []
    for img in imgs:
        json_list.append({
            'image': get_thumbnail(img.image, str(sizes['article_body']['width'])).url,
            'thumb': get_thumbnail(img.image, str(sizes['article_small']['width'])).url,
        })
    return HttpResponse(json.dumps(json_list), content_type='application/json')
