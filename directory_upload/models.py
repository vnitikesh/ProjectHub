from django.db import models

# Create your models here.
class Directory(models.Model):
    docfile = models.FileField(upload_to = 'directory/%Y/%m/%d')
    directory_name = models.CharField(null = True, blank = True, max_length = 200)
    
    def __str__(self):
        return self.directory_name
