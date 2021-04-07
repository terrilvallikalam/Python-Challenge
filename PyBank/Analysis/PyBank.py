import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Define the function and have it accept 'bank_data' as its only parameter
def budget(bank_data):
    #Assign values to variables with descriptors
    date = str(bank_data[0])
    pl = int(bank_data[1])

    # Total number of months included in the dataset
    total_months = len(date)

    # The net total amount of Profit/Losses over the entire period
    total_amount = sum(pl)

    # The average of the changes in Profit/Losses over the entire period
    average = total_amount / total_months

    # The greatest increase in profits over the entire period
    greatest_increase = max(pl)

    # The greatest decrease in profits over the entire period
    greatest_decrease = min(pl)



# Total number of months included in the dataset
#def total_months(bank_data):
 #   months = int(bank_data[1])
  #  total_months = len(months)

# The net total amount of Profit/Losses over the entire period
#def net_total(bank_data):
 #   total = int(bank_data[1])
  #  sum = sum(total)

# The average of the changes in Profit/Losses over the entire period
#def average_of_changes(bank_data):
    
# The greatest increase in profits over the entire period
#def greatest_increase(bank_data):
 #   increases = int(bank_data[2])
  #  increase = max(increases)
    

# The greatest decrease in losses over the entire period
#def greatest_decrease(bank_data):
 #   decreases =int(bank_data[2])
  #  smallest_number = min(decreases)

# Print out results
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_amount}")
print(f"Average: {average}")
print(f"Greatest Increase In Profits: {greatest_increase}")
print(f"Greatest Decrease In Profits: {greatest_decrease}")