import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Total number of months included in the dataset
def total_months(bank_data):
    months = int(bank_data[1])
    Sum = sum(months)

# The net total amount of Profit/Losses over the entire period
def net_total(bank_data):
    total = int(bank_data[2])
    Sum = sum(total)

# The average of the changes in Profit/Losses over the entire period
def average_of_changes(bank_data):
    
# The greatest increase in profits over the entire period
def greatest_increase(bank_data):
    increases = int(bank_data[2])
    largest_number = max(increases)

# The greatest decrease in losses over the entire period
def greatest_decrease(bank_data):
    decreases =int(bank_data[2])
    smallest_number = min(decreases)

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)