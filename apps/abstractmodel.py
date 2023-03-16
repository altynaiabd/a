from django.db import models
import uuid

class AbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name='Дата и время добавления', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

    class Meta:
        abstract = True

