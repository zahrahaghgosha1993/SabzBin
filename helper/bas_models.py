import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):

    """
        Base Model for add uid, updated, created fields to all Loyalty models

    """

    class Meta:
        abstract = True

    uid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    updated = models.DateTimeField(verbose_name=_("Updated At"),
                                   null=True, auto_now=True)

    created = models.DateTimeField(verbose_name=_("Created At"),
                                   null=True, auto_now_add=True)

