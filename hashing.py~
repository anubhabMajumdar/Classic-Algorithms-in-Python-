cp=4
p_list=[]
m=11
hash_table=[]
	
def get_prime_list():
	
	global p_list
	
	f=open('prime_list.txt')
	r=f.read()
	f.close()
	
	p_list=r.split()
	
def string_to_value(name):
	total=0
	for c in name:
		total+=ord(c)
	
	return(total)	
	
def print_hash_table(hash_table):
	
	count=1
	
	for element in hash_table:
		if element[1]==0:
			print(count,"--->",element[0])
		else:
			element[0]=''
			print(count,"--->",element[0])
		count+=1	
	
	print()

def calculate_alpha(ht,m):
	
	count=0
	for item in ht:
		if item[0]!='':
			count+=1
	
	ans=(count/m)*100
	
	return ans		

	
	
def hash_function_one(key):
	global m
	ans=key%m
	return ans		

def hash_function_two(key):
	global cp,p_list
	
	m2=int(p_list[cp-1])
	ans=1+(key%m2)
	return ans

def hash_function(key,i):
	global m
	ans=(hash_function_one(key)+(i*hash_function_two(key)))%m
	return ans	
	
def make_hash_table():
	global m,hash_table
	hash_table=[]
	element=['',0]
	for i in range(m):
		hash_table.append(element)
	
	
def insert(name):
	
	global hash_table,cp,p_list,m
	
	print('Name to be inserted-->',name)
	key=string_to_value(name)
	i=0
	while(i<m):
		#print(hash_function(key,i))
		if (hash_table[hash_function(key,i)][0]=='') | (hash_table[hash_function(key,i)][1]==1):
			l=[name,0]
			hash_table[hash_function(key,i)]=l
			break
		else:
			i=i+1
	
	calc=calculate_alpha(hash_table,m)
	
	if calc>70:
		new_hash_table(name)
	else:
		print('Number of probes required-->',i)
		print('Position-->',hash_function(key,i)+1)
		#print_hash_table(hash_table)
		print('\n')
	
	
def new_hash_table(name):
	global hash_table,cp,p_list,m
	
	print("Load factor>70%\nRe-Hashing the current Hash Table")
	print("Current hash table size-->",m)
	cp+=1
	m=int(p_list[cp])
	print("New hash table size-->",m)
	print()	
	copy=hash_table[:]
	make_hash_table()
	
	for element in copy:
		if element[0]!='':
			insert(element[0])
	
	insert(name)
	

def delete(name):
	global hash_table,cp,p_list,m
	
	print("Name to be deleted-->",name)
	
	key=string_to_value(name)
	i=0
	while(i<m):
		#print(hash_function(key,i))
		if (hash_table[hash_function(key,i)][0]==name):
			l=['',1]
			hash_table[hash_function(key,i)]=l
			break
		else:
			i=i+1
	
	
	if i==m:
		print('Name does not exist\n')
	else:
		print('Number of probes required-->',i)
		print('Position-->',hash_function(key,i)+1)
		#print_hash_table(hash_table)
		print('\n')
	
def search(name):
	global hash_table,cp,p_list,m
	
	print("Name to be searched-->",name)
	
	key=string_to_value(name)
	i=0
	found=0
	while(i<m):
		#print(hash_function(key,i))
		if (hash_table[hash_function(key,i)][0]==name):
			found=1
			break
		else:
			i=i+1
	
	
	if found==0:
		print('Name does not exist\n')
	else:
		print('Number of probes required-->',i)
		print('Position-->',hash_function(key,i)+1)
		#print_hash_table(hash_table)
		print('\n')
			
	
						
		
	
	
	
	
def initialize():
	get_prime_list()
	make_hash_table()
	

def run():
	global hash_table
	
	initialize()	
	make_hash_table()
	
	option=0
	
	while(option!=5):
		
		print('1-->View Hash Table')
		print('2-->Insert name')
		print('3-->Delete name')
		print('4-->Search name')
		print('5-->Quit')
		
		print('Kindly enter your choice-->',end='')
		option=int(input())
		
		print()
		
		if option==1:
			print_hash_table(hash_table)
		elif option==2:
			print("Enter name-->",end='')
			inp=input()
			print()
			insert(inp)
		elif option==3:
			print("Enter name-->",end='')
			inp=input()
			print()
			delete(inp)
		elif option==4:
			print("Enter name-->",end='')
			inp=input()
			print()
			search(inp)
		elif option==5:
			print("Thank You\n")
		else:
			print("Wrong choice\n")	
			



run()











'''insert('anubhab')
insert('ankur')
insert('anubrata')
insert('apala')
insert('aniket')
insert('amitava')
insert('alpana')
insert('ahindranath')
insert('anima')
insert('arunava')
insert('alexender')
insert('asimov')
insert('alaska')
insert('antonio')

delete('alexender')
delete('anubhab')
delete('amitava')
delete('alpana')
delete('asimo')

insert('alexender')
insert('anubhab')
insert('amitava')
insert('alpana')
insert('asimo')

search('anubhab')
delete('anubhab')
search('anubhab')
insert('anubhab')
search('anubhab')

#print_hash_table(hash_table)
'''			
	

