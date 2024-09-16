'''This Python module retrieves data from the web, processes it, and writes the results to different file formats.
Various python collections are employed in this module.
'''
#Standard Library imports
import csv
from io import StringIO
import json
import pathlib
import statistics

#External library imports (Virtual Environment must be active)
import requests
import openpyxl
import pandas

#Local module imports
import utils_arnoldk
import arnoldatchoe_projectsetup

#Define current project path
project_path = pathlib.Path.cwd()

#Create sub-directory in project_path to hold files
data_path = project_path.joinpath('data')
data_path.mkdir(exist_ok = True)

############
#Define Functions
############
def save_text(filename,url):
    file_path = data_path.joinpath(f"{filename}")
    with file_path.open('w') as file:
        file.write(url)
        print(f"Text data saved to {file_path}")

def save_json(filename,url):
    file_path = data_path.joinpath(f"{filename}")
    with file_path.open ('w') as file:
        json.dump(url)
        print(f"JSON data saved to {file_path}")

def save_excel(filename,url):
    file_path = data_path.joinpath(f"{filename}")
    df = pandas.DataFrame(url)
    file_path.df.to_excel(index = False, engine = 'openpyxl')
    print(f"Excel data saved to {file_path}")

def save_csv(filename,url):
    file_path = data_path.joinpath(f"{filename}")
    df = pandas.read_csv(StringIO(url))
    file_path.df.to_csv(index= False)
    print(f"CSV data saved to {file_path}")

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        save_text
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        save_json
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        save_excel
    else:
        print(f"Failed to fetch excel data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        save_csv
    else:
        print(f"Failed to fetch csv data: {response.status_code}")

def process_text_data(folder_name,filename,processed_filename):
    file_path = pathlib.Path(folder_name) / filename
    processed_file_path = pathlib.Path(folder_name) / processed_filename

    try:
        with open(file_path,'w') as file:
            text_file = file.read()

            words = text_file.split()
            unique_words = set(words)
            unique_words_count = len(unique_words)
            words_count = len(words)

        with open(processed_file_path,'w') as file:
            file.write(f"We have {words_count} words")
            file.write(f"We have {unique_words_count} unique words")
    except Exception as e:
        print(" Text file was not processed")

def process_csv_data(folder_name,filename,processed_filename):
    file_path = pathlib.Path(folder_name) / filename
    processed_file_path = pathlib.Path(folder_name)/ processed_filename
#Read csv file
    try:
        df = pandas.read_csv(file_path)
    except FileNotFoundError:
        print(f"{file_path} was not found")
    except pandas.errors.EmptyDataError:
        print(f"{file_path} is empty")
    except pandas.errors.ParserError:
        print(f"{file_path} could not be parsed")

#Basic file content information
    df = pandas.read_csv(file_path)
    num_rows, num_columns = df.shape
    column_names = df.columns.tolist()

    summary ={
        'Number of Rows': num_rows,
        'Number of Columns':num_columns,
        'Column Names':column_names
    }

    Stats = {}
    df = pandas.read_csv(file_path)
    for column in df.columns:
        if pandas.api.types.is_numeric_dtype(df[column]):
            Stats[column] = {
                'Mean':df[column].mean(),
                'Median': df[column].median(),
                'Standard deviation': df[column].std(),
                'Maximum': df[column].max(),
                'Minimum': df[column].min()
            }
        elif pandas.api.types.is_object_dtype(df[column]):
            Stats[column] = {
                'Unique Values': df[column].nunique(),
                'Top Value': df[column].mode() [0],
            }
            return summary
            return Stats
    with open(processed_file_path,'w') as file:
            file.write(f"{summary}")
            file.write(f"{Stats}")

def process_excel_data(folder_name, filename, processed_filename):
    """Extract and analyze data from an Excel file and save insights to a text file.

    Args:
        folder_name (str): The folder where the Excel files are located.
        filename (str): The name of the input Excel file.
        processed_filename (str): The name of the file where processed insights will be saved.
    """
    # Create file paths
    file_path = pathlib.Path(folder_name) / filename
    processed_file_path = pathlib.Path(folder_name) / processed_filename

    # Read Excel file into a DataFrame
    try:
        df = pandas.read_excel(file_path)
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return

    # Initialize dictionary to store statistics
    statistics = {}

    # Calculate statistics
    try:
        for column in df.select_dtypes(include=['number']).columns:
            stats = {
                'mean': df[column].mean(),
                'median': df[column].median(),
                'sum': df[column].sum(),
                'count': df[column].count(),
                'std_dev': df[column].std(),
                'min': df[column].min(),
                'max': df[column].max()
            }
            statistics[column] = stats
    except Exception as e:
        print(f"Error processing statistics: {e}")
        return

    # Write statistics to the output file
    try:
        with open(processed_file_path, 'w', encoding='utf-8') as file:
            for column, stats in statistics.items():
                file.write(f"Statistics for column '{column}':\n")
                for stat_name, value in stats.items():
                    file.write(f"  {stat_name}: {value}\n")
                file.write("\n")
        print(f"Statistics have been written to {processed_file_path}")
    except Exception as e:
        print(f"Error writing to the file {processed_file_path}: {e}")



def process_json_data(folder_name, filename, processed_filename):
    file_path = pathlib.Path(folder_name) / filename
    processed_file_path = pathlib.Path(folder_name) / processed_filename

    """Process JSON data and save a human-readable summary to a text file.

    Args:
        filename (str): The name of the input JSON file.
        processed_filename (str): The name of the file where the summary will be saved.
    """


    # Read JSON data from file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return

    # Prepare the summary
    def summarize_dict(d, indent=0):
        """Recursively summarize a dictionary."""
        summary_lines = []
        for key, value in d.items():
            if isinstance(value, dict):
                summary_lines.append(' ' * indent + f"{key}:")
                summary_lines.extend(summarize_dict(value, indent + 2))
            elif isinstance(value, list):
                summary_lines.append(' ' * indent + f"{key}:")
                for item in value:
                    if isinstance(item, dict):
                        summary_lines.extend(summarize_dict(item, indent + 2))
                    else:
                        summary_lines.append(' ' * (indent + 2) + str(item))
            else:
                summary_lines.append(' ' * indent + f"{key}: {value}")
        return summary_lines

    try:
        summary_lines = summarize_dict(data)
    except Exception as e:
        print(f"Error processing JSON data: {e}")
        return

    # Write summary to the output file
    try:
        with open(processed_filename, 'w', encoding='utf-8') as file:
            file.write("\n".join(summary_lines))
        print(f"Summary has been written to {processed_filename}")
    except Exception as e:
        print(f"Error writing to the file {processed_filename}: {e}")


def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Byline: {utils_arnoldk.byline}")

    txt_url = 'https://www.gutenberg.org/cache/epub/2600/pg2600-images.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = "https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls"
    
    json_url = "https://quickstats.nass.usda.gov/api/api_GET/?key=9223C2A1-8766-311D-97E0-9C0777807BCE&source_desc=SURVEY&commodity_desc=CHICKENS&short_desc=CHICKENS, (EXCL BROILERS) - SALES FOR SLAUGHTER, MEASURED IN $&doman_desc=TOTAL&agg_level_desc=NATIONAL"

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_text_data(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_data(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_data(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_data(json_folder_name,'data.json', 'results_json.txt')

if __name__ == '__main__':
    main()





    





