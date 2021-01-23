from django.db import models

# Create your models here.
class ProjectModel(models.Model):
    title = models.CharField(max_length = 128, null = True, blank = True)
    image = models.ImageField(upload_to = 'images', null = True, verbose_name = "")
    videofile = models.FileField(upload_to = 'video', null = True, verbose_name = "")
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.title +":"+ str(self.videofile)
