import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Create lists and define variables
date = []
profit = []
monthly_changes = []

month = 0
total_profit_difference = 0
initial = 0 
final = 0 
monthly_change_profits = 0
avg_change = 0
greatest_increase_date = 0 
greatest_increase = 0
greatest_decrease_date = 0
greatest_decrease = 0

# Read in the CSV file
with open(bank_csv, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Months
    for row in csvreader:
      month = month + 1
    # Total Profit
      profit.append(row[1])
      total_profit_difference = total_profit_difference + int(row[1])
    # Final Profit
      final = int(row[1])
      monthly_change_profits = final - initial
      monthly_changes.append(monthly_change_profits)
      total_profit_difference = total_profit_difference
      initial = final
    # Average Change
      avg_change = (total_profit_difference/monthly_change_profits)
      date.append(row[0])
    # Greatest Increase and Decrease in Profits
      greatest_increase = max(monthly_changes)
      greatest_increase_date = date[monthly_changes.index(greatest_increase)]

      greatest_decrease = min(monthly_changes)
      greatest_decrease_date = date[monthly_changes.index(greatest_decrease)]

# Print Out Results
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {month}")
print(f"Total: ${total_profit_difference}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase In Profits: {greatest_increase}")
print(f"Greatest Decrease In Profits: {greatest_decrease}")

# Print to Text
with open ('PyBankAnalysis.txt', 'w') as text:
  text.write("Financial Analysis")
  text.write("-----------------------------------")
  text.write(f"Total Months: {month}")
  text.write(f"Total: ${total_profit_difference}")
  text.write(f"Average Change: ${avg_change}")
  text.write(f"Greatest Increase In Profits: {greatest_increase}")
  text.write(f"Greatest Decrease In Profits: {greatest_decrease}")