from distutils.core import setup

setup(
  name='samp-server-cli',
  version='0.1.1',
  author='Zeex',
  author_email='zeex@rocketmail.com',
  url='https://github.com/Zeex/samp-server-cli',
  description='A command line interface for SA-MP server',
  license='BSD',
  entry_points = {
    'console_scripts': ['samp-server-cli=samp-server-cli:main']
  },
)
