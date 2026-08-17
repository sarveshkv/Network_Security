from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements from a file and returns them as a list."""
    requirement_lst:List[str] = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and  requirement!='-e .':
                    requirement_lst.append(requirement)
    except Exception as e:
        print(f"Error occurred while reading requirements from {file_path}: {e}")

    return requirement_lst
print(get_requirements("requirements.txt"))

setup(
    name="network_security",
    version="0.0.0",
    author="Sarvesh",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)