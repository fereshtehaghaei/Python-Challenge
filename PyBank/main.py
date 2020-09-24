#import library
import os
import csv

#joining path
budget_data = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

   
   """Analyzing Records"""

    #Initialize variables & Create and empty list for Date
    months=[]
    months =0

    # Finding Net Profit/losses and create an empty list
    profit = []
    total_profit_losses = 0

    # Initialize the variables for Average Changes in Profit/losses 
    average_change_profit = 0

    # Loop & Read through each row
    for rows in budgetreader:

    # Calculating Total number of months
      months +=1

  # Add month count to Months[] list. It will be used for greatest incease and decrease.
      months.append(rows[0])
      'print(count)

# Calculating the net Total amount of "Profit/Losses"
      total_profit_losses = total_profit_losses + int(rows[1])
      profit.append(rows[1])
      'print(total_profit_losses)

# Calculating Average of changes in Profit/Losses over the entire period
average = total_profit_losses / count


    

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
