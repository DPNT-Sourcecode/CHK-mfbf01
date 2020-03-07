

# noinspection PyUnusedLocal
# skus = unicode string

def price_dict():
	p = {}
	p['A'] = 50
	p['B'] = 30
	p['C'] = 20
	p['D'] = 15
	p['E'] = 40
	p['F'] = 10
	p['G'] = 20
	p['H'] = 10
	p['I'] = 35
	p['J'] = 60
	p['K'] = 80
	p['L'] = 90
	p['M'] = 15
	p['N'] = 40
	p['O'] = 10
	p['P'] = 50
	p['Q'] = 30
	p['R'] = 50
	p['S'] = 30
	p['T'] = 20
	p['U'] = 40
	p['V'] = 50
	p['W'] = 20
	p['X'] = 90
	p['Y'] = 10
	p['Z'] = 50


def checkout(skus):
    item_list = skus.split(" ")
    item_dict = {}
    price_dict = price_dict()
    
    for item in item_list:
    	num = -1
    	it = None
    	for s in item:
    		if(s.isupper()):
    			if(s not in item_dict):
    				item_dict[s] = 1
    			else:
    				item_dict[s] += 1
    		else:
    			return -1
    if(refined_list[5] >2):
    	refined_list[5] -= refined_list[5]//3 
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


