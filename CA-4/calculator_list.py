## calculator.py
#program will contain 10functions that are comminly used on a scientific calculator
#functions can take a list of arguments 

import os
'''import the math library for python functions,
this will save time and prevent the need for working out several derivations.
''' 
import math 

'''calculates the product of an integer and all the integers below it
eg factorial 4 = (4*3*2*1) = 24''' 



def main():
	os.system("cls") 	# clears screen when program starts
	
	print "Hello and welcome to your Scientific Calcultor"
	print
	
	#start a loop with the calculator options, after a calcution is completed the options will be printed again.
	while (True):
		print """ Calculator opptions are as follows..
		
		Exit		= 0 
		Add 		= 1
		Subtract 	= 2
		Multiply	= 3 
		Divide 		= 4 
		Factorial	= 5
		Square Root	= 6
		Power		= 7
		Sine		= 8 
		Cos		= 9
		Tan		= 10"""
		print
		
		choice = input("Please select the number of the function you wish to use : ")
		#use if and elif statements to call the necessary functions
		#add function is called and two arguments inputed
		if choice == 1:
			print "You have selected the Add fuction : "
			print
			
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			answer = reduce(lambda x,y:x+y,list_numbers)
			
			operator = '+'
			list_numbers
			print operator.join (list_string), '= ', answer
			print
			
		
		#subtract funtion is called and two arguments are inputed 
		elif choice == 2:
			print "You have selected the subtract fuction : "
			print
			
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			answer = reduce(lambda x,y:x-y,list_numbers)
			
			operator = '-'
			list_numbers
			print operator.join (list_string), '= ', answer
			print
		#multiply function is called and two arguments are inputed
		elif choice == 3:
			print "You have selected the multiply fuction : "
			print
			
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			answer = reduce(lambda x,y:x*y,list_numbers)
			
			operator = '*'
			list_numbers
			print operator.join (list_string), '= ', answer
			print
		
		#divide function is called and two arguments are inputed
		#variables are turned into floates to allow for non integer division 
		elif choice == 4:
			print "You have selected the multiply fuction : "
			print
			
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			answer = reduce(lambda x,y:x/y,list_numbers)
			
			operator = '/'
			list_numbers
			print operator.join (list_string), '= ', answer
			print
		
		#factorial function is called and one argument is inputed
		elif choice == 5:
			print "You have selected the factorial fuction : "
			print
			n = input("please enter the number you wish to calculate a factorial of: ")
			answer = reduce(lambda x,y:x*y,range(1,n+1))
			print
			print n, "!  =", answer
		
		#square root function is called on input list
		elif choice == 6:
			print "You have selected the square root fuction : "
			print
			
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			list_square  = map(math.sqrt,list_numbers)
			
			results = zip(list_numbers,list_square)		# zip joins 2 lists together, they must be the same size, the first elemnt both lists are paired with each other. Created as tuples.
			
			for a,b in results:
				print 'the square root of ',a,' is ',b 
			

			
		#power funtion is called and two arguments are inputed 
		elif choice == 7:
			print "You have selected the power fuction : "
			print
			
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			power = input("please enter the order of the power you wish to calculate : ")
			list_power = map(lambda x:x**power,list_numbers)
			
			print
			results = zip(list_numbers,list_power)
			
			for a,b in results:
				print a,' to the power of ', power ,'is ',b 
		
		#sin function is called and executes on the given input
		elif choice == 8:
			print "You have selected the Sine fuction : "
			print
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			list_sine  = map(lambda x:math.sin(math.radians(float(x))),list_numbers)
			
			results = zip(list_numbers,list_sine)
			
			for a,b in results:
				print 'the sin of (',a,') is ',b 
			

		
		#cos function is called and executes on the given input
		elif choice == 9:
			print "You have selected the Cos fuction : "
			print
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			list_cos  = map(lambda x:math.cos(math.radians(float(x))),list_numbers)
			
			results = zip(list_numbers,list_cos)
			
			for a,b in results:
				print 'the cos of (',a,') is ',b 
		
		#tan function is called and executes on the given input
		elif choice == 10:
			print "You have selected the Tan fuction : "
			print
			first = raw_input("please enter a list of numbers separtated by spaces: ")
			list_string = first.split()
			list_numbers = map(int,list_string)
			list_tan  = map(lambda x:math.tan(math.radians(float(x))),list_numbers)
			
			results = zip(list_numbers,list_tan)
			
			for a,b in results:
				print 'the tan of (',a,') is ',b 
		
		

		elif choice == 0:
			print
			print "Goodbye.. "
			break
		
		#invalid input, so loop restarts and options are re-printed
		else:
			print "That is not a valid selection, please choose between 0-10 : " 
	 
main()