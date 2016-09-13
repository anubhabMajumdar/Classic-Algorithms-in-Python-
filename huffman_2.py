class node:
	
	def __init__(self,value,fq):
		
		self.value=value
		self.code=[]
		self.fq=fq
		self.left=None
		self.right=None
	
	def add_nodes(self,l,r):
		
		self.left=l
		self.right=r	
		
class heap:
	
	def __init__(self,inp):
			
		self.array=[]
		self.array.append(inp[0])
			
		for i in range(1,len(inp)):
			self.insert(inp[i])
			
	def insert(self,x):
		
		self.array.append(x)
		n=(len(self.array))-1
		self.shift_up(n)
		return
		
	def shift_up(self,c):
		
		p=int(c/2)
		temp=0
					
		if (p>=1):
			if (self.array[p].fq>=self.array[c].fq):
				temp=self.array[c]
				self.array[c]=self.array[p]
				self.array[p]=temp
				
				self.shift_up(p)
			else:
				return
				
	def delete_heap(self,n):
		
		x=self.array[1]
		
		temp=self.array[1]
		self.array[1]=self.array[n]
		self.array[n]=temp
		
		'''n=n-1'''
		
		self.array.remove(x)
		
		
		n=len(self.array)-1
		self.shift_down(1,n)
		
		
		
		return(x)
		
	def shift_down(self,p,k):
		
		c=(2*p)
		
		if c>k:
			return
		if c==k:
			if self.array[c].fq<=self.array[p].fq:
				temp=self.array[c]
				self.array[c]=self.array[p]
				self.array[p]=temp
			return
							
		if self.array[c+1].fq<=self.array[c].fq:
			c=c+1
		
		if self.array[c].fq<=self.array[p].fq:
			temp=self.array[c]
			self.array[c]=self.array[p]
			self.array[p]=temp
		
		self.shift_down(c,k)
				
	def print_heap(self):
		
		for i in range(1,len(self.array)):
			x=self.array[i]
			print(x.value," ",x.fq)

def huffman_encoding(obj):
	
	n=len(obj.array)
	q=obj
	
	for i in range(1,n-1):
		
		'''obj.print_heap()'''
		
		x=obj.delete_heap(len(obj.array)-1)
		y=obj.delete_heap(len(obj.array)-1)
		'''print(x.fq," ",y.fq)'''
		new=node(x.value+y.value,(x.fq+y.fq))
		new.add_nodes(x,y)
		
		obj.insert(new)
	
	'''obj.print_heap()'''
	print()	
	return(obj.delete_heap(len(obj.array)-1))
	
def print_huffman_code(root):
	
	if (root.left==None) & (root.right==None):
		print(root.value,"--->",root.code)
	else:
		if (root.left!=None):
			root.left.code=root.code+"0"
			print_huffman_code(root.left)
		if (root.right!=None):
			root.right.code=root.code+"1"
			print_huffman_code(root.right)
						
			
	
def run(filename):
	
	f=open(filename,'r')
	
	text=f.read()
	text=text.lower()
	dictionary={}
	
	for i in 'abcdefghijklmnopqrstuwxyz':
		dictionary.update({i:0})
	
	for i in text:
		if i in dictionary.keys():
			dictionary[i]+=1	
	
	print(dictionary)
	
	new=node(0,0)
	node_array=[]
	node_array.append(new)
	
	for i in dictionary.keys():
		new=node(i,dictionary[i])
		node_array.append(new)
	
	obj=heap(node_array)
	root=huffman_encoding(obj)
	root.code=""
	
	print_huffman_code(root)
		
		
print("Enter filename")
inp=input()
run(inp)	

