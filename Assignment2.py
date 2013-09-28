def program():
	
	acc=0	# Instantiate the accumulator
	arr=[]	# Instantiate the array with 1000 spots
	switch = False	# Start the switch that will end the while loop when ready
	vals=[0]*200 # Set up empty array for values 
	labels = [0]*100 # Set up empty array for labels
	endofcode = 0 # Finds end of code and becomes a marker for data

	with open("stats.txt") as f: # Opens file and puts instructions into arr
		for line in f:
			line = line.partition('.')[0]
			line = line.rstrip()
			arr.extend(line.split())

	i = 0 # temp variable to find end of code
	for values in arr: # Goes through the arr and finds the 'data' instruction
		if values == 'data':
			endofcode = i+1
			break
		else:
			i+=1

	codes = ["blank", "add", "sub", "mult", "div", "read", "print", "load", "store", "iload", "br", "beq",
	"blt", "halt"] # An array of codes to do comparison with instructions

	count = 0  # Instantiate the Program Counter
	valMarker = 199 # Used to track where values are in the values array
	labelMarker = 0 # Used to track where the labels are in the label array

	tempcount=0 # Temporary count for labels finder
	for tempvar in arr: # Finds the labels in the array and replaces them with count number
		if tempvar[-1:] == ':':		
			labels[labelMarker] = tempcount+1
			arr[tempcount] = 'L' + str(labelMarker)
			secondvarcount = 0
			for secvars in arr:
				if secvars == tempvar[:-1]:
					arr[secondvarcount] = arr[tempcount]
				secondvarcount += 1
			labelMarker+=1		
		tempcount += 1


	while switch == False: 
		if arr[count] == codes[1]:  # OPCode 1
			acc = vals[arr[count+1]] + acc 	# addition
			count += 2
		
		elif arr[count] == codes[2]: # OPCode 2 
			acc = acc - vals[arr[count+1]]	# subtraction
			count += 2
		
		elif arr[count] == codes[3]: # OPCode 3
			acc = acc * vals[arr[count+1]]	# multiplication
			count += 2
		
		elif arr[count] == codes[4]: # OPCode 4
			acc = acc / vals[arr[count+1]]	# division
			count += 2
		
		elif arr[count] == codes[5]: # OPCode 5
			tempcount=0 # Temporary counter
			if type(arr[count+1]) == type(codes[1]):
				tempvarname = arr[count+1]
				for tempvar in arr: # Finds the variable name and replaces with the value number in val array
					if tempvarname == tempvar:
						arr[tempcount] = int(valMarker)
					tempcount += 1
				vals[valMarker] = int(arr[endofcode])	# get value from data, put in memory
				valMarker-=1
			elif type(arr[count+1]) == type(count):
				vals[arr[count+1]] = int(arr[endofcode])
			endofcode+=1 # Add 1 to endofcode so next data piece is readily available
			count += 2

		elif arr[count] == codes[6]: # OPCode 6
			print vals[arr[count+1]]	# print
			count += 2
		
		elif arr[count] == codes[7]: # OPCode 7
			acc = vals[arr[count+1]]
			count += 2
		
		elif arr[count] == codes[8]: # OPCode 8
			if type(arr[count+1]) != type(count): # If the variable isn't a name, this
				tempcount=0						  # puts the variable in the vals array and gives all
				tempvarname = arr[count+1]		  # future calls the spot in the vals array
				for tempvar in arr:
					if tempvarname == tempvar:
						arr[tempcount] = int(valMarker)
					tempcount += 1
				vals[valMarker] = acc  # Puts whatever is in the accumulator in the vals array spot
				valMarker-=1
			else:  # If its already been assigned, it puts the accumulator in the vals array spot
				vals[arr[count+1]] = acc
			count += 2
		
		elif arr[count] == codes[9]: # OPCode 9
			acc = int(arr[count+1])	# load accumulator with address
			count += 2
		
		elif arr[count] == codes[10]: # OPCode 10
			branchInstruction = int(arr[count+1][1:])
			count = labels[branchInstruction]	# branch to instruction at address
		
		elif arr[count] == codes[11]: # OPCode 11
			if acc == 0:
				branchInstruction = int(arr[count+1][1:])
				count = labels[branchInstruction]	# if accumulator is equal to 0, branch to address 
			else:
				count += 2 # otherwise move on
		
		elif arr[count] == codes[12]: # OPCode 12
			if acc < 0:
				branchInstruction = int(arr[count+1][1:])
				count = labels[branchInstruction]	# if accumulator is less than 0, branch to address
			else:
				count += 2 # otherwise move on
		
		elif arr[count] == codes[13]: # OPCode 13
			switch = True	# halt machine
		
		elif arr[count][0:1] == 'L': # If the spot has an 'L' in it, it is identified as a label spot and
			count += 1 				 # is skipped

		else: # If OPCode doesn't exist, run this command
			print "Not a valid command"


program()  # Run program
