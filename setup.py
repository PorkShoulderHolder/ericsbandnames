from setuptools import setup

setup(name='ericsbandnames',
      packages=['ericsbandnames'],
      version='0.3',
      description='Simple client for scraping the contents of ericsbandnames.com, some of which may be offensive, lewd, and/or puerile. However, majority of them are hilarious.',
      author='Sam Fox Royston (code), Eric Andre (content)',
      author_email='sfoxroyston@gmail.com',
      license="MIT",
      url='https://github.com/PorkShoulderHolder/ericsbandnames',
      keywords=["text", "joke", "eric andre", "nsfw", "scraping"],
      install_requires=["requests", "beautifulsoup4"],
      entry_points='''
          [console_scripts]
          ericsbandnames=ericsbandnames:cli
       ''',
)

