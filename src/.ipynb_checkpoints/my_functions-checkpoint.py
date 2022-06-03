"""

##Introduction to my_functions.py

Welcome to my_functions.py! This module contains the functions that are needed to run GraphMaker.ipynb - a notebook for ...

The documentation in this notebook follow the below format: 

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


def make_plot(data):
    """ This function contains the code needed to graph the time series contained in a LiPD file 
    Parameters: 
    - data (dict): the LiPD file data

    Returns
    - plt.show(): The plot   
    """
    #Define variables
    year = data['age'] #note: these may also be saved as 'year' in certain files 
    values = np.sort(data['paleoData_values'])

    #Make the figure
    plt.plot(year,values)
    plt.title("Name: "+data['dataSetName']+", archive: "+data['archiveType'])
    plt.xlabel(data['ageUnits']) #Note! These may also be saved as 'yearUnits' in certain files 
    plt.ylabel(data['paleoData_variableName'])
    plt.gca().invert_xaxis() # Here, I have inverted the x-axis. This is just a preference and is optional.
    #plt.gca().invert_yaxis() # Here, I have inverted the y-axis. This is just a preference and is optional.

    return plt.show()



def final_plot(data):
    """ This function filters the plots returned by make_plot(data) 
    Parameters: 
    - data (dict): the LiPD file data
    
    Returns
    -  make_plot(data) (function)
    """
    for data in ts:
        if any (x in data["paleoData_variableName"] for x in {"age","depth","year"}): #removing these as they are not useful in this case
            continue 
        else:
            figure(figsize=(5, 10))
            make_plot(data)
            
def make_table(data):
    """ This function contains the code needed to tabulate the information contained in the LiPD dataset 
    Parameters: 
    - data (dict): the LiPD file data

    Returns
    - return pd.read_table('data2.csv', sep=',', index_col=0) : the table   
    """
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


            if "age" in item: #minimum and maximum ages 
                min_age = min(map(float,item["age"]))
                max_age = max(map(float,item["age"]))
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
    # Convert archive type to a number (used for coloring).
    # Deal with duplicates, e.g. 'Lake Sediment' = 'lake sediment' = 'LakeSediment' = 1
    for i, item in enumerate(archive_types):
        if archive_type.lower().replace(" ","") == item.lower().replace(" ",""):
            return i
        
    # Special case
    if archive_type.lower().replace(" ","") == "treering":
        return archive_types.index("Tree")
    raise ValueError(f"Unkown archive type: {archive_type}")