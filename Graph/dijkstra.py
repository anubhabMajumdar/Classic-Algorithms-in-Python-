import matrix_to_list_2

def dijkstra_algo(dictionary):
	
	A={}
	A[1]=0
	B={}
	for keys in dictionary.keys():
		B[keys]=[]
	X={}
	X[1]=dictionary[1]		
	traversed=[]
	traversed.append(1)
	
	while(len(X)!=len(dictionary)):
		minimum=9999
		tupple=()
		key=-1	
		for keys in X.keys():
			for edge in X[keys]:
				if ((edge[0] in traversed)==False):
					temp=A[keys]+edge[1]
					if (temp<minimum):
						minimum=temp
						tupple=edge
						key=keys
						#print(tupple)
		X[tupple[0]]=dictionary[tupple[0]]
		A[tupple[0]]=minimum
		B[key].append(tupple[0])
		traversed.append(tupple[0])
		
	#print(A)
	#print(B)
	print("Started at Node 1")
	print_adjacency_list(A,"Minimum path values")
	print_adjacency_list(B,"Minimum Path graph")
	
			
	
	
def remove_double_edges(dictionary):
	
	for keys in dictionary.keys():
		for edge in dictionary[keys]:
			try:
				l=dictionary[edge[0]]
				l.remove((keys,edge[1]))
			except:
				pass		
	
	print_adjacency_list(dictionary,"remove_double_edges")
	return(dictionary)


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
	dijkstra_algo(dictionary)
		
print("Enter filename")
inp=input()
run(inp)

