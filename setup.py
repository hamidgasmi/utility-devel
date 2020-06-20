from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='utility-devel',
    version='0.1.0',
    author='Hamid Gasmi',
    author_email='mamid1706@hotmail.fr',
    description='A utility for unit-testing python projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hamidgasmi/utility-devel',
    packages=find_packages('src')
)