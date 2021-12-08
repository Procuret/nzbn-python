"""
New Zealand Business Number
PyPI Setup Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
from setuptools import setup, find_packages
from os import path
from codecs import open
from nzbn.version import VERSION

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name='nzbn',
    version=VERSION,
    description='New Zealand Business Number library',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/procuret/nzbn-python',
    author='Procuret',
    author_email='hugh@procuret.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Office/Business :: Financial'
    ],
    keywords='library http api web payments finance nzbn new-zealand nz busine\
ss business-number',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    project_urls={
        'Github Repository': 'https://github.com/procuret/nzbn-python',
        'About': 'https://github.com/procuret/nzbn-python'
    }
)
