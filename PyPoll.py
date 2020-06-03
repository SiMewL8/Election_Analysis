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

# Initialize total vote counter
total_votes = 0

# candidate options list
candidate_options = []

# dictionary to keep track of candidates votes
candidate_votes = {}

# tracking winning candidate, vote count and percentage.
winnig_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the elecion results and read the file
with open(file_to_load) as clrd_election_data:
    # read the file object with csv.reader functions
    file_reader = csv.reader(clrd_election_data)

    # read the header row and skip it
    headers = next(file_reader)

    # print each row in csv file
    # using loops to iterate each row to count total votes, unique names, and unique count
    for row in file_reader:
        # adds the total vote count
        total_votes += 1

        # evaluates candidates from correct coloumn
        candidate_name = row[2]

        # if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            
            # adds the name to the list of candidates
            candidate_options.append(candidate_name)

            # setting each unique vote count to zero for each candidate
            candidate_votes[candidate_name] = 0

        # adding vote to a unique candidate by increments
        candidate_votes[candidate_name] += 1

# use open function to write data with 'w' on file and save results
with open(saved_file, "w") as textcomp_file:
    
    #print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------------\n")
    print(election_results, end="")
    
    # save the final vote count to the text file.
    textcomp_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print the candidate name, vote count and percentage of votes in terminal.
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Save it in text file.
        textcomp_file.write(candidate_results)


        # Determine winning vote count, percentage, and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # if  true will set them equal to each other
            winning_count = votes

            winning_candidate = candidate
            
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"----------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------------\n")
        
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    textcomp_file.write(winning_candidate_summary)





