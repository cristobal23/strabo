# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="strabo",
    version='0.1',
    url='https://github.com/cristobal23/strabo',
    description='A Flask app that shows interesting places nearby.',
    author='Crist\u00f3bal Villarroel',
    author_email='cristobal23@gmail.com',
    packages=["strabo"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'geocoder',
        'hyperlink',
        'Flask-SQLAlchemy',
        'Flask-Caching',
        'Flask-WTF',
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
