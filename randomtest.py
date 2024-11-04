import numpy as np

# Number of trials
num_trials = 20

# Initialize a list to store results
results = []

for trial in range(num_trials):
    # Generate an array of 10 random integers between 0 and 9
    random_numbers = np.random.randint(0, 10, size=10)
    
    # Check how many numbers are in the correct form
    count_valid_numbers = sum(random_numbers[i] == i for i in range(10))
    
    # Store the result along with the array
    results.append((random_numbers, count_valid_numbers))

# Print the results for each trial
for i, (array, count) in enumerate(results):
    print(f"Trial {i + 1}: Array = {array}, Valid numbers count = {count}")