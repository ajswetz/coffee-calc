from setuptools import setup

setup(
    name='Coffee Calc',
    version='0.1.0',
    py_modules=['coffeecalc', 'brewratio'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'brew = coffeecalc:brew',
            'convert = coffeecalc:convert',

        ],
    },
)