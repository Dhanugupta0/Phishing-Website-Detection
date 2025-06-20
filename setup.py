from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This fn will return list of requiremnets
    '''
    requirement_lst: List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            ##proccess each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Dhanu Gupta",
    author_email="guptadhanu5842@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()


    )