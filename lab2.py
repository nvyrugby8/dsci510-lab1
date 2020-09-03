# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Lab 1
# ---
# Hello All,
# 
# I am Dhrumil Soni, the CP of the course DSCI 510. Welcome to the lab.
# 
# Guidelines for the Lab:
# - You will be given the lab assignment in the start of the lab. You're supposed to complete it by the deadline stated on DEN. Should be usually on Friday Midnight.  
# 
# - You've to complete the assignments individually. If you are having trouble completing the assignment do let me know, I will clear your doubts and guide you but I'll not write code for you and no one else should :) !!!  
# 
# - You have to fill in the code to this notebook and upload it to your repository. And simply, submit the link to the repo. Also, the repository name has to be in the form 'dsci510-lab(Lab Number)'. For example, first lab would be 'dsci510-lab1'  
# 
# - You are encouraged to look up resources online like python docs and stackoverflow. But, you are encouraged to look up the topics and not the questions themselves  
# 
# - Your last submission will be counted towards your grade on DEN and do not edit the repository after the deadline  
# %% [markdown]
# Q1[10 points]. Given two integers base and power print the exponent that is $base^{power}$. Fill the function in the next cell to complete the task.
# 
# After completing the whole lab, try running this code with a huge power like say a million and see what happens. Try to realize the potential of such a language that scales and utilizes the computing power that you have.(Computer might hang after this, do it with a smaller power if you think your computer can't handle it)
# 
# ---
# Example:  
# Input:  
# base = 2, power = 4  
# Output:  
# Answer is 16  
# 
# ---
# Rubric: 5 points if you get the exponent on a variable. 10 points if your code does exactly as required. 

# %%
def exponent(base, power):
    exp = base**power
    print("Answer is", exp)
    # Remove pass and enter your code here

exponent(2, 4)

# %% [markdown]
# Q2[10 points]. Take the input temperature in Fahrenheit and print the value of temperature in Celsius  
# Note: You have to prompt the user for taking the value of a variable. Fill the function in the next cell to complete the task.  
# 
# ---
# 
# For example,  
# Input:  
# Enter the temperature in Fahrenheit: 75  
# Output:  
# Temperature in Celcius is 23.88888888888889  
# 
# Hint:
# 1. Formula-> C = (F-32)*5/9  
# 2. You'll need to cast the datatype after the input  
# 
# ---
# Rubric: 3 points for taking the input correctly. 6 points if input is taken correctly and temperature in F is stored in appropriate datatype. 10 points if code does exactly as required. 

# %%
def f_to_c():
    fahr_input = input("Enter the temperature in Fahrenheit:")
    fahrenheit = float(fahr_input)
    celsius = (fahrenheit-32)*5/9
    print("Temperature in Celsius is", celsius)


f_to_c()

# %% [markdown]
# Q3[10 points]. Write a function that returns the slope of two points.  
# 
# ---
# Example 1:   
# Input:  
# x1 = 0, y1 = 0, x2 = 1, y2 = 1   
# Output:  
# 1  
# 
# Hint:  
# Formula: $slope = (y2-y1)/(x2-x1)$
# 
# ---
# Rubric: 3 points if code gets the slope. 10 points if it always gives correct slope and code doesn't crash.

# %%
# Use this cell for your solution

def get_slope(x1, y1, x2, y2):
    rise = y2 - y1
    run = x2 - x1
    if run == 0:
        print("Slope of (",x1,",",y1,") and (",x2,",",y2,") is undefined")
    else:
        slope = rise/run
        print("Slope of (",x1,",",y1,") and (",x2,",",y2,") =", slope)

get_slope(0, 0, 1, 1)

# %% [markdown]
# Challenge/Bonus Question[5 points]
# ---
# Provided the day $d$ of the week as an number from 0-6 where 0 indicates monday and 6 indicates sunday and a number $add$ as the number of days to be added. Print the day of the week after adding $add$ days to $d$.
#  
# ---
# Example 1:  
# Input:  
# d = 1, add = 3   
# Output:  
# The day is 4   
# Example 2:   
# Input:   
# d = 0, add = 7   
# Output:  
# The day is 0
# 
# ---
# Rubric: Binary

# %%
def day(d, add):
    new_day = d + add
    new_day_of_week = new_day % 7
    if new_day_of_week == 0:
        print ("The day is Monday.",new_day_of_week)
    elif new_day_of_week == 1:
        print ("The day is Tuesday.",new_day_of_week)
    elif new_day_of_week == 2:
        print ("The day is Wednesday.",new_day_of_week)
    elif new_day_of_week == 3:
        print ("The day is Thursday.",new_day_of_week)
    elif new_day_of_week == 4:
        print ("The day is Friday.",new_day_of_week)
    elif new_day_of_week == 5:
        print ("The day is Saturday.",new_day_of_week)
    elif new_day_of_week == 6:
        print ("The day is Sunday.",new_day_of_week)
    else:
        print("There has been an error!")


day(1, 3)
day(0, 7)


# %%



