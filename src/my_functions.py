"""

##Introduction to my_functions.py

Welcome to my_functions.py! This module contains the functions that are needed to run GraphMaker.ipynb

The documentation in this notebook follows the format below: 

def + The function name goes here ():
    " This is a docstring"
    The code goes here # This is a comment

The comment here will help us understand and edit the code, while docstrings will be helpful in explaining what the function does.

Additionally, docstrings are formatted in the following way: 

Description of the function 

Parameters
----------
     The variables listed inside the parentheses in the function definition

Returns
-------
    This is a description of what is returned.
    
"""

from src.dependencies import * 


class HiddenPrints:
    """Disable print statement. Found in: https://stackoverflow.com/questions/8391411/how-to-block-calls-to-print/8391926#8391926"""
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
    

def make_plot(data):
    """ This function contains the code needed to graph the time series contained in a LiPD file 
    Parameters: 
    - data (dict): the LiPD file data

    Returns
    - plt.show(): The plot   
    """
    #Define variables
    year = data['year'] 
    values = np.sort(data['paleoData_values'])

    #Make the figure
    plt.plot(year,values)
    plt.title("Name: "+data['dataSetName']+", archive: "+data['archiveType'])
    plt.xlabel(data['yearUnits']) 
    plt.ylabel(data['paleoData_variableName'])
    #plt.gca().invert_xaxis() # Here, I have inverted the x-axis. This is just a preference and is optional.
    #plt.gca().invert_yaxis() # Here, I have inverted the y-axis. This is just a preference and is optional.

    return plt.show()


def final_plot(data):
    """ This function filters the plots returned by make_plot(data) 
    Parameters: 
    - data (dict): the LiPD file data
    
    Returns
    -  make_plot(data) (function)
    """
    with HiddenPrints():
        ts = lipd.extractTs(data)
    for y in ts:
        if any (x in y["paleoData_variableName"] for x in {"age","depth","year"}): #removing these as they are not useful in this case
            continue 
        else:
            figure(figsize=(5, 10))
            make_plot(y)
            
            
def make_table(data):
    """ This function contains the code needed to tabulate the information contained in the LiPD dataset 
    Parameters: 
    - data (dict): the LiPD file data

    Returns
    - return pd.read_table: the table   
    """
    
    with HiddenPrints():
        ts = lipd.extractTs(data)
    header = ['Dataset Name', 'Archive Type', 'Proxy Type', 'Minimum Age', 'Maximum Age', 'Longitude', 'Latitude', 'Max Resolution', 'Min Resolution', ]
    with open('data2.csv', 'w', encoding='UTF8', newline="") as f:
        ana = csv.writer(f)
        ana.writerow(header)

        for item in ts: #naming the variable keys for table input   
            archiveType = item["archiveType"] #archive type = material used 
            name = item["dataSetName"]

            if any(x in item["paleoData_variableName"] for x in {"Snow accumulation water equivalent", "Negative Data Error", "Positive Age Uncertainty", "qualityCode","Negative Age Uncertainty", "Positive Data Error","age", "sedimentWeight", "waterContent", "depth", "label", "year","uncertainty", "uncertaintyHigh", "uncertaintyLow", "Commentregardingreliability1", "reliable", "sampleID", "Laminae"}):
                    continue #removing unwanted proxy types. Proxy types = what is measured 
            else: proxyType = item["paleoData_variableName"]

            if "year" in item: #minimum and maximum ages 
                min_age = min(map(float,item["year"]))
                max_age = max(map(float,item["year"]))
            else:
                min_age = ""
                max_age = ""

            geo_meanLon = item["geo_meanLon"] #location coordinates
            geo_meanLat = item["geo_meanLat"]

            if "paleoData_hasResolution_hasMaxValue" in item: #maximum resolution 
                resolution_max_value = item["paleoData_hasResolution_hasMaxValue"]
                if resolution_max_value == "nan":
                    resolution_max_value = ""
            else: 
                resolution_max_value = ""

            if "paleoData_hasResolution_hasMinValue" in item: #minimum resolution
                resolution_min_value = float(item["paleoData_hasResolution_hasMinValue"])
                if resolution_min_value == float("nan"):
                    resolution_min_value = ""
            else:
                resolution_min_value = ""

            data = [ #matching the variables defined above to the headers 
                name,
                archiveType,
                proxyType,
                min_age,
                max_age,
                geo_meanLon,
                geo_meanLat,
                resolution_max_value,
                resolution_min_value
            ]
            ana.writerow(data)
        return pd.read_table('data2.csv', sep=',', index_col=0)
    
    
    
    
