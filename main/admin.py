from django.contrib import admin

# Register your models here.
from .models import BusinessUser, QuotePricing, RoofQuote, FinalQuote 


@admin.register(BusinessUser)
class BusinessUser(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'slug']
    ordering = ['name']

@admin.register(QuotePricing)
class QuotePricing(admin.ModelAdmin):
    list_display = ['client']
    ordering = ['client']

@admin.register(RoofQuote)
class RoofQuote(admin.ModelAdmin):
    list_display = ['quote_id', 'business_user', 'first_name', 'last_name']
    ordering = ['quote_id']

@admin.register(FinalQuote)
class FinalQuote(admin.ModelAdmin):
    list_display = ['roof_quote', 'business_user']
    ordering = ['roof_quote']