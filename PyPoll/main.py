import os
import csv

PyPoll_csv = os.path.join("Resources","election_data.csv")

candidate_list = []
actual_candidate = []
vote_count = []
vote_percent = []
count = 0


with open(PyPoll_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        count = count + 1
        candidate_list.append(row[2])

    for x in set(candidate_list):
        actual_candidate.append(x)

        y = candidate_list.count(x)
        vote_count.append(y)

        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = actual_candidate[vote_count.index(winning_vote_count)]
    
 
print("Election Results")   
print("Total Votes :" + str(count))    
for i in range(len(actual_candidate)):
            print(actual_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("The winner is: " + winner)


with open('main.py.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(count) + "\n")
    for i in range(len(set(actual_candidate))):
        text.write(actual_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("The winner is: " + winner + "\n")