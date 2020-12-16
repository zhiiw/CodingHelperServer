from django.db import models
from django.contrib.auth.models import User


class Time(models.Model):

    total = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    java = models.DecimalField(max_digits=5, decimal_places=2)
    rs = models.DecimalField(max_digits=5, decimal_places=2)
    hs = models.DecimalField(max_digits=5, decimal_places=2)
    py = models.DecimalField(max_digits=5, decimal_places=2)
    kt = models.DecimalField(max_digits=5, decimal_places=2)
    js = models.DecimalField(max_digits=5, decimal_places=2)
    go = models.DecimalField(max_digits=5, decimal_places=2)
    cpp= models.DecimalField(max_digits=5, decimal_places=2)
    c = models.DecimalField(max_digits=5, decimal_places=2)
    other = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        # return self.title 将文章标题返回
        return self.total
# Create your models here.
