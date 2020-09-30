#import library
import os
import csv

#joining path
election_data = os.path.join("Resources", "election_data.csv")

# open and read csv
with open(election_data, newline="") as csv_election:
    election_reader = csv.reader(csv_election, delimiter=",")
    election_header = next(csv_election)

    # Initialize variable and create and empty list[] 
    votes =[]
    total_votes = 0
    candidates_votes =[]
  
    # Creating a dictionary for cadiates
    candidates_dictionary = {}
    #candidate name = key you have to make a mark

    # Loop & read through each row
    for candidates in election_reader:
        
    # calculating The total number of votes cast
        votes.append(candidates[0])
        total_votes = (len(votes))
        candidate = (candidates[2])

    # Calculating a complete list of candidates who received votes
        if candidate in candidates_dictionary:
          candidates_dictionary[candidate]+=1 # creating a count in dictionary since we have none
        else:
          candidates_dictionary[candidate]= 1 # candidate in dictionary
     #print(candidates_dictionary)
    final_list = list(zip(votes,candidates_votes))


        
    
# print out Eelction Results

print("     Election Results:")
print("--------------------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------------------")
for candidate, candidates_votes in candidates_dictionary.items():
    print(candidate + ':  ' + '('+str(candidates_votes)+')')




"""


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