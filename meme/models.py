from django.db import models
from enum import Enum

# Create your models here.
class Language(Enum):
    BN = "Bengali"
    EN = "English"
    HN = "Hindi"


class MemeTemplate(models.Model):
    id          = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='/meme/meme_template')
    language    = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in Language]
    )

