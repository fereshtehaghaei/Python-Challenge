#import library
import os
import csv

#joining path
budget_data = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as budget:
    budget_reader = csv.reader(budget, delimiter=",")
    budget_header = next(budget)
    # skip header row
    print(f"Header: {budget_header}")   
   
    # # # #  Analyzing Records  # # # #  

    #Initialize variables & Create and empty list for Date
    date=[]
    
    # Finding Net Profit/losses and create an empty list
    profit_loss = []
    total_profit_Loss = 0

    # Initialize the variables for Average Changes in Profit/losses 
  

    # Loop & Read through each row
    for rows in budget_reader:

    # Calculating Total number of months & adding count of months to months[] empty list
      date.append(rows[0])
      months_total = len(date)
      
    # Calculating the net Total amount of "Profit/Losses"
      profit_loss.append(int(rows[1]))
      total_profit_Loss = int(sum(profit_loss))
      

  

  # Calculating Average of changes in Profit/Losses over the entire period

  # print out the Results
    print("Financial Analysis")

    print("-----------------------------------------------------------------------")

    print(f'Total Months: {months_total}')
    print(f'Total Profit_Loss: {total_profit_Loss}')


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
