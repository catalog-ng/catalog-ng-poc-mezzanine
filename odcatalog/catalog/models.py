from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField



class Dataset(Page):
    license = models.CharField(max_length=128, null=True, blank=True)
    long_description = RichTextField(null=True, blank=True)

    search_fields = ("long_description",)


class Distribution(models.Model):
    dataset = models.ForeignKey(Dataset, related_name='distributions')

    # A URL pointing to the resource
    url = models.CharField(max_length=256)

    # An optional title/description
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # Distribution type: stuff like "file", "api", ...
    distribution_type = models.CharField(max_length=128, null=True, blank=True)

    # Descriptive format, eg. "json" or "csv"
    data_format = models.CharField(max_length=128, null=True, blank=True)

    # Mime type of the file, eg. "application/json"
    mime_type = models.CharField(max_length=128, null=True, blank=True)

    # Size of the file (retrieved automatically)
    size = models.PositiveIntegerField(null=True, blank=True)
