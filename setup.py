from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Python package to encrypt data for Adyen payment processing'
LONG_DESCRIPTION = "A package that allows you do take information and encrypt it to be submitted to Adyen's payment processor"

# Setting up
setup(
    name="Py Adyen Encrypt",
    version=VERSION,
    author="66niko99",
    author_email="niko@slimaio.com",
    description=DESCRIPTION,
    url="https://github.com/66niko99/py-adyen-encrypt",
    packages=find_packages(),
)

