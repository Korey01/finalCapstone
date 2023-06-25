
#This is a program that allows a user to chose an and execute an action from a series of action without the program crashing due to wrong entry by the user. User will also choose a task from either entering data or reading data from text file or closing the program. It also allow the user choose the operand  they want to use in their task equation,
file = open("calculator.txt", "w") #this line of code opens a text file where the code/equation will be written to

#This block allows the user to enter numbers for his calculation and uses try-except to prevent an error when an an invalid interger is or an invalid divisor is entered by the user.
while True:
  try:
    Number_1 = int(input("Kindly enter a Number: "))
    Number_2 = int(input("Kindly enter a second number: "))
    divide = Number_1/Number_2 #This line of division code is used to test the entry for invalid divisors
    break
     
  except Exception:
    print("Sorry! You have either entered an invalid number or an invalid divisor. Remember you cant divide by Zero")
    
    #print("Sorry! That was not a valid number")
  #finally:
    #divide = Number_1/Number_2
    #if ZeroDivisionError:
     # print("Zero is not a valid Divisor")

#this block of prevent the program from running into an unidentified variable when is about to write the equation to the opened text file.    
#multiply = Number_1*Number_2

#subtract = Number_1 - Number_2
#add = Number_1 + Number_2



#This block of code is used to iterate on the operand variable if the user enters a wrong operand. it alkso calculates the chosen/intended equation.
while True:
  Operand = input("Kindly Choose from the following operands to calculate ('Multiply'(*), 'Divide'(/), 'Add'(+), 'Subtract'(-): ").lower()
  
  if Operand == "multiply" or Operand == "*":
    multiply = Number_1*Number_2 
    print(f"Your answer is: {multiply}")
    file.write(f"{Number_1}{Operand}{Number_2}")#used to write equation to text file.
    file.write(f"= {multiply}")#used to write equation to text file.
    
    break      
  elif Operand == "divide" or Operand == "/":
    try: 
      divide = Number_1/Number_2
      print(f"Your answer is: {divide}")
      file.write(f"{Number_1}{Operand}{Number_2}")#used to write equation to text file.
      file.write(f"= {divide}")#used to write equation to text file.
      break
    except ZeroDivisionError: 
      print("Zero is not a valid Divisor")
  elif Operand == "subtract" or Operand == "-":
    subtract = Number_1 - Number_2
    print(f"Your answer is: {subtract}")
    file.write(f"{Number_1}{Operand}{Number_2}")#used to write equation to text file.
    file.write(f"= {subtract}")#used to write equation to text file.
    break      
  elif Operand == "add" or Operand == "+":
    add = Number_1 + Number_2
    print(f"Your answer is: {add}")
    file.write(f"{Number_1}{Operand}{Number_2}")#used to write equation to text file.
    file.write(f"= {add}")#used to write equation to text file.
    break
  else:
    print("Incorrect Operand")
    file.write(f"{Number_1}{Operand}{Number_2}")#used to write equation to text file.
    file.write("= Incorrect Operand.")#used to write equation to text file.
    break

      
file.close() #This line of code closes the opened text file



#Thisd block of code gives the user an opportunity to chose whether to type equation or read equation from text file or end program

while True:
  choice = input("Enter 'E' to type actions, Enter 'R' to read text file, and enter 'EE' to end program: ").upper()
  #this block runs the code to execute the entered equation   
  if choice == "E":
    while True:
       try:
         Number_1 = int(input("Kindly enter a Number: "))
         Number_2 = int(input("Kindly enter a second number: "))
         divide = Number_1/Number_2 #This line of division code is used to test the entry for invalid divisors
         break
       except Exception:
         print("Sorry! You have either entered an invalid number or an invalid divisor. Remember you cant divide by Zero")

    while True:
      Operand = input("Kindly Choose from the following operands to calculate ('Multiply'(*), 'Divide'(/), 'Add'(+), 'Subtract'(-): ").lower()
  
      if Operand == "multiply" or Operand == "*":
        multiply = Number_1*Number_2 
        print(f"Your answer is: {multiply}")
        break      
      elif Operand == "divide" or Operand == "/":
        divide = Number_1/Number_2
        print(f"Your answer is: {divide}")
        break      
      elif Operand == "subtract" or Operand == "-":
        subtract = Number_1 - Number_2
        print(f"Your answer is: {subtract}")
        break      
      elif Operand == "add" or Operand == "+":
        add = Number_1 + Number_2
        print(f"Your answer is: {add}")
        break
      else:
        print("Incorrect Operand")
      break

#block runs the code to read text file  
  elif  choice == "R":
    while True:
      file_name = input("Enter name of text file: ")
      try:
        file= open(file_name)
        info=file.readlines()
        print(info)
        break
      except FileNotFoundError:
        print("Sorry,File doesn't exist.")
      finally:
        if file is not None:
          file.close()

#this block runs the code to end the program  
  elif choice == "EE":
    print("The Program has ended.")
    break

  else:
    print("That was a wrong entry! ")
     


  
  
  

    
    
