from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import Dataset, Distribution


class DistributionInline(admin.TabularInline):
    model = Distribution


class DatasetAdmin(PageAdmin):
    inlines = (DistributionInline,)


admin.site.register(Dataset, DatasetAdmin)
