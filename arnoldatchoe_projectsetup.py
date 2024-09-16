'''This script or module provides the functionality of creating 
folders to organise our projects under various conditions. Conditions include;
1. Creating folders for a series of years.
2. Creating folders given a list. 
3. Creating folders given a range.
4. Creating folders periodically.
Note: The goal is to have a script that can be edited to fit various circumstances.
This script also contains functions we can call upon in other projects.
'''

##################
#We first import the needed python modules.
##################

#Import pathlib from python's standard library which has functions needed in this script
import pathlib as pl

#Import time from python's standard library which has functions needed in this script
import time

#Import os from python's standard library which has functions needed in this script
import os



#Import our local module or script
import utils_arnoldk

##################
#Declare global variables
##################

#Assign the current project path to a variable.
#This variable is used in the creation of project sub-directories
project_path = pl.Path.cwd()

###Create possible project sub-directories.

#Create a data path object if it does not exist.
data_path = project_path.joinpath('data')
data_path.mkdir(exist_ok=True)


##########################
#Define functions
##########################

##############
###Function 1 is used to create sub-directories for a range of years
##############

def create_folders_for_range(identifier:str,start_year:int,end_year:int)->None:
    '''
    Function Arguments
   1. identifier provides information on what type of data is contained in the folder.
   2. start_year --this is the beginning of the range of years.
   3. end_year--this is the ending of the range of years.
    Both start_year and end_year are inclusive.Note that +1 is include with the end_year in the range function below to make it 
    inclusive.
    '''
    for year in range(start_year,end_year+1):
        folder_name = f'{identifier}_{year}'
        year_path = data_path.joinpath(folder_name)
        year_path.mkdir(exist_ok = True)

        #Log the function call and its arguments using f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

##############
###Function 2 is used to create folders when given a list of names
##############

def create_folders_from_list(folder_list:list)->None:
    '''Function Argument
    1. Folder_list which is a list of names is the only argument for this function
     '''
    for name in folder_list:
         name_path = data_path.joinpath(name)
         name_path.mkdir(exist_ok=True)

         #Log the function call and its arguments using f-string
    print(f"FUNCTION CALLED: create_folder_from_list with {folder_list}")

##############
###Function 3 is used to create folders with prefixed names given a list of names and a specified prefix
##############

def create_prefixed_folders(folder_list,prefix:str)->None:
    '''Function Arguments'''
    for name in folder_list:
        folder_name = F'{prefix}-{name}'
        name_path = data_path.joinpath(folder_name)
        name_path.mkdir(exist_ok=True)
    print(f"FUNCTION CALLED: create_prefixed_folders with {folder_list} and {prefix}")

##############
###Function 4 is used to create folders periodically.
##############
def create_folders_periodically(duration_seconds:int, maximum_number_of_folders:int)->None:
    '''Function Arguments
    1. duration_seconds specifies the time interval in seconds between each folder creation.
     2. maximum_number_of_folders is used to limit how many folders are created. '''
    index = 0
    #the index variable servers as a counter to help in the iteration process.
    while index < maximum_number_of_folders:
            folder_name = F'folder_{index}'
            name_path = data_path.joinpath(folder_name)
            name_path.mkdir(exist_ok=True)
            time.sleep(duration_seconds)
            index += 1
    print(f"FUNCTION CALLED: create_folders_periodically with {duration_seconds} and {maximum_number_of_folders}")


##############
#Define main function
##############

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(utils_arnoldk.get_byline())
    # print(f"Byline: {case_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(identifier='financial statement',start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    maximum_number_of_folder:int = 10
    create_folders_periodically(duration_secs,maximum_number_of_folder)
 
    # Call function 2 to test the list of regions.
    regions= [ "North America", "South America",  "Europe",  "Asia", "Africa", "Oceania", "Middle East"]
    create_folders_from_list(regions)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()











