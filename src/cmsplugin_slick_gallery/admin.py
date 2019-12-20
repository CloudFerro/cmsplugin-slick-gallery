from django.contrib import admin

from .models import GalleryImage, SlickGallery

class GalleryImageInline(admin.StackedInline):
    model = GalleryImage
    extra = 1

class SlickGalleryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ('folders',)
    inlines = (GalleryImageInline,)

admin.site.register(SlickGallery, SlickGalleryAdmin)
