"""Models for the ``cmsplugin_link_extended`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.plugins.link.models import Link


class LinkExtension(models.Model):
    """This model extends the original Link model."""
    link = models.ForeignKey(
        Link,
        verbose_name=_('Link'),
        related_name='extensions',
    )

    css_classes = models.CharField(
        max_length=256,
        verbose_name=_('CSS Classes'),
        blank=True,
    )
