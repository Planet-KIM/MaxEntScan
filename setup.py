from setuptools import setup, find_packages
import os

__version__ = ""
for line in open('maxentscan/__init__.py'):
    if line.startswith('__version__'):
        exec(line.strip())

# setup pkgs to install
PACKAGES = find_packages()

# list for pre-requisite modules
# requirments.txt is preferred to pin specific version of modules
REQUIRES = []

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('maxentscan')

setup(
    name='maxentscan',
    version=__version__,
    description='package for common modules used in jklab',
    author='dwkim',
    packages = PACKAGES,
    install_requires = REQUIRES,
    python_requires = '>=3.6',
    package_data={'':extra_files}
)
