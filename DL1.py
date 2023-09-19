# Given age of the person and predict whether he will buy insurance or not
# Binary classification

# Import libraries
import pandas as pd
import math

data = pd.read_csv('insurance_data.csv') 

# Linear regression
# y = mx + b

# Logistic regression
# z = 1/(1 + e^-y)

# If z < 0.5 the o/p = 0 else o/p = 1

# Let x = 35
# x = 43
x = 35
y = 0.042 * x - 1.53		# Linear equation as first part
z = 1/(1 + 2.71 ** -y)		# Activation function as second part

if z < 0.5:
	print("Person will not buy insurance")
else:
	print("Person will buy insurance")

# Instead of x being the single feature, there can be multple features
# as x1, x2, x3
# Then y = Sum(wi*xi) + b
# 	   z = 1 / (1 + e ^ -y)