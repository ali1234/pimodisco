from setuptools import setup
from pimodisco import version

setup(
    name='pimodisco',
    keywords='Pimoroni Discord Bot',
    version=version,
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
