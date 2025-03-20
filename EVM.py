import os
import time

# Candidates and their vote counts stored in a dictionary
candidates = {
    "cristiano ronaldo": 0,
    "lionel messi": 0,
    "taylor swift": 0,
    "bts": 0,
    "black pink": 0,
    "narendra modi": 0,
    "rahul gandhi": 0,
    "donald trump": 0,
    "joe biden": 0,
    "vladimir putin": 0,
    "adolf hitler": 0,
    "israel": 0,
    "palestine": 0
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    print("Electronic Voting Machine (EVM)")
    print()
    time.sleep(2)

    # Display candidates
    print("Vote for any ONE of the following:")
    for candidate in candidates:
        print(f"- {candidate.title()}")
    print()
    time.sleep(7)

    # Get the vote input
    vote = input("> ").strip().lower()

    # Check if the vote is valid
    if vote in candidates:
        candidates[vote] += 1
    else:
        print("Invalid vote. Please try again.")
        time.sleep(2)
        continue

    time.sleep(1)
    clear_screen()

    # Display current results
    print("Results till now:")
    for candidate, votes in candidates.items():
        print(f"{candidate.title()}: {votes}")
    print()
    time.sleep(10)

    # Ask if the user wants to vote again
    again = input("Once more? (yes/no): ").strip().lower()
    if again != "yes":
        break

    clear_screen()