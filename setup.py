from distutils.core import setup

setup(
  name='samp-server-cli',
  version='0.1.6',
  author='Zeex',
  author_email='zeex@rocketmail.com',
  url='https://github.com/Zeex/samp-server-cli',
  description='A command line interface for SA-MP server',
  license='BSD',
  py_modules = ['samp-server-cli'],
  entry_points = {
    'console_scripts': ['samp-server-cli=samp-server-cli:main']
  },
)
