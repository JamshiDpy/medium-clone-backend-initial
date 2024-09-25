from modeltranslation.translator import TranslationOptions, register
from .models import  CustomUser


@register(CustomUser)
class CustomUSerTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'middle_name')

