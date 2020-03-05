from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.folder import Folder
from filer.models import ThumbnailOption
from filer.models.imagemodels import Image

class SlickGallery(models.Model):
    name = models.CharField(_("Gallery name"), max_length=255)
    UNIT_CHOICES = (
        ('px', _("pixels (px)")),
        ('%', _("percent (%)")),
        ('em', _("relative to font size (em)")),
    )
    width = models.PositiveIntegerField(_("width"), null=True, blank=True)
    width_units = models.CharField(_("width units"), max_length=2, choices=UNIT_CHOICES, default='px')
    height = models.PositiveIntegerField(_("height"), null=True, blank=True)
    height_units = models.CharField(_("height units"), max_length=2, choices=UNIT_CHOICES, default='px')
    thumbnail_option = models.ForeignKey(ThumbnailOption, null=True, blank=True, verbose_name=_("Thumbnail configuration"), on_delete=models.CASCADE)
    folders = models.ManyToManyField(Folder, blank=True)

    autoplay =  models.BooleanField(_("Autoplay"), default=True, help_text=_("Autoplays after the page loads"))
    autoplay_speed =  models.IntegerField(_("Autoplay speed"), default=3000, blank=False, null=False, help_text=_("(in miliseconds)"))
    arrows = models.BooleanField(_("Arrows"), default=True, help_text=_("Enable previous/next arrows"))
    dots = models.BooleanField(_("Dots"), default=True, help_text=_("Enable dot indicators"))
    draggable = models.BooleanField(_("Draggable"), default=True, help_text=_("Enable mouse dragging"))
    fade = models.BooleanField(_("Fade"), default=False, help_text=_("Enable fading"))
    infinite = models.BooleanField(_("Infinite"), default=False, help_text=_("Enable infinite loop sliding"))
    initial_slide = models.PositiveIntegerField(_("Initial slide"), default=0, null=False, blank=False, help_text=_("Number of the slide to start on (counting from 0)"))
    pause_on_hover = models.BooleanField(_("Pause on hover/focus"), default=True, help_text=_("Pause when the gallery is hovered over or focused on"))

    @property
    def folder_images(self):
        return list(Image.objects.filter(folder_id__in=self.folders.all().values_list("id", flat=True)).order_by("folder_id"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Slick gallery")
        verbose_name_plural = _("Slick gallery")

class GalleryImage(models.Model):
    gallery = models.ForeignKey(SlickGallery, verbose_name=_("Slick gallery"), on_delete=models.CASCADE)
    image = FilerImageField(null=True, blank=True, default=None, verbose_name=_("Image"), on_delete=models.DO_NOTHING)
    text = HTMLField(_("Slide text content"), blank=True, null=True)
    text_transform_left = models.IntegerField(_("Move text from the left"), default=15, blank=False, null=False, help_text=_("(in percents)"))
    text_transform_top = models.IntegerField(_("Move text from the top"), default=0, blank=False, null=False, help_text=_("(in percents)"))
    ALIGNMENT_CHOICES = (
        ('center', _("center")),
        ('left', _("left")),
        ('right', _("right")),
        ('bottom', _("bottom")),
        ('top', _("top")),
    )
    alignment = models.CharField(_("image alignment"), max_length=255, choices=ALIGNMENT_CHOICES, default='center')
    alternative_url = models.URLField(_("Alternative image url"), null=True, blank=True, default=None)
    alt_text = models.CharField(_("alt text"), null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = _("Gallery image")
        verbose_name_plural = _("Gallery images")
    

class SlickGalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(SlickGallery, verbose_name=_("Choose a gallery"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Slick gallery add-on")
        verbose_name_plural = ("Slick gallery add-ons")
