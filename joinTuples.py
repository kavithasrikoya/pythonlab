myList = [(2, 5), (9, 4), (9, 0), (1, 4), (1, 5)]
print("Initially the list is : " + str(myList))
joinList = []
for val in myList:										
	if joinList and joinList[-1][0] == val[0]:			
		joinList[-1].extend(val[1:])						
	else:
		joinList.append([ele for ele in val])	
joinList = list(map(tuple, joinList))
print("Joined list : " + str(joinList))

