from django.db import models
from django.db.models.functions import Length

models.CharField.register_lookup(Length)

class Iswc(models.Model):
    title = models.CharField(max_length=500)
    contributors = models.TextField()
    iswc = models.CharField(max_length=13,unique=True, blank=True, null=True, default=None)

    class Meta:
        constraints = [
            # For iswc == null only
            models.UniqueConstraint(fields=['title','contributors'], name='unique__title__contributors__when__iswc__null',
                                    condition=models.Q(iswc__isnull=True)|models.Q(iswc__length__gt=0)),
            # For iswd != null only
            models.UniqueConstraint(fields=['iswc'], name='unique__iswc__when__iswc__not_null')
        ]

    def __str__(self):
        return self.title