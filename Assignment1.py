def program():
	f = open('data1.txt','r')	# Open the text file in read mode
	
	acc=0	# Instantiate the accumulator
	arr=[0]*1000	# Instantiate the array with 1000 spots
	switch = False	# Start the switch that will end the while loop when ready


	spot=0	# Mark the spot at the end of the data file
	for line in f.readlines():	# Runs through each line of the data file
		for i in line.split():	# Splits the line into two variables and runs through them
			arr[spot] = int(i)	# Convert string to int and store in the array
			spot+=1 # Add to spot to keep track of array size

	spot -= 1 # Subtract 1 to get end of array
	endofcode = spot # endofcode will be where the code ends and data begins

	while arr[endofcode] != 0: # If there is data, this will run
		endofcode -= 1 # Subtract by one until it finds the 0 barrier in code

	endofcode += 1  # Adds one to define the beginning of data

	codes = ["blank", "add", "sub", "mult", "div", "read", "print", "load", "store", "iload", "br", "beq",
	"blt", "halt"]

	count = 0  # Instantiate the Program Counter

	print codes[6]
	str = "aaaaabbbb"
	newstr = str[-4:]
	print newstr

	while switch == False:
		if arr[count] == 1:  # OPCode 1
			acc = arr[arr[count+1]] + acc 	# addition
			count += 2
		
		elif arr[count] == 2: # OPCode 2
			acc = acc - arr[arr[count+1]]	# subtraction
			count += 2
		
		elif arr[count] == 3: # OPCode 3
			acc = acc * arr[arr[count+1]]	# multiplication
			count += 2
		
		elif arr[count] == 4: # OPCode 4
			acc = acc / arr[arr[count+1]]	# division
			count += 2
		
		elif arr[count] == 5: # OPCode 5
			arr[arr[count+1]] = arr[endofcode]	# get value from data, put in memory
			endofcode+=1 # Add 1 to endofcode so next data piece is readily available
			count += 2
		
		elif arr[count] == 6: # OPCode 6
			print arr[arr[count+1]]	# print
			count += 2
		
		elif arr[count] == 7: # OPCode 7
			acc = arr[arr[count+1]]	# load accumulator from memory location
			count += 2
		
		elif arr[count] == 8: # OPCode 8
			arr[arr[count+1]] = acc 	# store value of accumulator in memory location
			count += 2
		
		elif arr[count] == 9: # OPCode 9
			acc = arr[count+1]	# load accumulator with address
			count += 2
		
		elif arr[count] == 10: # OPCode 10
			count = arr[count+1]	# branch to instruction at address
		
		elif arr[count] == 11: # OPCode 11
			if acc == 0:
				count = arr[count+1]	# if accumulator is equal to 0, branch to address
			else:
				count += 2 # otherwise move on
		
		elif arr[count] == 12: # OPCode 12
			if acc < 0:
				count = arr[count+1]	# if accumulator is less than 0, branch to address
			else:
				count += 2 # otherwise move on
		
		elif arr[count] == 13: # OPCode 13
			switch = True	# halt machine
		
		else: # If OPCode doesn't exist, run this command
			return "Not a valid command"


program()  # Run program
