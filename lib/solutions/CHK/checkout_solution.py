

# noinspection PyUnusedLocal
# skus = unicode string

def first_clear(d):
	p = 0
	p += d['A']//5 * 200 
	d['A'] -= d['A']//5 * 5
	p += d['A']//3 * 130 

	
	d['B'] -= d['E']//2
	p += d['B'] // 2 * 45 
	
	if(d['F'] > 2):
		d['F'] -= d['F'] // 3


	p += d['H'] // 10 * 80
	d['H'] -= d['H'] // 10 * 10
	p += d['H'] // 5 * 45 
	d['H'] -= d['H'] // 5 * 5

	p += d['K'] // 2 * 150
	d['K'] -= d['K'] // 2 * 2

	d['M'] -= d['N'] // 3

	p += d['P'] // 5 * 200
	d['P'] -= d['P'] //5 * 5

	d['Q'] -= d['R'] // 3

	p += d['Q'] // 3 * 80
	d['Q'] -= d['Q'] // 3 * 3

	d['U'] -= d['U'] // 4

	p += d['V'] // 3 * 130
	d['V'] -= d['V'] // 3 * 3
	p += d['V'] // 2 * 90
	d['V'] -= d['V'] // 2 * 2


	return [d,p]
	
def second_clear(d,p,price_d):
	for x in d:
		if(price_d[x] >= 0):
			p += d[x] * price_d[x]

	return p

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

	return p

def checkout(skus):
    item_list = skus.split(" ")
    item_dict = {}
    for i in range(ord('A'), ord('Z')):
    	item_dict[chr(i)] = 0
    g = price_dict()
    p = 0
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
    print(item_dict)
    d,p = first_clear(item_dict)
    p = second_clear(d,p,g)
    return p

print(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))




