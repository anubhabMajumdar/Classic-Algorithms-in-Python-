class list_structure:

	def __init__(self,value,weight=None):
		self.value=value
		self.weight=weight
		
class adjacency_matrix:

	def __init__(self,filename):
		
		f=open(filename,'r')
		self.vertex=int(f.readline())
		self.matrix=[]
		self.file=filename
		f.close()
		
	def edge_relation(self):
		f=open(self.file,'r')
		count=int(f.readline())
		
		for i in range(count):
			line=f.readline()
			line=line.split()
			new=[]
			new=[int(j) for j in line]
			self.matrix.append(new)
				
		f.close()
		
	def print_matrix(self):
		print("Number of vertices-->",self.vertex,"\n")
		print("Matrix input")
		for i in range(0,self.vertex):
			print (self.matrix[i])
		print()
		
	def return_vertex(self):
		return(self.vertex)
	
	def return_matrix(self):
		return(self.matrix)
		
class adjacency_list:
	
	def __init__(self,matrix_obj):
		self.vertex=matrix_obj.return_vertex()
		self.matrix_input=matrix_obj.return_matrix()
		self.dictionary={}
		
	def edge_relation(self):
		for i in range(self.vertex):
			edge_list=[]
			for j in range(self.vertex):
				#if (self.matrix_input[i][j]>0):
				if ((self.matrix_input[i][j]==0)==False):
					'''new=list_structure(j+1,self.matrix_input[i][j])'''
					new=(j+1,self.matrix_input[i][j])
					edge_list.append(new)
			edge_list=sorted(edge_list,key=return_key)
			edge_list.reverse()		
			self.dictionary.update({(i+1):edge_list})
	
	def print_adjacency_list(self):
		print("Adjacency List")
		for i in self.dictionary.keys():
			l=[j for j in self.dictionary[i]]
			print(i,'-->',l)				
			
		print()

	def return_adjacency_list(self):
		return(dict(self.dictionary))
		
		
def return_key(s):
	
	return (s[1])
	
def run(filename):
	
	a=adjacency_matrix(filename)
	a.edge_relation()
	a.print_matrix()
	
	b=adjacency_list(a)
	b.edge_relation()
	'''b.print_adjacency_list()'''
	
	return(b.return_adjacency_list())
		
'''run('input2.txt')'''	
				
