## PyBank
import os
import csv

# Assigning the path since my CSV file is in a seprate folder called Resource folder
budgetpath = os.path.join('Resources', 'budget_data.csv')

# Now open the file 
with open(budgetpath,'r', newline ='') as budgetfile:

# Now Reading the file
    budgetreader =csv.reader(budgetfile, delimiter = ',')

# Read the header row 1st and then Converting current row into a list
    budgetheader = next(budgetreader)
    print(f'{budgetheader}')

    

""""  
The dataset is composed of two columns: `Date` and `Profit/Losses`

  * Create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset 

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""