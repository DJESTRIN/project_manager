# setup.py in my_repo/
from setuptools import setup, find_packages

setup(
    name='projectmanager',
    version='0.1',
    packages=find_packages(),  # Automatically find subfolder1 and subfolder2 as packages.
    install_requires=['rich'],
    author='David Estrin',
    author_email='',
    description='A short description of your project',
    url='https://github.com/DJESTRIN/Sweet2PPlus',  # Replace with your repository URL.
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
