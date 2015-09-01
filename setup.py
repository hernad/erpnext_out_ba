from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='erpnext.out.ba',
    version=version,
    description='ERPNext.out.ba website',
    author='bring.out.ba',
    author_email='hernad@bring.out.ba',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
