

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = skus.split(" ")
    refined_list = []
    print(item_list)
    for item in item_list:
    	num = -1
    	it = None
    	print(item)
    	for s in item:
    		
    		if s.isdigit():
    			if(num == -1):
    				num = 0
    			num = num*10 + int(s)
    		elif ((s == 'A' or s == 'B' or s == 'C' or s == 'D') and it == None and num != -1):
    			it = s 
    		else:
    			print(s)
    			return -1
    	if(num < 0):
    		return -1
    	refined_list.append([num,it])

    print(item_list)
    print(refined_list)

print(checkout("1A 3A"))




