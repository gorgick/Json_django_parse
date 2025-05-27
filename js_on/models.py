from django.db import models


class DestAnime(models.Model):
    data = models.JSONField(default=dict, blank=True)
