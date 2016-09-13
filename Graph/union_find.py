global univ_list

def make_set(u):
	
	global univ_list
	
	l=[]
	l.append(u)
	
	univ_list.append(l)
	
def find(u):
	
	global univ_list
	
	for l in univ_list:
		if (u in l)==True:
			return l
	return -1

def union(u,v):
	
	global univ_list
	
	univ_list.remove(u)
	univ_list.remove(v)
	u.extend(v)
	univ_list.append(u)
	
	return univ_list

	
def initialize():
	
	global univ_list
	univ_list=[]
	
	'''make_set(1)
	make_set(2)
	make_set(3)
	
	a=find(2)
	b=find(3)
	
	c=union(a,b)
	print(c)'''
	
	
initialize()	

