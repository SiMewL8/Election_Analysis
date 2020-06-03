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

# Open the elecion results and read the file
with open(file_to_load) as clrd_election_data:

    # to do: read ana analyze the data here
    
    # read the file object with csv.reader functions
    file_reader = csv.reader(clrd_election_data)

    # printing the header row
    headers = next(file_reader)
    print(headers)






















# use open function to write data with 'w' on file
with open(saved_file, "w") as write_file:

    #write data onto file
    write_file.write("Counties in the Election")
    write_file.write("\n-------------------------\n")
    write_file.write("Arapahoe\nJefferson\nDenver")


