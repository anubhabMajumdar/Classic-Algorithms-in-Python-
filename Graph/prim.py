import matrix_to_list_2

class list_structure:

	def __init__(self,value,weight=None):
		self.value=value
		self.weight=weight

def remove_double_edges(d,min_key,minimum):
	
	(a,b)=minimum
	try:
		d[a].remove((min_key,b))
	except:
		pass

def prim_algo(dictionary):
	result={}
	traversed=[]
	
	key_list=list(dictionary.keys())
	key_list=sorted(key_list)
	pop_value=dictionary[key_list[0]].pop()
	result[key_list[0]]=[]
	result[key_list[0]].append(pop_value[0])
	traversed.append(key_list[0])
	result[pop_value[0]]=[]
	traversed.append(pop_value[0])
	remove_double_edges(dictionary,key_list[0],pop_value)
	
	while(len(result)!=len(dictionary)):
		minimum=(-1,99999)
		min_key=-1
		for keys in result.keys():
			key_list=list(result.keys())
			if dictionary[keys]!=[]:
				pop_value=dictionary[keys].pop()
			if (pop_value[1]<minimum[1]) & ((pop_value[0] in traversed)==False):
				minimum=pop_value
				min_key=keys
			dictionary[keys].append(pop_value)
		remove_double_edges(dictionary,min_key,minimum)
		dictionary[min_key].remove(minimum)				
		result[min_key].append(minimum[0])
		traversed.append(minimum[0])
		result[minimum[0]]=[]	
		'''print(result)
		print_adjacency_list(dictionary)'''	
	
	return(result)
				
def print_adjacency_list(dictionary,text="Adjacency List"):
	print(text)
	for i in dictionary.keys():
		'''l=[j for j in dictionary[i]]'''
		print(i,'-->',dictionary[i])				
	print()
			
def run(filename):
	
	dictionary=matrix_to_list_2.run(filename)
	print_adjacency_list(dictionary)
	answer=prim_algo(dictionary)
	print_adjacency_list(answer,"Minimum Spanning Tree")
	
run('input.txt')

