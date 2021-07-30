from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='lifostack',
      version='1.0',
      description='LIFO Implementation of Stack in Python.',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/FireHead90544/stack',
      project_urls={
        "Issue tracker": "https://github.com/FireHead90544/mathemagic/issues",
      },
      author='Rudransh Joshi',
      author_email='rudranshjoshi1806@gmail.com',
      platforms='any',
      license='Apache License 2.0',
      packages=['stack'],
      zip_safe=False,
      install_requires=[])
