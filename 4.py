import re

with open ('genius club.txt', 'r') as file:
    pattern = r'\+\d\d+\-\d+'
    sequence = file.read()
    print(re.findall(pattern,sequence))

#Kudos for the Big bang theory question. Sheldon Approves 