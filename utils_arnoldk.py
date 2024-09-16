''' ITERATION 5 CORRECTED

Module: Alpha Analytics - Reusable Module for My Data Analytics Projects

In this iteration we are going to update out byline reflect descriptive statistical measures of the client_satisfaction_scores
variable. It is the only list in our code that contain a numerical list.

Process:
Include the previously declared variables assigned statistical measure values to the fstring of the byline.
'''
#####################################
# Import Modules at the Top
#####################################

#In Python, we can import modules to add extra tools and functions.
#Below, we are importing:
#-'statistics module':This gives us tools to calculate important statistical measures.

import statistics

#####################################
# Declare a global variable-Keeping the byline at the end.
#We will use this information in a smarter byline
#####################################

#Boolean variables to indicate if the company has international clients.
has_international_client:bool = True

#Integer variable to determine the number of years in operation.
years_in_operation:int = 10

#List of strings representing the skills offered by the company
skills_offered:list = ["Data Analysis","Machine Learning","Business Intelligence"]

#List of floats representing individual client satisfaction
client_satisfaction_scores:list = [4.8,4.6,4.9,5.0,4.7]

#List representing experience of our 6 employees(analysts) 
employee_experience_years:list = [10,15,11,13,7,9]

#####################################
# Calculate Basic statistics
#   Do this BEFORE we declare a byline.
#   So the values have been calculated
#   and ready for use in the byline.
#####################################

min_score:float = min(client_satisfaction_scores)
max_score:float = max(client_satisfaction_scores)
mean_score:float = statistics.mean(client_satisfaction_scores)
stdev_score:float = statistics.stdev(client_satisfaction_scores)
min_experience:float = min(employee_experience_years)
max_experience:float = max(employee_experience_years)
mean_experience:float = statistics.mean(employee_experience_years)
stdev_experience:float = statistics.stdev(employee_experience_years)


#####################################
# Declare a global variable named byline.
#Make it a multiline f-string to show our information.
#####################################

byline:str = f"""
------------------------------------------------------------
Alpha Analytics: Delivering Transforming Insights
------------------------------------------------------------
Has International Clients: {has_international_client}
years in Operation: {years_in_operation}
Skills Offered: {skills_offered}
Client satisfaction Score:{client_satisfaction_scores}
Maximum_Satisfaction_score:{max_score}
Minimum_Satisfaction_score:{min_score}
Average_Satisfaction_score:{mean_score}
Stdev_Satisfaction_score:{stdev_score}\n
Maximum_employee_experience:{max_experience}
Minimum_employee_experience:{min_experience}
Average_employee_experience:{mean_experience}
Stdev_employee_experience:{stdev_experience}
"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline()-> str:
    '''Return a byline for my analytics projects.'''
    return byline 

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())
    
    # Call main function if this script is executed directly
if __name__ == '__main__':
    main()
