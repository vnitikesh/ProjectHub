from django.db import models

# Create your models here.

class ProjectUpload(models.Model):
    title = models.CharField(max_length = 100, null = True, blank = True)
    codebase_link = models.CharField(max_length = 100, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    technology_used = models.CharField(max_length = 225, null = True, blank = True)
    graphic = models.FileField(upload_to = None, max_length = 200, null = True, blank = True)

    def __str__(self):
        return self.title
