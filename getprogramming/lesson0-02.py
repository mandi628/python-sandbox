# Think, code, test, debug, repeat
# Think - make sure you understand what is being asked of you. Decide whether you have any recipes (algorithms)
# that might work or if you need to come up with one on your own.

# Code - get your hands dirty and experiment with possible combinations of ingredients, any substitutions, and
# any repetitive parts. This is called implementation of an algorithm.

# Test - run the program with different inputs and check whether the actual output matches the expected output.

# Debug - figure out which lines of code are causing incorrect behavior.

# 2.3.1 Understanding the task - write a vague problem statement, then a specific one
# 2.3.2 Visualizing the task - create a flowchart outlining the processes you'll need
# 2.3.3 Write pseudocode - write out the steps of the problem solution in plain English

# 2.4 Writing readable code
# 2.4.1 Use descriptive and meaningful names
# 2.4.2 Comment in your code

# Quick Check 2.4

# You comment here - variables defining hose times in hours
time_green = 1.5
time_blue = 1.2

# Your comment here - conversion of hose times to minutes
minutes_green = 60 * time_green
minutes_blue = 60 * time_blue

# Your comment here - rate of filling per hour
rate_hose_green = 1 / minutes_green
rate_hose_blue = 1 / minutes_blue

# Your comment here - combining hose rates per hour
rate_host_combined = rate_hose_green + rate_hose_blue

# Your comment here - total time to fill pool with hoses combined
time = 1 / rate_host_combined
print(time)
