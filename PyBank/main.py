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
   
    #*#*#*#*#*#*#*#* Analyzing Records Formulas Begin *#*#*#*#*#*#*#*#*

    #Initialize variables & Create and empty list for Date
    date=[]
    months_total =0
    
    # Finding Net Profit/losses and create an empty list
    profit_loss = []
    total_profit_Loss = 0

    # Initialize the variables for Average Changes in Profit/losses 
    monthly_change = []
    initial_profit_loss = 0
    final_profit_loss = 0
    total_monthly_changes =0
    average_change = 0

    # Loop & Read through each row
    for rows in budget_reader:

      # Calculating Total number of months & adding count of months to months[] empty list
      date.append(rows[0])
      months_total += 1
      
      # Calculating Total amount of "Profit/Losses" & Adding to profit_losst[] empty list & Formatting $ sign in to total
      profit_loss.append(int(rows[1]))
      total_profit_Loss = int(sum(profit_loss))
      total_profit_Loss = "${:.0f}".format(total_profit_Loss)   

      # Calculating Average of changes in Profit/Losses from month to month
      final_profit_loss = int(rows[1])
      monthly_change_profit_loss = final_profit_loss - initial_profit_loss
      
      # Add monthly_change for profit/loss inside monthly_change[] empty list  
      monthly_change.append(monthly_change_profit_loss)
      
      # Calcuating Average Change for entire period
      total_monthly_changes = total_monthly_changes + monthly_change_profit_loss 
      initial_profit_loss = final_profit_loss   
      average_change = (total_monthly_changes / months_total)
    
    # print out the Results for Financial Analysis
    print("Financial Analysis")
    print("-----------------------------------------------------------------------")
    print(f'Total Months: {months_total}')
    print(f'Total Profit_Loss: {total_profit_Loss}')
    print(f'Average Change: {average_change}')


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
