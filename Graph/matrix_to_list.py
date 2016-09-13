'''Building Blocks For Adjacency List'''

class list_structure:
	
	def __init__(self,value):
		self.val=value
		self.link=None
		

class adjacency_matrix:

	def __init__(self,v,e):
		self.vertex=v
		self.edge=e
		self.matrix=[]
		
	def edge_relation(self):
		f=open('input.txt','r')
		f.readline()
		
		content=f.read()
		line=content.split()
		
		for l in line:
			new=[]
			new=[int(i) for i in l]
			self.matrix.append(new)
				
		f.close()
		
	def print_matrix(self):
		print("Matrix input")
		for i in range(0,self.vertex):
			print (self.matrix[i])
	
	def return_matrix(self):
		return(self.matrix)
		
class adjacency_list:
	
	def __init__(self,v,e):
		self.vertex_list=[]
		self.vertex=v
		self.dictionary={}
		a=list_structure(None)
		
		for i in range(1,v+1):
			a=list_structure(i)
			self.vertex_list.append(a)
			
	def edge_relation_by_matrix(self,obj):
		matrix=obj.matrix
		n=0
		head=None
		for i in range(0,self.vertex):
			b=None
			for j in range(0,self.vertex):
				if matrix[i][j]==1:
					b=list_structure(j+1)					
					b.link=self.vertex_list[i].link
					self.vertex_list[i].link=b
			self.dictionary.update({(i+1):self.vertex_list[i]})
			
	def print_adjacency_list(self):
		print('Adjacency List')
		'''for i in range(self.vertex):
			p=[]
			now=self.vertex_list[i]
			while(now.link!=None):
				now=now.link
				p.append(now.val)
			
			print("[",self.vertex_list[i].val,"]-->",p)'''
			
		for i in self.dictionary.keys():
			print(i,'-->',self.dictionary[i])	
	
					
def run(filename):
	
	f=open(filename,'r')
	inp=int(f.readline())
	print("Number of vertex-->",inp)
	f.close()
	
	a=adjacency_matrix(inp,None)
	a.edge_relation()
	a.print_matrix()
	
	b=adjacency_list(inp,None)
	b.edge_relation_by_matrix(a)
	b.print_adjacency_list()
		
run('input.txt')
		
