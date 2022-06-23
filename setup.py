from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1.0.0","mysql-connector-python>=8.0"]

setup(
    name="py-db-interface",
    version="0.0.1",
    author=["Felix Schulz", "Stefan Mayer"],
    author_email="felixschulz@uni-tuebingen.de",
    description="An implementation of the R package {DBI} in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/felixschulz385/py-db-interface.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)