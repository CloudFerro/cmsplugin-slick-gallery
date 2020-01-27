from builtins import object
from os import name
from tkinter import Image
from venv import create

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from cmsplugin_slick_gallery.cms_plugins import SlickGalleryPluginBase
from cmsplugin_slick_gallery.models import (SlickGallery, SlickGalleryPlugin,
                                            GalleryImage)
from django.test import TestCase
from django.test.client import RequestFactory
from filer.models import ThumbnailOption
from filer.models import File, Image
from filer import settings as filer_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.utils.module_loading import import_string
from sekizai.context import SekizaiContext
import numpy as np
import shutil

# based on
# http://docs.django-cms.org/en/latest/how_to/testing.html#testing-plugins
# https://github.com/divio/django-filer/blob/master/tests/test_filer_check.py


class SlickGalleryPluginTests(TestCase):
    @classmethod
    def setUpClass(cls):
        # ensure that filer_public directory is empty from previous tests
        storage = import_string(
            filer_settings.FILER_STORAGES['public']['main']['ENGINE'])()
        upload_to_prefix = filer_settings.FILER_STORAGES['public']['main']['UPLOAD_TO_PREFIX']
        if storage.exists(upload_to_prefix):
            shutil.rmtree(storage.path(upload_to_prefix))


        original_filename = 'testimage.jpg'
        file_obj = SimpleUploadedFile(
            name=original_filename,
            content=np.zeros([300, 300, 3], dtype=np.uint8).fill(255),
            content_type='image/jpeg')
        filer_file = File.objects.create(
            file=file_obj,
            original_filename=original_filename)
        test_image = Image.objects.create(
            file_ptr=filer_file, uploaded_at=filer_file.uploaded_at)

        thumbnail_option = ThumbnailOption.objects.create(name="thumb_opt",
                                                            width=200,
                                                            height=100)
        cls.slick_gallery = SlickGallery.objects.create(name="Test",
                                                        width=200,
                                                        width_units="px",
                                                        height=100,
                                                        height_units="px",
                                                        thumbnail_option=thumbnail_option)
        GalleryImage.objects.create(
            image=test_image, gallery=cls.slick_gallery)
        cls.placeholder = Placeholder.objects.create(slot='test')
        super(SlickGalleryPluginTests, cls).setUpClass()


    def test_plugin_context(self):
        model_instance = add_plugin(
            self.__class__.placeholder,
            SlickGalleryPluginBase,
            'en',
            position='last-child',
            target=None,
            gallery_id=self.__class__.slick_gallery.id
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('instance', context)
        self.assertEqual(
            context['instance'].gallery.galleryimage_set.all().count(), 1)

    def test_plugin_html(self):
        self.maxDiff = None
        expected_html = '''
<section class="carousel" id="slick-carousel-1" style="width:200px; 
                                                                    height:100px;">
    <img class="carousel-left" id="slick-carousel-left-1" src="/static/cmsplugin_slick_gallery/icons/2289-arrow-left.svg" alt="Carousel left"/>
    <div class="carousel-items" id="slick-carousel-items-1">  
        <div>
            <img src="" alt="Carousel-img"/>
            <div class="wrapper carousel-desc flex-wrapper vertical justify-center" style="top: 0%; left: 15%;">
                
            </div>
        </div>
    </div>
    <img id="slick-carousel-right-1" class="carousel-right" src="/static/cmsplugin_slick_gallery/icons/2290-arrow-right.svg" alt="Carousel right"/>
</section>
        '''
        model_instance = add_plugin(
            self.__class__.placeholder,
            SlickGalleryPluginBase,
            'en',
            position='last-child',
            target=None,
            gallery_id=self.__class__.slick_gallery.id
        )
        renderer = ContentRenderer(request=RequestFactory())
        sekizai_context = SekizaiContext()
        html = renderer.render_plugin(model_instance, context=sekizai_context)
        self.assertHTMLEqual(html, expected_html)
