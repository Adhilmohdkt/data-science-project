from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:  # Use List from typing for compatibility
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() to clean newlines
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="data science project",
    version='0.0.1',
    author="adhil mohammed kt",
    author_email="adhil9106@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Read dependencies from requirements.txt
)
