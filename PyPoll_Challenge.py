# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = "Resources/election_results.csv"
# Add a variable to save the file to a path.
file_to_save = "analysis/Election_Analysis.txt"

# Initialize a total vote counter.
total_votes = 0

# Creating empty list and dictionary for county options and county votes casted 
county_options = []
county_votes_casted = {}

# Creating empty list and dictionary for candidate options and candidate votes. 
candidates_options = []
candidates_votes = {}

# Assign variables for tracking the county with largest turnout and its votes count
county_largest_turnout = ""
votes_count_largest = 0

# Assign variables for tracking the winning candidate, vote count, and percentage.
winning_candidate= ""
winning_candidate_vc = 0
winning_candidate_percent = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    header = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Get the county name from each row.
        name_of_county = row[1]
        # Get the candidate name from each row.
        name_of_candidate = row[2]
        # Add to the total vote count.
        total_votes+=1
        # If the county does not match any existing county, add the the county list.
        if name_of_county not in county_options: 
            county_options.append(name_of_county)
            county_votes_casted[name_of_county] = 0
        county_votes_casted[name_of_county] += 1
        # If the candidate does not match any existing candidate, add the the candidate list.
        if name_of_candidate not in candidates_options:
            candidates_options.append(name_of_candidate)
            # And begin tracking that candidate's voter count.
            candidates_votes[name_of_candidate] = 0
          # Add a vote to that candidate's count.
        candidates_votes[name_of_candidate] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (f"\nElection Results\n"
    "......................\n"
    f"Total Votes:{total_votes:,}\n"
    ".......................\n"
    f"County Votes:\n"
    )
    print(election_results)
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    for county in county_options:
         # Retrieve vote count and percentage.
        votes = county_votes_casted[county]
        percentage_votes = (float(votes)/total_votes)*100
        county_results = (
            f"{county}:"
            f"{percentage_votes:.1f}% ({votes:,}) \n")
        # Print county results to the terminal.
        print(county_results)
        # Save county results to the text file
        txt_file.write(county_results)

        if votes> votes_count_largest:
             # Retrieve vote count and percentage of the largest county turnout
            votes_count_largest = votes
            county_largest_turnout = county
            Largest_county_turnout = (f"............................\n"
                f"Largest County Turnout:{county_largest_turnout}\n"
                f".............................\n"
                )
    # Print largest county turnout to the terminal.
    print(Largest_county_turnout)
    txt_file.write(Largest_county_turnout)

    for candidate in candidates_options:
        votes1 = candidates_votes[candidate]
        percentage_vote1 = float(votes1)/total_votes*100
        candidate_result = (
            f"{candidate}: {percentage_vote1:.1f}% ({votes1:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_result)
        txt_file.write(candidate_result)
        # Determine winning vote count, winning percentage, and winning candidate.
        if votes1>winning_candidate_vc:
            winning_candidate_vc = votes1
            winning_candidate = candidate
            winning_candidate_percent = percentage_vote1
            winning_summary = (f"........................\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_candidate_vc:,}\n"
            f"Winning Percentage: {winning_candidate_percent:.1f}%\n"
            f"........................")
    # Print the winning candidate's results to the terminal.
    print(winning_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_summary)
