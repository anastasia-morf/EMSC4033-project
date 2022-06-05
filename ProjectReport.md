## EMSC4033 - Project Report

### Instructions 
First, the user has to follow the installation guide `Installation.ipynb` and ensure that lipd can be imported. Then, the user can either choose a single file from the uploaded dataset (from the Resources folder), or download LiPD files through the recommended websites, and define the path on the third kernel. The notebook will then run the code for plotting the timeseries contained in the LiPD file. The timeseries graphs display the age on the x axis, and the proxy type on the y axis. 

Next, the user can opt to upload a larger dataset and run the code for creating a CSV table. This table contains information regarding the archive type, proxy type, age, location and resolution. The information contained in this table is then used to create temporal and spatial graphs. 

The temporal graph displays the temporal extent of each LiPD file, sorted by latitude and colour cocded based on archive type. The user is able to modify the age ranges they wish to be displayed in this graph. 

The spatial map displays the locations of each site referenced in the LiPD dataset, colour coded by archive type. The The user is able to modify the map extent they wish to have displayed. 

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
There were ... tests written. These are available in RunTests.py
- 
- 
-

### Limitations / Future Improvments	
- It would have been ideal to be able to drop duplicate time series based on DOI (kernel 8 of GraphMaker.ipynb) but had to use the co-ordinates instead - still not sure why it wasn't working. 
- There is an existing function from the `LiPD` package that allows you to convert LiPDs into CSV files but was not working on my platform - it would have been great to be able to use it or modify it to get the table produced in my code, instead of having to do it manually.
- Although this packages aims for standardization of paleoclimate data, some scientists use different keys for the same measurements (e.g. 'd18O' vs 'd18O' vs 'd18Oforam' etc) which makes it difficult to sort through large datasets. Some common errors have been handled in my code, but it is not exhaustive and will need to be tweaked.
- I was not able to follow through with the original plan (preparing 3 notebooks to be used as tutorials) as the second notebook took me too much long to complete, so I made my project smaller. Having a third notebook that goes through data analysis methods would have been great. 
- 
