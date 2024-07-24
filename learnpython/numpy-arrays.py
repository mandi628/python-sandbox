# alternatives to Python Lists; advantages - fast, easy to work with, give users the
# opportunity to perform calculations across entire arrays.

# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Print out the type of np_height
# NOTE: Not sure of the purpose of this line, but it's in the exercise.
print(type(np_height))

# NOTE: For consistency, I am printing the arrays.
print("Heights: %s" % np_height)
print("Weights: %s" % np_weight)

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print("BMIs: %s" % bmi)

# Another great feature of Numpy arrays is the ability to subset. For instance, if you
# wanted to know which observations in our BMI arary are above 25, we could quickly subset it
# to find out.

# For a boolean reponse
bmi > 25
# Print only those observations above 25
print("BMIs above 25: %s" % bmi[bmi > 25])

