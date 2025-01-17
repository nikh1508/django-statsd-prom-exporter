import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="django-statsd-prom-exporter",
    version='0.3.0',
    url="https://github.com/workindia/django-statsd-prom-exporter",
    license="MIT license",

    author="Kshitij Nagvekar",
    author_email="kshitij.nagvekar@workindia.in",

    description="A collection of django middleware to track django + WSGI service metrics accurately via "
                "prom/statsd-exporter sidecar + prometheus",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        'django',
        'datadog >= 0.42.0'
    ],
    setup_requires=[
        'wheel',
        'pip>=20'
    ],
    python_requires='>=3.6',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent"
    ],
)
