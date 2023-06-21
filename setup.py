import sys

if not 'sdist' in sys.argv:
    sys.exit(
        """\n\n\n\n\n\n\n\n
  ____                  _     _
 |  _ \  ___  ___ _ __ | |   (_)_ __ ___   ___   |
 | | | |/ _ \/ _ \ '_ \| |   | | '_ ` _ \ / _ \  |     CONTACT US FOR A LICENSE OF GEOLIME
 | |_| |  __/  __/ |_) | |___| | | | | | |  __/  |             contact@deeplime.io
 |____/ \___|\___| .__/|_____|_|_| |_| |_|\___|  |
                 |_|                             |

        \n\n\n\n\n\n\n\n
        """
        )

from setuptools import setup


setup(
    name='geolime',
    version='1.3.0',
    description='Deeplime Python Library',
    url='https://github.com/deeplime-io/geolime',
    author='Deeplime',
    author_email='contact@deeplime.io',
    license='LICENSE',
    python_requires='>=3.8',
)
