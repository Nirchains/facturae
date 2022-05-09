from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in facturae/__init__.py
from facturae import __version__ as version

setup(
	name="facturae",
	version=version,
	description="Facturae",
	author="Pedro Antonio Fernández Gómez",
	author_email="pedro@hispalisdigital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
