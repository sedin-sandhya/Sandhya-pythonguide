from django.db import models

# Create your models here.


class ShortURL(models.Model):
    url = models.URLField(max_length=500)

    short_code = models.CharField(max_length=10, unique=True)
    access_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_code
