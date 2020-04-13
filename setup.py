# coding: utf-8
import os
from _bowie.utils.info_git import get_version
from setuptools import setup, find_packages

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
version = get_version(CURRENT_DIR)
package_name = "taskmanager"

setup(
    name=package_name,
    version=version,
    description="Petisco Sample for a Simple Flask Service",
    author_email="support@alicebiometrics.com",
    url="",
    keywords=["petisco", "flask", "service", "sample", "clean"],
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Petisco Sample for a Simple Flask Service
    """,
)
