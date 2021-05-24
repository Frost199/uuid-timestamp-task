import uuid

from django.db import models


class UniqueIdentifierTimestamp(models.Model):
    unique_identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "UniqueIdentifierTimestamps"

    def __str__(self):
        return str(self.unique_identifier)
