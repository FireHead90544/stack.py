from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='stack.py',
      version='2.0',
      description='LIFO Stack & FIFO Queue Implementation in Python.',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/FireHead90544/stack.py',
      project_urls={
        "Issue tracker": "https://github.com/FireHead90544/stack.py/issues",
      },
      author='Rudransh Joshi',
      author_email='rudranshjoshi1806@gmail.com',
      platforms='any',
      license='Apache License 2.0',
      packages=['stack'],
      zip_safe=False,
      install_requires=[])
