# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.

    The version of the OpenAPI document: 1.0.0
    Contact: team@digitalpsych.org
"""

from setuptools import setup, find_packages

setup(
    name="LAMP_core",
    version="1.0.5",
    description="LAMP Platform",
    author="Division of Digital Psychiatry at Beth Israel Deaconess Medical Center.",
    author_email="team@digitalpsych.org",
    url="https://docs.lamp.digital/",
    keywords=["LAMP Platform"],
    install_requires=[
      "urllib3 >= 1.15",
      "six >= 1.10",
      "certifi",
      "python-dateutil",
      "nulltype",
      "numpy",
      "pandas",
    ],
    extras_require={':python_version <= "2.7"': ['future']},
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The LAMP Platform API.
    """
)