def get_archive_num(archive_type): 
    """ This function deals with duplicate data and converts the archive type to a number (used for coloring).
    Parameters: 
    - archive_type (str): ... 
    
    Returns
    -  i : integer 
    """
    archive_types = ["Coral", "Lake Sediment", "Marine Sediment", "Tree", "Peat", "Sediment", "Leaf material", "Ostracod", "Foraminifera", "Speleothem"]
    # Convert archive type to a number (used for coloring).
    # Deal with duplicates, e.g. 'Lake Sediment' = 'lake sediment' = 'LakeSediment' = 1
    for i, item in enumerate(archive_types):
        if archive_type.lower().replace(" ","") == item.lower().replace(" ",""):
            return i
        
    # Special case
    if archive_type.lower().replace(" ","") == "treering":
        return archive_types.index("Tree")
    raise ValueError(f"Unkown archive type: {archive_type}")
    
    
def make_temporal_map(data):
    """ This function makes the temporal graph.
    Parameters: 
        - data (dict): the LiPD file data
    Returns
    -  matplotlib figure
    """
    data = pd.read_table('data2.csv', sep=',')
    data = data.drop_duplicates(subset=["Longitude", "Latitude"], keep="first") #This removes any duplicates (based on longitude and latitude)
    data = data.sort_values(["Latitude"]) #sorting the table by latitude - you can sort by any of the keys
    data = data.reset_index(drop = True)

    ax = plt.axes()
    plt.autoscale(True)
    ax.yaxis.set_major_locator(ticker.NullLocator())
    colors = plt.get_cmap('Set3').colors  # colours: https://matplotlib.org/stable/tutorials/colors/colormaps.html

    archive_types = ["Coral", "Lake Sediment", "Marine Sediment", "Tree", "Peat", "Sediment", "Leaf material", "Ostracod", "Foraminifera", "Speleothem"]

    for i in range(len(data)):
        x = [data["Minimum Age"].values[i], data["Maximum Age"].values[i]]
        y = [data["Dataset Name"].values[i] + str(i), data["Dataset Name"].values[i] + str(i)]
        archive_type = data["Archive Type"].values[i]
        if ((not numpy.isnan(x[0])) and (not numpy.isnan(x[1]))): 
            archive_type = data["Archive Type"].values[i]
        plt.plot(x, y, c=colors[get_archive_num(archive_type)], solid_capstyle='round')
        
    plt.xlim([0,2022]) #YOU CAN MODIFY THIS 


    #Make the figure
    plt.xlabel('year (CE)') 
    plt.ylabel('Latitude')
    patches = [mpatches.Patch(color=colors[get_archive_num(archive_type)], label=archive_type) for archive_type in archive_types]
    ax.legend(handles=patches, bbox_to_anchor=(1.09, 0.8), loc='upper left', borderaxespad=0)
    plt.title("Age Ranges for Archive Data")
    
    return plt.show()
    
    
def make_spatial_map(data):    
    """ This function makes the temporal graph.
    Parameters: 
        - data (dict): the LiPD file data
    Returns
    -  matplotlib figure
    """

    #Creating a map 
    ax = plt.axes(projection = ccrs.PlateCarree())
    plt.title('Distribution of Archive')
    ax.set_extent([100, 180, 10, -60], ccrs.PlateCarree()) # YOU CAN MODIFY THIS - This is for Australia

    archive_types = ["Coral", "Lake Sediment", "Marine Sediment", "Tree", "Peat", "Sediment", "Leaf material", "Ostracod", "Foraminifera", "Speleothem"]

    ax.coastlines(resolution='110m')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='gray', alpha=0.5, linestyle='--')
    #Changing Axes
    gl.top_labels = False
    gl.left_labels = False
    gl.xlines = True
    gl.xlabel_style = {'size': 20, 'color': 'gray'}
    gl.xlabel_style = {'color': 'blue', 'weight': 'bold'}

    #Adding Features
    ax.add_feature(cfeature.LAND, color="lightgrey", alpha=0.5)
    # ax.stock_img() #to make realistic

    colors = plt.get_cmap('Set3').colors

    #adding points
    df = pd.read_csv('data2.csv')
    print(len(df.index))

    point_cols = [colors[get_archive_num(archive_type)] for archive_type in df["Archive Type"]]

    plt.scatter(x=df.Longitude, y=df.Latitude,
                color=point_cols,
                s=10,
                alpha=1,
                transform=ccrs.PlateCarree())
    # print(len(df.index))

    # Create legend
    patches = [mpatches.Patch(color=colors[get_archive_num(archive_type)], label=archive_type) for archive_type in archive_types]
    ax.legend(handles=patches, bbox_to_anchor=(1.2, 0.15), loc='lower left', borderaxespad=0)

    return plt.show()