cho = ""
while (cho != "end"):
	print("""                      ##########################
		      #                        #
		      #   Simple Calculator    #
		      #                        #
		      ########################## """)
	print("""  Choise the Function
         1.Calculate the number
         2.Exit the program """ )
	inp = input(" Choose Number :")
	if(inp == "1"):
		num1 = int(input("Enter First Number :"))
		num2 = int(input("Enter Second Number :"))
		operator = input("Enter Operator :")
		if(operator == "+"):
			plus = num1 + num2			
			print("Answer  =  %d" %plus)
		elif(operator == "-"):
			minus = num1 - num2
			print("Answer  =  %d" %minus)
		elif(operator == "*"):
			multi = num1 * num2
			print("Answer  =  %d" %multi)
		elif(operator == "%"):
			divided = num1 % num2
			print("Answer  =  %d" %divided)
		else:
			print("Input ERROR")
	elif(inp == "2"):
		print("Good Bye")
		cho = "end"




