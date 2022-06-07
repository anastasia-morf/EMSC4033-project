## EMSC4033 - Project Report

### Instructions 

First, the user has to follow the installation guide `Installation.ipynb` and ensure that lipd can be imported. Then, the user can either choose a single file from the uploaded dataset (from the Resources folder), or download LiPD files through the recommended websites, and define the path on the third kernel. The notebook will then run the code for plotting the timeseries contained in the LiPD file. The timeseries graphs display the age on the x axis, and the proxy type on the y axis. 

Next, the user can opt to upload a larger dataset and run the code for creating a CSV table. This table contains information regarding the archive type, proxy type, age, location and resolution. The information contained in this table is then used to create temporal and spatial graphs. 

The temporal graph displays the temporal extent of each LiPD file, sorted by latitude and colour cocded based on archive type. The user is able to modify the age ranges they wish to be displayed in this graph. 

The spatial map displays the locations of each site referenced in the LiPD dataset, colour coded by archive type. The The is able to modify the map extent they wish to have displayed. 

Finally, the user can run an example for filtering the dataset, and create time series plots based on the filtered dataset. 


### List of dependencies	

The following dependencies are used, loaded in dependencies.py:
- **lipd**: Reading and manipulating LiPD files
- **matplotlib**
  - **matplotlib.pyplot**: For figures and graphs 
    - **figure**: Creating figures 
  - **matplotlib.ticker**: Removing the y axis values on the temporal plot  
  - **matplotlib.patches**: 2D artists 
- **numpy**: Numerical processing 
- **csv**: Converting LiPD data into CSV format
- **pandas**: Data analysis
- **cartopy**
  - **cartopy.crs**: Changing the map projection
  - **cartopy.feature**: Adding land features to map 
- **sys**: system functionalities (removing print() functionality)
- **os**: directory functionalities (removing print() functionality)
- **warnings**: raise warnings while program runs



### Describe testing	

There were 5 tests written. These are available in test_functions.py. Unfortunately, they do not cover all of the functionalities in the package and are quite simple - I was facing lots of problems with running pytest and I ended up running out of time when writing the functions.
Nevertheless, the testing functions written include:
- test_if_data_is dictionary(): - Testing whether the data we have loaded is a dictionary. This is importart as it will tell us if any LiPD files are corrupt.
- test_check_for_specific_file(): This will test whether a specific file has been loaded in the dataset - useful for the user if they are working with a large dataset and want to investigate a specific file
- test_extracted_time_series(): this will test whether the data series output from the plot has the correct number - this test is only specific to the example code I have provided.
- test_make_plots_axis - tests whether there are valid variables for loading in the plot axes.
- test_make_table - tests the length of the table to see whether the data loaded properly - this test is only specific to the example code I have provided.


### Limitations

There are some limitations to this project that could have not been avoided. Firstly, although this notebook runs relatively fast, it does so because the dataset that was loaded contains only 'light' files - this was done on purpose as the processing time for larger datasets can be quite slow. In reality, when the user tries to load their own dataset, it will take longer to run (few minutes). 

Secondly, although the `LiPD` packages aims for standardization of paleoclimate data, some scientists use different keys for the same measurements (e.g. 'd18O' vs 'd18O' vs 'd18Oforam' etc) which makes it difficult to sort through large datasets. Some common errors have been handled in my code, but it is not exhaustive and will need to be tweaked if more come up. 

I also faced some more specific problems when writing the code: 
- It would have been ideal to be able to drop duplicate time series based on DOI (kernel 8 of GraphMaker.ipynb) but had to use the co-ordinates instead - still not sure why it wasn't working. 
- There is an existing function from the `LiPD` package that allows you to convert LiPDs into CSV files but was not working on my platform - it would have been great to be able to use it or modify it to get the table produced in my code, instead of having to do it manually.
- Testing is not exhaustive - I simply ran out of time and my tests are very simple as a result. 


### Future Improvements	
- Having a third notebook that goes through advanced data analysis methods, such as principal component analysis would have been great. Unfortunately, I was not able to follow through with my original plan so I had to remove this part from my project.
- Going through some of the functionalities available in the analysis package `pyleoclim` would have also been helpful, but the documentation for this was updated in the last few days, so it would have made my project reductant. 
- Allowing the user to choose more variables (e.g. the projection type for the map) or modify the table directly on the notebook would have been great, but they can still do so in `my_functions.py`.
- Writing the main notebook as a tutorial instead of a template would have been nice, but hopefully the code has enough documentation in it that the user can replicate if the want.
- Improve testing and exception handling - improve their coverage. Also adding tests for the exceptions would have been great - I have only tested them manually.


