from distutils.core import setup

setup(
  name='samp-server-cli',
  version='1.0',
  author='Zeex',
  author_email='zeex@rocketmail.com',
  url='https://github.com/Zeex/samp-server-cli',
  description='Advanced CLI for GTA: San Andreas Multiplayer (SA-MP) server',
  license='BSD',
  py_modules = ['samp_server_cli'],
  entry_points = {
    'console_scripts': ['samp-server-cli=samp_server_cli:main']
  },
)
