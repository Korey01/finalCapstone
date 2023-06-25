#This is a program that allows the user to determine either their retuns through simple or compound interest in the case of an investment or allows the user know their monthly repayment on a home loan. it is written to ensure that user response is not case sensitive and so the user can make choices as the progress on the application. NOTE: INTEREST RATE USED FOR INVESTMENT IS INPUTED AS SIMPLIFIED DECIMAL BY USER whilst INTREST RATE FOR BOND IS INPUTED AS A WHOLE NUMBER AND THEN PROCESSED THROUGH CODE TO DECIMAL AND PRORATED THROUGH A 12 MONTH DIVISION FOR OUR CALCULATION. THIS IS FOR NO SPECIAL REASON BUT JUST TO SHOW UNDERSTASNDING OF THE CODE.



print("Investment - to calculate amount of interest you'll earn on investment" )
print("Bond       - to calculate the amount you'll have to pay on a home loan" )


Choice_of_transaction = input ("Enter either 'investment' or 'bond' from the above menu to proceed: ").lower()
Choice_of_transaction == "investment" or "Bond"
if Choice_of_transaction == "investment":
  Principal = int(input("Enter principal amount: "))
  Rate = float(input("Enter rate : "))
  Time = int(input("Enter duration in years: "))   
  Choice_of_interest_type= input("Enter either 'simple' or 'compound': ").lower()
  if Choice_of_interest_type == "simple":
    Amount = Principal*(1+(Rate/100)*Time)  
    print(f"Your total return on investment is {Amount}")    
  elif Choice_of_interest_type == "compound":
      Amount_2 = int(Principal*math.pow((1+(Rate/100)),Time))
      print(f"Your total return on investment is {Amount_2}")
          
elif Choice_of_transaction == "bond":
  PV = int(input("Enter present value of House: "))
  interest_rate = (float(input("Enter rate (e.g 4%): "))/100)/12 
  duration = int(input("Enter duration in months: "))
  repayment = int((interest_rate * PV)/(1 - (1 + interest_rate)**(-duration)))
  print(f"Your monthly repayment on a home loan is {repayment}")