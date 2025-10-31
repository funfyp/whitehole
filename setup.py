from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:

long_description = fh.read()

setup(

name="whitehole",

version="0.1.0",

author="Lovely Rhythm Melody",

author_email="lovelyfunfyp@gmail.com",

description="Unified theory of black holes, white holes, and cosmic blinking",

long_description=long_description,

long_description_content_type="text/markdown",

url="https://github.com/funfyp/whitehole",

packages=find_packages(),

classifiers=[

"Programming Language :: Python :: 3",

"Programming Language :: Python :: 3.8",

"Programming Language :: Python :: 3.9",

"Programming Language :: Python :: 3.10",

"Programming Language :: Python :: 3.11",

"License :: OSI Approved :: MIT License",

"Operating System :: OS Independent",

"Topic :: Scientific/Engineering :: Physics",

"Topic :: Scientific/Engineering :: Mathematics",

"Development Status :: 3 - Alpha",

],

python_requires=">=3.8",

install_requires=[

"numpy>=1.21.0",

"scipy>=1.7.0",

"matplotlib>=3.4.0",

],

)