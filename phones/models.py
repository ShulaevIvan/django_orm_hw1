from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")