import math

class heap:
	
	def __init__(self,array):
		
		self.array=[]
		
		for num in range(len(array)):
            		self.array.append(array[num])
            		self.heapify(num)
		
		self.print_heap()
		print()
		
		n=len(self.array)-1
	
		while n>0:
		    temp=self.array[0]
		    self.array[0]=self.array[n]
		    self.array[n]=temp
		    n-=1
		    self.shift_down(0,n)
		    
			
	def heapify(self,n):
		
		p=math.ceil(n/2)
		temp=0
		if p>=1:
			if (self.array[n].fq>self.array[p].fq):
				temp=self.array[n]
				self.array[n]=self.array[p]
				self.array[p]=temp
				self.heapify(p)
			else:
		    		return
			    	
	def shift_down(self,parent,n):
	    
	    child=(2*parent)+1
	    
	    if child>=n:
	    	return
	    	
	    if self.array[child+1].fq>self.array[child].fq:
	    	child+=1
		
	    if self.array[child].fq>self.array[parent].fq:
	    	temp=self.array[child]
	    	self.array[child]=self.array[parent]
	    	self.array[parent]=temp
	    
	    self.shift_down(child,n)
	    
	    return
	
	def print_heap(self):
		
		for a in self.array:
			print(a.value," ",a.fq)	
		
	def insert(self,value):
	
		self.array.append(value)
		self.heapify()		
		
		n=len(self.array)-1
	
		while n>0:
		    temp=self.array[0]
		    self.array[0]=self.array[n]
		    self.array[n]=temp
		    n-=1
		    self.shift_down(0,n)
		    
	def extract(self):
		
		print(self.array[0])
		x=self.array[0]
		self.array.remove(x)
		
		return(x)
		
	
class node:
	
	def __init__(self,value=None,fq=None):
	
		self.value=value
		self.fq=fq
		self.left=None
		self.right=None
	
	def update(self,x,y):
	
		self.left=x
		self.right=y
		self.fq=x.fq+y.fq
		
class huffman_class:

	def __init__(self,array):
		
		self.new_heap=heap(array)
		self.array=array
		
	def huffman_coding(self):
		
		n=len(self.array)
		q=self.new_heap
		
		for i in range(0,n):
			new=node()
			x=self.new_heap.extract()
			y=self.new_heap.extract()
			
			new.update(x,y)
			self.new_heap.insert(new)
			
		return (self.new_heap.extract())
	
	
def run():
	
	print("Enter number of element-->",end="")
	n=int(input())
	
	node_array=[]
	for i in range(n):
		print("Enter Value-->",end="")
		val=input()
					
		print("Enter frequency-->",end="")
		fq=input()
			
		new=node(val,fq)
		
		node_array.append(new)
	
	'''huf_obj=huffman_class(node_array)
	
	root=huf_obj.huffman_coding()
	
	print_huffman_code(root)'''
	
	obj=heap(node_array)
	obj.print_heap()
	x=obj.extract()
	print(x.value," ",  x.fq)
	
def print_huffman_code(root):

	if (root.left==None) & (root.right==None):
		print(root.value,"	",root.fq)
	else:
		if (root.left!=None):
			print_huffman_code(root.left)
		if (root.right!=None):
			print_huffman_code(root.right)
					
		
run()

			
			
				
		
					
		
		
		
		
		
		
		
		
		
		
		
				
		    			
				
		
		
		
		
		
		
		
		
		
		
