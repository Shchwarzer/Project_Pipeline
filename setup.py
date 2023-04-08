from setuptools import setup, find_packages


setup(name="census-income", 
version = "0.0.1",
author = "Shubham",
author_email="shubham.s.torawane@gmail.com",
packages= find_packages(),
install_requires = ["pandas", "numpy", "seaborn" ,"scipy"]
     )