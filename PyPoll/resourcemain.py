
import os
import csv


# Set the path for the CSV file in PyPollcsv

PyPollcsv = os.path.join("Resources","election_data.csv")

# Initialize the variables and Create the empty lists for Candidates and their votes.
candidates = []
num_votes = []
vote_percent = []
winner_list = []
total_votes = 0
#Creates the dictionary to be used for candidate name and vote count.
cadidate_dic = {}


# Open the CSV using the set path PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
  

    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] in cadidate_dic.keys():
            cadidate_dic[row[2]] = cadidate_dic[row[2]] + 1
        else:
            cadidate_dic[row[2]] = 1
 
    # test print(cadidate_dic) here
    #print (cadidate_dic)
#takes dictionary keys and values and set them into the Candidate list and num_votes list 

for key, value in cadidate_dic.items():
    candidates.append(key)
    num_votes.append(value)


for n in num_votes:
    vote_percent.append(round(n/total_votes*100,3))
    

# creat final tuples (unchangeable) for my lists.
final_list = list(zip(candidates, num_votes, vote_percent))



for name in final_list:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]



print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------")
for entry in final_list:
            print(entry[0] + ": " + str(entry[2]) +"% (" + str(entry[1])+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    for entry in final_list:
        text.write(entry[0] + ": " + str(entry[2]) +"% (" + str(entry[1]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("---------------------------------------\n")
