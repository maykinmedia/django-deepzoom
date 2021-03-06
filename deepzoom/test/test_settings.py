# Django settings for django-deepzoom test project.

import os


DEBUG = True

TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

SECRET_KEY = 'django-deepzoom-test-secret'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': ':memory:', 
    }
}


TEST_ROOT = os.path.abspath(os.path.dirname(__file__))


STATIC_ROOT = os.path.abspath(os.path.join(TEST_ROOT, 'test_static'))

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.abspath(os.path.join(TEST_ROOT, 'test_media'))

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(TEST_ROOT, 'test_static')), 
)

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(TEST_ROOT, '../templates/deepzoom')), 
)

EXTERNAL_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.messages', 
    'django.contrib.sessions', 
    'django.contrib.staticfiles', 
    'django.contrib.sitemaps', 
    'django.contrib.sites', 
]

INTERNAL_APPS = [
    'deepzoom', 
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS



#===django-deepzoom settings====================================================


#This is the directory appended to MEDIA_ROOT for storing uploaded images.
#If defined, but not physically created, the directory will be created for you.
#If not defined, the following default directory name will be used:
#UPLOADEDIMAGE_ROOT = 'uploaded_images'

#These are the keyword arguments used to initialize the deep zoom creator:
#'tile_size', 'tile_overlap', 'tile_format', 'image_quality', 'resize_filter'.
#They strike a good (the best?) balance between image fidelity and file size.
#If not defined the following default values will be used:
#DEEPZOOM_PARAMS = [256, 1, "jpg", 0.85, "antialias"]

#This is the directory appended to MEDIA_ROOT for storing generated deep zooms.
#If defined, but not physically created, the directory will be created for you.
#If not defined, the following default directory name will be used:
#DEEPZOOM_ROOT = 'deepzoom_images'


#EOF django-deepzoom test project settings