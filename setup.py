from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="teste_vitali",
    version="0.0.1",
    author="Tiago Vitali",
    author_email="televisaos@hotmail.com",
    description="Test version - Training package creation. This project belongs to Tiago Vitali, chemistry Technician, Oerations Technician, Chemical Engineering, Project Manager and  Data Scientist student. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp DIO UNIMED Ciência de Dados. E-mail:televisaos@hotmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Televisaos",
    packages=find_packages(),
    #install_requires=requirements, #Apenas se o pacote possuir dependência de outros pacotes
    python_requires='>=3.8',
)