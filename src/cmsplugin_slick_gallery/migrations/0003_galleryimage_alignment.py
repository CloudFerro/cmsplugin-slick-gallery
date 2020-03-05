# Generated by Django 2.2.11 on 2020-03-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_slick_gallery', '0002_auto_20191216_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='alignment',
            field=models.CharField(choices=[('center', 'center'), ('left', 'left'), ('right', 'right'), ('bottom', 'bottom'), ('top', 'top')], default='center', max_length=255, verbose_name='image alignment'),
        ),
    ]