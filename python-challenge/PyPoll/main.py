import os
import csv

#Create the CSV path
budget_csv = os.path.join("Resources", "election_data.csv")

#Declaring varibles
total_votes = 0 
khan_votes = 0
correy_votes = 0
otooley_votes= 0
li_votes= 0

#List of candidates
candidates = ["Khan", "Correy", "Li","O'Tooley"]

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        #Get total number of votes
        total_votes = total_votes + 1

        #If statment to get the total votes per candidate
        if row[2] == "Khan": 
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li": 
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

#Percentage of votes
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#Finding the candidate with the most votes
votes = [khan_votes, correy_votes, li_votes, otooley_votes]
candidate_votes = dict(zip(candidates,votes))
winner = max(zip(candidate_votes.values(),candidate_votes.keys())) 


# # Print the summary table
# print(f"Election Results")
# print(f"----------------------------")
# print(f"Total Votes: {total_votes}")
# print(f"----------------------------")
# print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
# print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
# print(f"Li: {li_percent:.3f}% ({li_votes})")
# print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
# print(f"----------------------------")
# print(f"Winner: {winner}")
# print(f"----------------------------")

# Output 
output_file = os.path.join("Election_Results.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

#Write rows in csv
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Khan: {khan_percent:.3f}% ({khan_votes})"])
    writer.writerow([f"Correy: {correy_percent:.3f}% ({correy_votes})"])
    writer.writerow([f"Li: {li_percent:.3f}% ({li_votes})"])
    writer.writerow([f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["----------------------------"])