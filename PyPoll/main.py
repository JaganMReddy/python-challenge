import os
import csv

# declare vaiables to store the result needed 
total_votes = 0
contenders_votes = {}

# oepn the file
with open("C:\\Users\\HZ3903\\UTAUS201807DATA2\\homework-instructions\\03-Python-Instructions\\Instructions\\PyPoll\\Resources\\election_data.csv") as infile:
    reader = csv.reader(infile)  
    
    next(reader, None)  # skip the headers
    
    for row in reader:  # process each row of the input
        voter_id = row[0]
        county = row[1]
        contender = row[2]
        total_votes +=1
        if contender in contenders_votes :
           contenders_votes[contender] = contenders_votes[contender] + 1 
        else:
           contenders_votes[contender] = 1
    
#   Print the summary at the terminal

    print("Election Results")
    print("-----------------------------")
    print("Total Votes : " + str(total_votes))
    print("-----------------------------")

    for key,value in contenders_votes.items():
        print (str(key) + "\t" + ": " + str('{:,.3f}'.format(value * 100/total_votes) ) + " (" + str(value) + " )" )
    print("-----------------------------")
    for key,value in contenders_votes.items(): 
        print ("Winner: " + str(key)) 
        break
    print("-----------------------------")
    
#   open file       
    file = open("PyPoll_Output.txt", "a+")

#   write to the file
    file.write("Election Results" + "\n" )
    file.write("-----------------------------" + "\n")
    file.write("Total Votes : " + str(total_votes) + "\n")
    file.write("-----------------------------" + "\n")
    for key,value in contenders_votes.items():
        file.write(str(key) +  "\t" + ": " + str('{:,.3f}'.format(value * 100/total_votes) ) + " (" + str(value) + " )" + "\n")  
    file.write("-----------------------------")
    for key,value in contenders_votes.items(): 
        file.write("Winner: " + str(key) + "\n") 
        break
    file.write("-----------------------------")    
#   close the file      
    file.close()

