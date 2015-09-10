from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Scrap(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=250)
    pubdate = models.DateTimeField(
        verbose_name=_("Created on")
    )
    link = models.CharField(max_length=32)
    guid = models.CharField(max_length=16, unique=True)
    started_on = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Started On")
    )

    def __str__(self):
        return str(title)
