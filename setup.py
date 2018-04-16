from setuptools import setup



def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt")
print(install_reqs)
# reqs = [str(ir.req) for ir in install_reqs]


setup(name='ericsbandnames',
      packages=['ericsbandnames'],
      version='0.2',
      description='Simple client for scraping the contents of ericsbandnames.com, some of which may be offensive, lewd, and/or puerile. However, majority of them are hilarious.',
      author='Sam Fox Royston (code), Eric Andre (content)',
      author_email='sfoxroyston@gmail.com',
      license="MIT",
      url='https://github.com/PorkShoulderHolder/ericsbandnames',
      keywords=["text", "joke", "eric andre", "nsfw", "scraping"],
      install_requires=install_reqs,
      entry_points='''
          [console_scripts]
          ericsbandnames=ericsbandnames:cli
       ''',
)

