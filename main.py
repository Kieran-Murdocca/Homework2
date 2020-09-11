# Author: Kieran Murdocca kkm5754@psu.edu
# Homework 2

def getGradePoint(lg1, lg2, lg3): 
  if lg1 == "A" or lg2 == "A" or lg3 == "A": 
    return float(4.00)
  elif lg1 == "A-" or lg2 == "A-" or lg3 == "A-": 
    return float(3.67)
  elif lg1 == "B+" or lg2 == "B+" or lg3 == "B+": 
    return float(3.33)
  elif lg1 == "B" or lg2 == "B" or lg3 == "B": 
    return float(3.00)
  elif lg1 == "B-" or lg2 == "B-" or lg3 == "B-": 
    return float(2.67)
  elif lg1 == "C+" or lg2 == "C+" or lg3 == "C+": 
    return float(2.33)
  elif lg1 == "C" or lg2 == "C" or lg3 == "C": 
    return float(2.00)
  elif lg1 == "D" or lg2 == "D" or lg3 == "D": 
    return float(1.00)
  else: 
    return float(0.00)

def run(): 
  lg1=input("Enter your course 1 letter grade: ")
  c1=float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is {getGradePoint(lg1)}.")
  lg2=input("Enter your course 2 letter grade: ")
  c2=float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is {getGradePoint(lg2)}.")
  lg3=input("Enter your course 3 letter grade: ")
  c3=float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is {getGradePoint(lg3)}.")
  print(f"Your GPA is:", (float(lg1) * float(c1) + float(lg2) * float(c2) + float(lg3) * float(c3)) / (float(c1) + float(c2) + float(c3) ))
  

if __name__ == "__main__": 
  run()