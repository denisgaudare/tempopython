import datetime
import re
from pathlib import Path

from setuptools import setup, find_packages

def get_version():
    content = Path("mypkg/__init__.py").read_text()
    match = re.search(r'__version__\s*=\s*"(.+?)"', content)
    return match.group(1)

# Exemple de génération de fichier dynamique
with open("mypkg/generated_info.py", "w") as f:
    f.write(f'# Ce fichier a été généré automatiquement\n')
    f.write(f"BUILD_DATE = 'XYZ'")


setup(
    name="mypkg",
    install_requires=[
        'requests>=2.0',
        'numpy~=1.24.0',
    ],
    version=get_version(),
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["mypkg=mypkg.cli:main"]},
)
