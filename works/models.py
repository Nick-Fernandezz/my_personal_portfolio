from django.db import models

# Create your models here.


class PortfolioWorks(models.Model):
    name = models.TextField(null=False, max_length=100, blank=True)
    description = models.TextField(null=False, max_length=300, blank=True)
    link = models.URLField(null=True, blank=True)
    media = models.ImageField(upload_to='works/images')

