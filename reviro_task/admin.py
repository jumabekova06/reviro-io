from django.contrib import admin
from .models import QuoteAnalysis

class Quote(admin.ModelAdmin):
    list_display=['quote',]

admin.site.register(QuoteAnalysis,Quote)