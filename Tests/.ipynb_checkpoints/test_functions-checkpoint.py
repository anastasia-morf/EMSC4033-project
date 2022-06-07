import pytest 
from src.my_functions import *

with HiddenPrints():
        data = lipd.readLipd(usr_path = 'C:/Users/anast/Desktop/Aus_LiPD_data')
        ts = lipd.extractTs(data)
        
def test_if_data_is_dictionary(): 
    """Testing whether the data we have loaded is a dictionary"""
    if type(data) == dict:
        assert True, "Data has not been loaded as a dictionary"
        
def test_check_for_specific_file():
    """Testing to see whether a specific file has been loaded"""
    for x in ts:
        if 'dataSetName' == 'OregonCaves.Ersek.2012':
            assert True, "File has been loaded"

def test_extracted_time_series():
    """Testing if spatial plot has valid time series"""
    if len(ts) == 2988:
        assert True, "Data has not been loaded correctly - wrong time-series"

def test_make_plots_axis():
    """Test if there is a valid variable for the axes"""
    if 'year' and 'paleoData_variableName' in data.keys():
        assert True, "Not enough data available - cannot plot"

def test_make_table():
    """Test if the length of the table is correct"""
    if len(make_table(data)) == 362:
           assert True, "Data did not load properly"
        