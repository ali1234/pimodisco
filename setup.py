from setuptools import setup

setup(
    name='pimodisco',
    keywords='Pimoroni Discord Bot',
    version='2.0.2',
    license='GPLv3+',
    packages=['pimodisco'],
    install_requires=[
        'discord'
    ],
    entry_points={
        'console_scripts': [
            'pimodisco = pimodisco.__main__:main'
        ]
    },
)
