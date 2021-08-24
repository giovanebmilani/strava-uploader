from setuptools import setup
from setuptools import find_packages

setup(
    name="strava-uploader",
    version="1.0.0",
    description="",
    author="Giovane Bianchi Milani",
    author_email="giovanebmilani@hotmail.com",
    url="https://github.com/giovanebmilani/strava-uploader",
    install_requires=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "strava-uploader = uploader:main",
        ]
    },
)