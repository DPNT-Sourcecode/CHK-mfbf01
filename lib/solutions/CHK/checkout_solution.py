

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = skus.split(" ")
    refined_list = [0,0,0,0,0,0]
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
    		elif(s=='E'):
    			refined_list[4] += 1
    		elif(s=='F'):
    			refined_list[5] += 1
    		else:
    			return -1
    if(refined_list[5] >2):
    	refined_list[5] = refined_list[5]//2 + refined_list[5] % 2
    refined_list[1] -= refined_list[4]//2 
    if(refined_list[1] < 0):
    	refined_list[1] = 0


    price = 0
    price += refined_list[0]//5 * 200
    refined_list[0] -= refined_list[0] // 5 * 5
    price += refined_list[0]//3 * 130 + refined_list[0]%3 * 50
    price += refined_list[1]//2 * 45 + refined_list[1]%2 * 30
    price += refined_list[2] * 20
    price += refined_list[3] * 15
    price += refined_list[4] * 40
    price += refined_list[5] * 10

    return price

print(checkout("FFFFF"))



