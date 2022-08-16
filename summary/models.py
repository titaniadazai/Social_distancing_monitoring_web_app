from django.db import models

# Create your models here.


# class location(models.Model):
#    area = models.CharField(max_length=100)
#   img_src = models.CharField(max_length=100)
#  video_src = models.CharField(max_length=100)

# def _str_(self):
#    return f"{self.area} ({self.img_src})"


class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")

    def _str_(self):
        return self.caption
