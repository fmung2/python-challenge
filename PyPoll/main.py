# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv
	
def cand_list(lst): #Gets Distinct List of Canditates Participating From 
    words = []
    for word in lst:
        if word not in words:
           words.append(word)
    return words
	
def result_list(cl): #Creates List Within List so each Candidate can have row with name, count and percentage columns
    mat = []
    for i in range(len(cl)):
        mat.append([])
        for j in range(0,1):
            mat[i].append(cl[i])
    return mat

def result_count(rl, cl): #Appends the count column with the total number of votes each candidate gets
    mat = rl
    for i in range(len(rl)): 
        rl[i].append(cl.count(rl[i][0]))
    return mat
	
def result_percentage(rl, vl):  #Appends the percentage column with the total number of votes each candidate gets
    mat = rl
    for i in range(len(rl)): 
        rl[i].append(round(rl[i][1]/len(vl) * 100 ,0))
    return rl
	
	
def result_winner(rc): # Creates a list that will return the winner of the election based on the max count column
    winner = rc[0]
    for word in rc:
        if word[1] > winner[1]:
           winner = word
    return winner

def result_print(rp): # Prints the list within the lists to show the name, count and percentage
    for word in rp:
        print(str(word[0]) + ": " + str(word[2]) + "%" + " (" + str(word[1]) + ")\n")
		
def result_write(rp, fl): # Writes to file the list within the lists to show the name, count and percentage
    for word in rp:
        fl.write(str(word[0]) + ": " + str(word[2]) + "%" + " (" + str(word[1]) + ")\n")
	
County_List = [] 
Voter_List = []
Candidate_List = []
csvpath = os.path.join('..','PyPoll', 'election_data_1.csv')
csvpath2 = os.path.join('..','PyPoll', 'election_data_2.csv')


with open(csvpath, newline='') as csvfile:
    next(csvfile, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        Voter_List.append(row[0])
		
with open(csvpath, newline='') as csvfile2:
    next(csvfile2, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader2 = csv.reader(csvfile2, delimiter=',')

    #print(csvreader2)
    #  Each row is read as a row
	
    for row in csvreader2:
        Candidate_List.append(row[2])
				
		
with open(csvpath2, newline='') as csvfile3:
    next(csvfile3, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader3 = csv.reader(csvfile3, delimiter=',')

    #print(csvreader3)

    #  Each row is read as a row
    for row in csvreader3:
        Voter_List.append(row[0])

with open(csvpath2, newline='') as csvfile4:
    next(csvfile4, None)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader4 = csv.reader(csvfile4, delimiter=',')

    #print(csvreader4)

    #  Each row is read as a row
    for row in csvreader4:
        Candidate_List.append(row[2])		
		
print("Election Results\n")
print("\n")
print("--------------------" + "\n")
print("\n")
print("Total Votes: " + str(len(Voter_List)) + "\n")
print("\n")
print("--------------------" + "\n")
print("\n")
result_print(result_percentage(result_count(result_list(cand_list(Candidate_List)),Candidate_List ),Voter_List ))
print("\n")
print("--------------------" + "\n")
print("\n")
print("Winner: " + str((result_winner(result_count(result_list(cand_list(Candidate_List)),Candidate_List )))[0]))
f = open('PyPoll.txt','w')
f.write("Election Results\n")
f.write("\n")
f.write("--------------------" + "\n")
f.write("\n")
f.write("Total Votes: " + str(len(Voter_List)) + "\n")
f.write("\n")
f.write("--------------------" + "\n")
f.write("\n")
result_write(result_percentage(result_count(result_list(cand_list(Candidate_List)),Candidate_List ),Voter_List ), f)
f.write("\n")
f.write("--------------------" + "\n")
f.write("\n")
f.write("Winner: " + str((result_winner(result_count(result_list(cand_list(Candidate_List)),Candidate_List )))[0]))
f.close()
