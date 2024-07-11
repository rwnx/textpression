from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="textpression",
    version="0.1",
    requires=[
      "typer"
    ],
    entry_points={
      'console_scripts': [
          'textpression = textpression.cli:main',
      ],
    },
    author="Rowan Twell",
    author_email="<rowantwell@gmail.com>",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
)
