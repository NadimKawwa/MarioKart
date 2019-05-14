# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path


from io import open

here = path.abspath(path.dirname(__file__))



# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
    
setup (
    name='MarioKart',
    version='0.1',
    description='Fun way to keep track of mario kart players',
    author='Nadim Kawwa',
    author_email='nadimkawwa91@gmail.com',
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Luigi', 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    project_urls={
        'Github': 'https://github.com/NadimKawwa',
        'Say Hi!': 'https://www.instagram.com/nadim.961/',
        "Let's connect!": 'https://www.instagram.com/nadim.961/',
    },
)