# Generated by Django 2.2.9 on 2020-01-08 15:10

from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_slick_gallery', '0002_auto_20191216_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='text_de',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Slide text content'),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='text_en',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Slide text content'),
        ),
    ]