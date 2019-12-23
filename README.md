# cmsplugin-slick-gallery


### Requirements

django-modeltranslation
djangocms-text-ckeditor

slick.min.js
slick-theme.min.css
slick.min.css
(http://kenwheeler.github.io/slick/)

### Installation

1. cmsplugin-slick-gallery utilizes the power of django modeltranslation module to create galleries with multilingual text on them
It's necessary to run makemigrations first so that fields with correct languages will be added to the database
```python
python manage.py makemigrations
python manage.py migrate
```


2. Add cmsplugin_slick_gallery to INSTALLED APPS:

```python
INSTALLED_APPS = (
        ...
        'cmsplugin_slick_gallery',
        ...
    )
```

3. Remember to add js/css requirements to `<head>` in your base template, after jQuery, for example (depending on location of your files):
```html
<link rel="stylesheet" type="text/css" href="{% get_static_prefix %}css/slick.min.css">
<link rel="stylesheet" type="text/css" href="{% get_static_prefix %}css/slick-theme.min.css">
<script src="{% get_static_prefix %}js/slick.min.js"></script>

```
or using CDN:
```html
<link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
<link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"/>
<script type="text/javascript" src="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>

```