from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-setstateforpendingvalidation',
    version=version,
    description="Will set the state of dataset to draft when new resources are uploaded",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Thomas Gilbert',
    author_email='thomas.gilbert@alexandra.dk',
    url='www.alexandra.dk/thomas.gilbert',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.setstateforpendingvalidation'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.setstateforpendingvalidation.plugin:PluginClass
	setstateforpendingvalidation = ckanext.setstateforpendingvalidation.plugin:SetStateForPendingValidationPlugin
    ''',
)
