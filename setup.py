import os
from setuptools import setup, find_packages
import cmsplugin_link_extended


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

dependency_links = [
    'https://github.com/divio/django-cms/tarball/3a09d5c39b3469e64aeecc0205a193f5b70c2061',  # NOQA
]

setup(
    name="cmsplugin-link-extended",
    version=cmsplugin_link_extended.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, django-cms, plugin, link, extension',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/cmsplugin-link-extended",
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    dependency_links=dependency_links,
    include_package_data=True,
)
