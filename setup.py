from setuptools import find_packages,setup
from typing import List

hyphendot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hyphendot in requirements:
            requirements.remove(hyphendot)
        
    return requirements


setup(
    name='score_prediction',
    version='0.1.0',
    author='shruti',
    author_email='dharreny@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)