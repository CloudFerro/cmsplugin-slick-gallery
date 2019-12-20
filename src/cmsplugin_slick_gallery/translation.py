from modeltranslation.translator import translator, TranslationOptions
from .models import GalleryImage

class GalleryImageTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(GalleryImage, GalleryImageTranslationOptions)