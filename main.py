# Author: Kieran Murdocca kkm5754@psu.edu
# Homework 2

def getGradePoint(lg): 
  if lg == "A": 
    return float(4.00)
  elif lg == "A-": 
    return float(3.67)
  elif lg == "B+": 
    return float(3.33)
  elif lg == "B": 
    return float(3.00)
  elif lg == "B-": 
    return float(2.67)
  elif lg == "C+": 
    return float(2.33)
  elif lg == "C": 
    return float(2.00)
  elif lg == "D": 
    return float(1.00)
  else: 
    return float(0.00)

def run(): 
  lg1=input("Enter your course 1 letter grade: ")
  c1=float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(lg1)}")
  gp1=getGradePoint(lg1)
  lg2=input("Enter your course 2 letter grade: ")
  c2=float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint(lg2)}")
  gp2=getGradePoint(lg2)
  lg3=input("Enter your course 3 letter grade: ")
  c3=float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint(lg3)}")
  gp3=getGradePoint(lg3)
  gpa = (gp1 * c1 + gp2 * c2 + gp3 * c3) / (c1 + c2 + c3)
  print(f"Your GPA is: {gpa}")
  

if __name__ == "__main__": 
  run()