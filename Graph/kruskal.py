import union_find
import matrix_to_list_2

def return_key(element):
	return(element[1])
	
def make_list(dictionary):
	
	f_list=[] 
	for keys in dictionary.keys():
		for l in dictionary[keys]:
			f_list.append(((keys,l[0]),l[1]))
	
	f_list=sorted(f_list,key=return_key)
	print(f_list)		
	return f_list

def print_adjacency_list(dictionary,text="Adjacency List"):
	print(text)
	for i in dictionary.keys():
		'''l=[j for j in dictionary[i]]'''
		print(i,'-->',dictionary[i])				
	print()

			
def kruskal_algo(dictionary):
	
	print_adjacency_list(dictionary)
	result=[]
	f_dict={}
	
	l=make_list(dictionary)
	
	key_list=list(dictionary.keys())
	
	for item in range(1,(max(key_list))+1):
		union_find.make_set(item)
		f_dict[item]=[]
	
	for item in l:
		a=union_find.find(item[0][0])
		b=union_find.find(item[0][1])
		
		if (a!=b):
			union_find.union(a,b)
			result.append(item[0])
	
	'''print(result)'''	
	
	for item in result:
		f_dict[item[0]].append(item[1])
	
	print_adjacency_list(f_dict,"Minimum Spanning Tree")
	
kruskal_algo(matrix_to_list_2.run('input.txt'))			
		
		

