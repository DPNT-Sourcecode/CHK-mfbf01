

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
    			return -1


    price = 0
    	
    price += refined_list[0]//3 * 130 + refined_list[0]%3 * 50
    price += refined_list[1]//2 * 45 + refined_list[1]%2 * 30
    price += refined_list[2] * 20
    price += refined_list[3] * 15

    return price

print(checkout(""))
