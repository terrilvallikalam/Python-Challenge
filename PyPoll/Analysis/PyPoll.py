import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Create a list and define variables
count = 0
total_canidates = []
name = []
voter_count = []
voter_percent = []
total_votes = 0

# Read in the CSV file
with open(election_csv, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Count
    for row in csvreader:
        count = count + 1
        total_canidates.append(row[2])
    for i in set(total_canidates):
        name.append(i)
        votes = total_canidates.count(i)
        voter_count.append(votes)
    # Percent
        percent = (votes/count)*100
        voter_percent.append(percent)
# Winner
winning = max(voter_count)
winner = name[voter_count.index(winning)]

# Print Results
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {count}")
print("-----------------------------------")
for i in range(len(name)):
             print(f"{name[i]}: {round(voter_percent[i],2)}00% ({str(voter_count[i])})")
print("-----------------------------------")
print(f"The winner is: {winner}")
print("-----------------------------------")

# Print Results to Text
with open ('PyPollAnalysis.txt', 'w') as text:
    text.write("Election Results")
    text.write("-----------------------------------")
    text.write(f"Total Votes: {count}")
    text.write("-----------------------------------")
    for i in range(len(name)):
                text.write(f"{name[i]}: {round(voter_percent[i],2)}00% ({str(voter_count[i])})")
    text.write("-----------------------------------")
    text.write(f"The winner is: {winner}")
    text.write("-----------------------------------")  
