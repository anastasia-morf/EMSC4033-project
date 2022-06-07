# EMSC4033-project
My project for EMSC4033, 2022

Paleoclimatology is a highly collaborative field that relies on online databases for data sharing. However, accessing, analyzing, modelling and visualizing paleoclimate observations can be extremely time consuming, especially when dealing with large data volumes. 

`LiPD` (Linked Paleo Data) is a convenient tool that provides a standardized format for storing and exchanging paleoclimate data, enabling quick querying and extraction. But there are some tricks to know before we can use it.

The purpose of this Git repository is to provide a set of modules that can be used as an introduction to Python utilities for LiPDs. By following these modules, you will learn (1) how to create a new environemnt and install `LiPD` and (2) how to use the `LiPD` package to access and visualise data contained in large datasets.

## Guide to the Repository 	

To get started, you will first need to copy or "fork" the repository, which will allow you to freely experiment and modify the notebooks without affecting the original code. 

Everything that you need next is contained within these files: 

#### Jupyter Notebooks 
There are notebooks two contained in the repository: 
1. Installation.ipynb - Provides instructions to creating a new environment and installing `LiPD`.
2. GraphMaker.ipynb - Generalised plotter notebooks that teaches `LiPD` functionalities.

#### src folder
1. dependencies.py - contains all of the dependencies you need to load to run the notebook
2. my_functions.py - contains all of the functions needed to run the notebook

#### Tests folder 
- tests_functions.py - contains all the functions needed to run the tests 
- src folder - duplicate of above you and can ignore this - simply there for loading 

#### Resources 
Contains the `LiPD` files needed to run the code.

#### ProjectPlan.md 
The project plan - contains more information about this project (executive summary, requirements, timeline, review of existing codes and testing plan)

#### ProjectReport.md 
The project report contains the user instructions, list of dependencies, a description of the testing code, as well as limitations and future improvements. 

#### Runtests.ipynb
- Contains a function for file validation and !pytest

Hope you find this useful and please contact me if you have any suggestions for improvements :) 
