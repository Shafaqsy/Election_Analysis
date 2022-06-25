#1. The data we need to retreive.
#2. add the total number of vote cast.
#3. a complete list of candidates who received votes.
#4. the percentage of votes each candidte won.
#5.the total number of votes each candidate won.
#6. the winner of the election based on popular vote.

#import the csv and os module
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('resources/election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
      # Read and print the header row.
    headers = next(file_reader)
      # Print each row in the CSV file.
    for row in file_reader:
        
         # 2. Add to the total vote count.
        total_votes += 1
         # Print the candidate name from each row.
        candidate_name = row[2]

  # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

   # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

  # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
