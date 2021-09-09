from django.db import models


# Create your models here.
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.MP3', '.mp3', '.m4a']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Music(models.Model):
    CATEGORIES = (
        ('kd', 'Karadeniz Yöresi'),
        ('ad', 'Anadolu Yöresi'),
        ('mr', 'Marmara Yöresi'),
        ('eg', 'Ege Yöresi'),
    )
    category = models.CharField(max_length=3, choices=CATEGORIES)
    music_name = models.CharField(max_length=200)
    singer_name = models.CharField(max_length=200)
    url = models.FileField(upload_to='musics', validators=[validate_file_extension])

    def __str__(self):
        return self.music_name


class Video(models.Model):
    place = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images/')
    video = models.FileField(upload_to='media/videos/')

    def __str__(self):
        return self.place + " " + self.city
