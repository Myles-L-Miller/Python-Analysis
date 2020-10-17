#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.


import os
import csv

#Link File
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Assign starting values
VoteCount=0
Winner=""
CandidateArray=[]
TallyArray=[]
PercentArray=[]

#Open and read csv, skip header
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header=next(csv_reader)

#Read through each row of data
    for row in csv_reader:
        VoteCount+=1
        if row[2]in CandidateArray:
            TallyArray[CandidateArray.index(row[2])]+=1
        else:
            CandidateArray.append(row[2])
            TallyArray.append(1)

#Get percentage of votes
for Tally in TallyArray:
    PercentArray.append(round(((Tally*100)/VoteCount),2))

#Find Winner
Winner=CandidateArray[TallyArray.index(max(TallyArray))]

#Print Results
print("Election Results \n-----------------------\n")
print(f"Total Votes: {VoteCount} \n-----------------------\n")
for i in range(len(CandidateArray)):
    print(f"{CandidateArray[i]}: {PercentArray[i]}% [{TallyArray[i]}]\n")
print("\n-----------------------\n")
print(f"Winner: {Winner}\n")
print("-----------------------")

#Convert to Text File
results=open("PyPoll/Analysis/Results.txt","w")
results.write("Election Results \n-----------------------\n")
results.write(f"Total Votes: {VoteCount} \n-----------------------\n")
for i in range(len(CandidateArray)):
    results.write(f"{CandidateArray[i]}: {PercentArray[i]}% [{TallyArray[i]}]\n")
results.write("\n-----------------------\n")
results.write(f"Winner: {Winner}\n")
results.write("-----------------------")
