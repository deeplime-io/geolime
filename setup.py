from setuptools import setup, find_packages


setup(
    name='geolime',
    version='0.1.0',
    description='Deeplime Python Library',
    url='https://github.com/deeplime-io/geolime',
    author='Deeplime',
    author_email='contact@deeplime.io',
    license='LICENSE',
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True
)
