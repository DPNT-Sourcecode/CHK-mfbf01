

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = skus.split(" ")
    refined_list = []
    print(item_list)
    for item in item_list:
    	num = 0
    	it = None
    	print(item)
    	for s in item:
    		
    		if s.isdigit():
    			num = num*10 + int(s)
    		elif ((s == 'A' or s == 'B' or s == 'C' or s == 'D') and it == None):
    			it = s 
    		else:
    			print(s)
    			return -1

    	refined_list.append([num,it])

    print(item_list)
    print(refined_list)

print(checkout("1A 2B"))



