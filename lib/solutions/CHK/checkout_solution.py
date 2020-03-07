

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = skus.split(" ")
    refined_list = [0,0,0,0]
    #print(item_list)

    #parse skus
    for item in item_list:
    	num = -1
    	it = None
    	#print(item)
    	for s in item:
    		
    		
    		if(s=='A'):
    			refined_list[0] += 1
    		elif(s=='B'):
    			refined_list[1] += 1
    		elif(s=='C'):
    			refined_list[2] += 1
    		elif(s=='D'):
    			refined_list[3] += 1
    		else:
    			#print(s)
    			return -1
    	if(num < 0):
    		return -1
    	refined_list.append([num,it])

    price = 0
    for x in refined_list:
    	if(x[1] == 'A'):
    		price += x[0]//3 * 130 + x[0]%3 * 50
    	elif(x[1] == 'B'):
    		price += x[0]//2 * 45 + x[0]%2 * 30
    	elif(x[1] == 'C'):
    		price += 20
    	elif(x[1] == 'D'):
    		price += 15

    return price

print(checkout("4A 3B"))






