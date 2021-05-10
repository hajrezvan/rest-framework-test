from django.db import models
from django.utils.timezone import now


class Book(models.Model):
    name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='', upload_to='store_image/', null=True, blank=True)
    favorite = models.BooleanField(default=False)
    create_date = models.DateField(default=now())

    def __str__(self):
        return self.name
