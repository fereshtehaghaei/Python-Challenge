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

# Output text file (file name, 'w':write to file)
with open("Analysis/Election_Results.txt", 'w') as text:
    text.write("======================================\n")
    text.write("      Election Results " + "\n")
    text.write("======================================\n\n")
    text.write(f'Total Votes: {total_votes}' + "\n\n")
    text.write("--------------------------------------\n")
    for candidate, candidates_votes in candidates_dictionary.items():
        vote_percentage = (round(candidates_votes/total_votes*100,2))
        if candidates_votes > max_vote:
           max_vote = candidates_votes
           candidates = candidate
           winner_candidate.append(candidate)
        text.write(candidate + ':    ' + str(vote_percentage) + '%   ' + ' ('+str(candidates_votes)+') '"\n")
    text.write("======================================\n")
    text.write(f'        Winner:   {candidates}' "\n")
    text.write("======================================\n")