#import library
import os
import csv

#joining path
budget_data = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvbudget:
    budget_reader = csv.reader(csvbudget, delimiter=",")
    budget_header = next(csvbudget)
    
    # skip header row
    # print(f"Header: {budget_header}")   
   
    #*#*#*#*#*#*#*#* Analyzing Records Begin *#*#*#*#*#*#*#*#* 
    #Initialize variables & Create and empty list [] for Date
    months=[]
    months_total =0
    
    # Create empty lists to iterate through specific rows for the following variables
    profit_loss = []
    monthly_profit_change = []
    # Loop & Read through each row in stored file
    for rows in budget_reader:

      # Calculating Total number of months & adding count of months to months[] empty list
      months.append(rows[0])
      months_total += 1
      
      # Calculating Total amount of "Profit/Losses" & Adding to profit_losst[] empty list
      profit_loss.append(int(rows[1]))
      total_profit_Loss = int(sum(profit_loss))
      total_profit_Loss = "${:.0f}".format(total_profit_Loss) # Formatting $ sign in to total and 0 decimal points

    # Iterate through the profit_loss list in order to get the monthly change in profits
    for pf in range(len(profit_loss)-1):

        # Calculating the diffrence between two months and append to monthly_profit_change [] empty list
        monthly_profit_change.append(profit_loss[pf+1]-profit_loss[pf])
        average_monthly_change = sum(monthly_profit_change) / len(monthly_profit_change)
        average_monthly_change = "${:.2f}".format(average_monthly_change) # Formatting $ sign in to total and 2 decimal points
          
# Obtaining The greatest increase in profits (date and amount) over the entire period
greatest_increase_profit = max(monthly_profit_change)

# I used the +1 at the end since month associated with change is the + 1 month or next month
greatest_increase_date = months[monthly_profit_change.index(greatest_increase_profit)+1]

# Obtaining The greatest decrease in losses (date and amount) over the entire period
greatest_decrease_loss = min(monthly_profit_change)

# I used the +1 at the end since month associated with change is the + 1 month or next month
greatest_decrease_date = months[monthly_profit_change.index(greatest_decrease_loss)+1]

# print out the Results for Financial Analysis
print("--------------------------------------")
print("     Financial Analysis:")
print("--------------------------------------")
print(f'Total Months: {months_total}')
print(f'Total Profit_Loss: {total_profit_Loss}')
print(f'Average Change: {average_monthly_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profit})')
print(f'Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_loss})')

# Output text file (file name, 'w':write to file)
with open("Financial_Analysis_Summary.txt", 'w') as text:
    text.write("-----------------------------------------------------------\n") # \n next line
    text.write("  Financial Analysis:"+ "\n")
    text.write("-----------------------------------------------------------\n\n")
    text.write(f'       Total Months: {months_total}'+ "\n")
    text.write(f'       Total Profit_Loss: {total_profit_Loss}'+ "\n")
    text.write(f'       Average Change: {average_monthly_change}' +"\n")
    text.write(f'       Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profit})'+ "\n")
    text.write(f'       Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_loss})'+ "\n\n")
    text.write("-----------------------------------------------------------\n\n")