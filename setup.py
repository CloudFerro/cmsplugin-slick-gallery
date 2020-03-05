from setuptools import setup, find_packages

setup(
    name="cmsplugin-slick-gallery",
    version='1.1.5',
    url='https://github.com/CloudFerro/cmsplugin-slick-gallery',
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
    license='BSD',
    description="gallery plugin for django-cms using slick.js",
    long_description=open('README.md').read(),
    author='Radosław Stępień',
    author_email='rstepien@protonmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.11",
        "django-filer >= 1.2.0",
        "django-cms >= 3.4",
    ],
    zip_safe=False,
)
