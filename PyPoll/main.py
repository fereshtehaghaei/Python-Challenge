#import library
import os
import csv

#joining path
election_data = os.path.join("Resources", "election_data.csv")

# open and read csv
with open(election_data, newline="") as csv_election:
    election_reader = csv.reader(csv_election, delimiter=",")
    election_header = next(csv_election)

    # Initialize variable and create and empty list[] for number of votes
    votes =[]
    total_votes = 0
    
    # Loop & read through each row
    for rows in election_reader:
        
    # calculating The total number of votes cast
        votes.append(rows[0])
        total_votes += 1

# print out Eelction Results
print("--------------------------------------")
print("     Election Results:")
print("--------------------------------------")
print(f'Total Votes: {total_votes}')





"""
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""