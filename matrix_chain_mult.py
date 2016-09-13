import sys

class matrix:
	
	def __init__(self,row,column):
		self.row=row
		self.column=column
		
	def display(self):
		print(self.row," ",self.column)
		
class matrix_chain_mult:
	
	def __init__(self,p,matrix_chain=None):
		self.matrix=matrix_chain
		self.p=p
		self.m=[]
		self.s=[]
		
		n=len(self.p)
		
		for i in range(n):
			a=[]
			b=[]
			for j in range(n):
				a.append(sys.maxsize-1)
				b.append(0)
			self.m.append(a)
			self.s.append(b)
			
		
	def matrix_chain_order(self):	
		
		n=len(self.p)
		n-=1
		
		for i in range(1,n+1):
			self.m[i][i]=0
			
		for l in range(2,n+1):
			for i in range(1,(n-l+1)+1):	
			
				j=i+l-1
				for k in range(i,j):
					q=self.m[i][k]+self.m[k+1][j]+(self.p[i-1]*self.p[k]*self.p[j])
			
					if (q<self.m[i][j]):
						self.m[i][j]=q
						self.s[i][j]=k
						
		print("Number of scaler multiplication-->",self.m[1][n])
		
	def print_parentheis(self,i,j):
		
		if (i==j):
			print(i,"",end='')
		else:
			print("(",end='')
			self.print_parentheis(i,self.s[i][j])	
			self.print_parentheis(self.s[i][j]+1,j)
			print(")",end='')
		
		
def run():
	
	p=[]
	print("Enter number of matrix")
	length=int(input())
	
	for i in range(length+1):
		print("Enter p[",i,"]-->",end='')
		inp=int(input())
		p.append(inp)
		
	m=matrix_chain_mult(p)
	m.matrix_chain_order()
	m.print_parentheis(1,length)
	print()	

run()			
		
