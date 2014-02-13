"""Forms or the ``cmsplugin_link_extended`` app."""
from django import forms
from django.utils.translation import ugettext_lazy as _

from cms.plugins.link.forms import LinkForm

from .models import LinkExtension


class CustomLinkForm(LinkForm):
    css_classes = forms.CharField(
        max_length=256,
        label=_('CSS classes'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CustomLinkForm, self).__init__(*args, **kwargs)
        if self.instance:
            try:
                extension = LinkExtension.objects.get(link=self.instance)
            except LinkExtension.DoesNotExist:
                pass
            else:
                self.initial['css_classes'] = extension.css_classes

    def save(self, *args, **kwargs):
        instance = super(CustomLinkForm, self).save(*args, **kwargs)
        instance.save()
        try:
            extension = LinkExtension.objects.get(link=instance)
        except LinkExtension.DoesNotExist:
            extension = LinkExtension(link=instance)
        extension.css_classes = self.cleaned_data['css_classes']
        extension.save()
        return instance
