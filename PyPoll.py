# # Total number of votes cast
#     how to total count votes
# # A complete list of candidates who received votes
#     listing each candidate 
# # Total number of votes each candidate received
#     each candidate in all districts
# # Percentage of votes each candidate won
#     doing percentages with districts
# # The winner of the election based on popular vote
#     comparing the candidates, and printing a majority? winner

import csv
import os


# Assign a variable for the file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save file to a path
saved_file = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote counter
total_votes = 0

# Open the elecion results and read the file
with open(file_to_load) as clrd_election_data:
    # read the file object with csv.reader functions
    file_reader = csv.reader(clrd_election_data)

    # read the header row and skip it
    headers = next(file_reader)

    #print each row in csv file
    for row in file_reader:
        #2. adding to total vote count
        total_votes += 1

# 3. Printing total votes
print(total_votes)



















# use open function to write data with 'w' on file
with open(saved_file, "w") as write_file:

    #write data onto file
    write_file.write("Counties in the Election")
    write_file.write("\n-------------------------\n")
    write_file.write("Arapahoe\nJefferson\nDenver")


