from django.contrib import admin
from .models import ContactForm, ApprenticeShip


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')


@admin.register(ApprenticeShip)
class ApprenticeShip(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')



