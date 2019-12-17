#Write a Python program to take the date of birth of the user in form 1997 10 19, and then display the age of the user in number of days.
import datetime
  
def calculateAge(birthDate): 
    today = datetime.date.today() 
    age = today.year - birthDate.year - ((today.month, today.day)<(birthDate.month, birthDate.day))  
    return age 
      
dob = datetime.datetime.strptime(input('Enter your dob: '))      
print(calculateAge(dob), "years") 