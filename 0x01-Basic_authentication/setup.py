from setuptools import setup, find_packages

setup(
    name="my_api_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask", "Flask-Cors", "requests",
    ],
    entry_points={
        'console_scripts': [
            'start_server=main:run',
        ],
    },
)
