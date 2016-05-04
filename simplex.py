#First put problem in standard form and construct cannonical matrix
#     ^^ program will NOT do this.

#Loop
	#PHASE I
	#Find initial feasible solution


	#PHASE II
	#Find min C[i]
	#Check that min C[i] < 0
		#If yes Continue
			#For a[r,j] > 0 calculate b[r]/a[r,j] *note we'll need exceptions for negative and DBZ terms*
			#Find min (b[r]/a[r,j]) for a[r,j] > 0, ignoring previously reduced columns 
		#Else exit() with result
	#Rebuild cannonical table