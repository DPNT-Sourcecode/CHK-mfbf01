

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_list = skus.split(" ")
    refined_list = []
    for item in item_list:
    	num = 0
    	item = None

    	for s in item_list:
    		print(s)
    		if s.isdigit():
    			num = num*10 + int(s)
    		elif ((s == 'A' or s == 'B' or s == 'C' or s == 'D') and s == None):
    			item = s 
    		else:
    			return -1

    	refined_list.append([num,item])

    print(item_list)
    print(refined_list)

print(checkout("1A 2B"))


