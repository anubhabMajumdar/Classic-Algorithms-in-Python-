import matrix_to_list_2
import sys

def bellman_ford_algo(dictionary):
	distance={}
	predecessor={}
	
	for keys in dictionary.keys():
		if keys==1:
			distance[keys]=0
		else:
			distance[keys]=sys.maxsize
		
		predecessor[keys]=None		
	
	for keys in dictionary.keys():
		for item in dictionary[keys]:
			u=keys
			v=item[0]
			w=item[1]
			
			if ((distance[u]+w)<distance[v]):
				distance[v]=distance[u]+w
				predecessor[v]=u
	
	print_adjacency_list(distance,"Distance")	
	print_adjacency_list(predecessor,"Predecessor")	
	
	for keys in dictionary.keys():
		for item in dictionary[keys]:
			u=keys
			v=item[0]
			w=item[1]
			
			if ((distance[u]+w)<distance[v]):
				print("Error!!! Negetive cycle detected!\n")
				sys.exit(0)
				
	result={}
	for keys in dictionary.keys():
		result[keys]=[]
		
		
	for keys in predecessor.keys():
		item=predecessor[keys]
		if item:
			result[item].append(keys)
		
		
	print_adjacency_list(result,"Result")	
	
	
	
	
	
	
	
		
def print_adjacency_list(dictionary,text="Adjacency List"):
	print(text)
	for i in dictionary.keys():
		'''l=[j for j in dictionary[i]]'''
		print(i,'-->',dictionary[i])				
	print()
	

def run(filename):
	
	dictionary=matrix_to_list_2.run(filename)
	print_adjacency_list(dictionary)
	#dictionary=remove_double_edges(dictionary)
	bellman_ford_algo(dictionary)
		
print("Enter filename")
inp=input()
run(inp)

