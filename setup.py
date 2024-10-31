from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of requirements,
    excluding any entries like '-e .'.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        # Remove any extra whitespace or newline characters
        requirements = [req.strip() for req in requirements]
        # Remove '-e .' if present
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Mohammad Shuaib",
    author_email="mohammadshuaib3455@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
