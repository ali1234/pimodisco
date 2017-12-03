from setuptools import setup
from pimodisco import version, source_url

setup(
    name='pimodisco',
    keywords='Pimoroni Discord Bot',
    version=version,
    url=source_url,
    license='GPLv3+',
    packages=['pimodisco'],
    install_requires=[
        'discord', 'algoliasearch'
    ],
    entry_points={
        'console_scripts': [
            'pimodisco = pimodisco.__main__:main'
        ]
    },
)
