from setuptools import setup, find_packages

setup(
    name="mypkg",
    version="0.1.0",
    packages=find_packages(exclude="tests"),
    entry_points={
        "console_scripts": ["mypkg=mypkg.cli:main"]
    },
)