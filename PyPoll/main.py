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
    max_vote = 0
    winner_candidate=[]

    # Creating a dictionary for cadiates
    candidates_dictionary = {}  #candidate name = key, you have to make a mark
    
    # Loop & read through each row
    for candidates in election_reader:
        
    # calculating The total number of votes cast
        votes.append(candidates[0])
        total_votes +=1
        candidate = (candidates[2])  #assigning candidate column 

    # Calculating a complete list of candidates who received votes
        if candidate in candidates_dictionary:
          candidates_dictionary[candidate]+=1   # creating a count in dictionary since we have none
        else:
          candidates_dictionary[candidate]= 1 # candidate in dictionary
        # test print dictionary
    # print(candidates_dictionary)

# print out Eelction Results
print("**************************************")
print("     Election Results ")
print("======================================")
print(f'Total Votes: {total_votes}')
print("======================================")

# Created a For loop to iterate through dictionary and print each key
for candidate, candidates_votes in candidates_dictionary.items():

    # Calculating The percentage of votes each candidate won
    vote_percentage = (round(candidates_votes/total_votes*100,2))

    # finding the winner of the election based on popular vote.
    if candidates_votes > max_vote:
       max_vote = candidates_votes
       candidates = candidate
       winner_candidate.append(candidate)
    print(candidate + ':  ' + str(vote_percentage) + '% ' + ' ('+str(candidates_votes)+')')

print("======================================")
print(f'Winner:   {candidates}')
print("======================================")
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