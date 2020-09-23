from django.db import models
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class File(MPTTModel):
    name = models.CharField(max_length=256)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='children'
    )
    folder = models.BooleanField(default=False, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
