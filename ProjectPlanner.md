# EMSC4033 Project Plan 

### Introduction to Python utilities for LiPD files

## Executive summary


The LiPD framework is standardized format for paleoclimate files, but can be difficult to navigate if you are not an experienced user. For this project, I will construct a generalised plotter notebook that can be used as a template for users to filter (e.g. spatially, temporally, types of proxy system) and assess records (e.g. time series within a particular temporal window) and metadata (e.g. publication information) from LiPD files/ databases as needed. This will be useful to users who are not familiar with the LiPD format, or want to quickly access data from databases without having to learn how to use data analysis packages such as Pyleoclim/GeochronR.
 

## Goals

I will create two Jupyter notebooks, which will achieve the goals of:
1) Teaching a user how to set up a new environment, install LiPD and the relevant utilities.
2) Provide a template for users to access infrormation from LiPD files through a generalised plotter notebook. This will involve: 
    - reading LiPD files 
    - Convert LiPD files to Excel
    - displaying the data on spatial and temporal scales and 
    - filtering variables.


## Background and Innovation  

Paleoclimatology is a highly collaborative field that relies on online databases for data sharing. However, accessing, analyzing, modelling and visualizing paleoclimate observations can be extremely time consuming, especially when dealing with large data volumes. To deal with this issue, the standardized LiPD (short for Linked PaleoData) framework was built for the quick and easy exchange of paleoclimate data amongst scientists. The package allows users to convert existing data into LiPD files, as well as analyze and manipulate LiPD data.

This package is still in development, and although there are some tutorials available, they are hard to navigate for inexperiened users and make use of additional data analysis packages (e.g. pyleoclim), that require some dependencies unavailable to Windows. My project will build on this existing documentation (more information can be found on the official [LiPD Utilities’s documentation](https://nickmckay.github.io/LiPD-utilities/python/index.html) and [Linked Earth Wiki](http://wiki.linked.earth/Using_LiPD_files)). 

My aim for this project is to provide a simpler, more straight-foward documentation, which can serve as a motivation for more scientists to make use of this package though a generalised plotter notebook that can help teach new users how to install and use the `LiPD` package. 

## Resources & Timeline

- I'll be using the existing package `LiPD` and it's existing documentation and [module contents](http://nickmckay.github.io/LiPD-utilities/python/source/lipd.html#module-lipd) to help me write my code. I will build extra functionalities to use with this package. 
- I will be downloading LiPD files from [NOAA](https://www.ncei.noaa.gov/access/paleo-search/), [LinkedEarth Wiki](http://wiki.linked.earth/Main_Page) and [PANGAEA](https://www.pangaea.de/) and journal publications to test my notebooks.
- I will be in contact with my former supervisor Georgina Falster, who introduced me to this package and has helped me learn how to use it if I have any problems. 
- This will be a one off project and I do not intend to continue in the future.


## Testing, validation, documentation

I will be conducting tests using both the `assert` function and the validation tests avaiable in the `LiPD` package.



**Note:** You need to think about how you will know your code is correct and achieves the goals that are set out above (specific tests that can be implemented automatically using, for example, the `assert` statement in python.)  It can be really helpful if those tests are also part of the documentation so that when you tell people how to do something with the code, the example you give is specifically targetted by some test code.

_Provide some specific tests with values that you can imagine `assert`ing_

