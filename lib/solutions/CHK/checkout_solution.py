

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = skus.split(" ")
    refined_list = []
    #print(item_list)

    #parse skus
    for item in item_list:
    	num = -1
    	it = None
    	#print(item)
    	for s in item:
    		
    		if s.isdigit():
    			if(num == -1):
    				num = 0
    			num = num*10 + int(s)
    		elif ((s == 'A' or s == 'B' or s == 'C' or s == 'D') and it == None and num != -1):
    			it = s 
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





