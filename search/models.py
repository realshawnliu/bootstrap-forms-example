from django.db import models


class Search(models.Model):
    domain = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
