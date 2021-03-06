import random

pivot_height=0
pivot=None
pivot_parent=None
root=None


class tree:

    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
        self.balance=0

    def add_right(self,right_tree):
        self.right=right_tree

    def add_left(self,left_tree):
        self.left=left_tree

    def print_tree(self):
        print(self.data,"\t",self.balance)

        if self.left!=None:
            self.left.print_tree()
        if self.right!=None:
            self.right.print_tree()

    def insert_node(self,new_tree):
        if self.data>new_tree.data:
            if self.left==None:
                self.add_left(new_tree)
                return
            else:
                self.left.insert_node(new_tree)
        else:
            if self.right==None:
                self.add_right(new_tree)
                return
            else:
                self.right.insert_node(new_tree)

    def compute_height(self):
        if (self.right==None) & (self.left==None):
            h=0
            return h+1
        else:
            if self.left==None:
                hl=0
            else:
                hl=self.left.compute_height()
            if self.right==None:
                hr=0
            else:
                hr=self.right.compute_height()
            h=max(hl,hr)+1
            return h

    def assign_balance_factor(self):
        if self.left==None:
            hl=0
        else:
            hl=self.left.compute_height()
        if self.right==None:
            hr=0
        else:
            hr=self.right.compute_height()

        self.balance=hl-hr

    def set_balance_factor(self):
        self.assign_balance_factor()

        if self.left!=None:
            self.left.set_balance_factor()
        if self.right!=None:
            self.right.set_balance_factor()
        return

    def get_pivot(self):
        global pivot_height,pivot
        if (self.balance==2) | (self.balance==-2):
            if (self.compute_height())<pivot_height :
                pivot_height=self.compute_height()
                pivot=self

        if self.left!=None:
            self.left.get_pivot()
        if self.right!=None:
            self.right.get_pivot()

    def set_pivot_parent(self):
        global pivot,pivot_parent,root
        if (pivot==root):
            pivot_parent=None
            return
        elif(self.left==pivot):
            pivot_parent=self
            return
        elif(self.right==pivot):
            pivot_parent=self
            return
        if self.left!=None:
            self.left.set_pivot_parent()
        if self.right!=None:
            self.right.set_pivot_parent()

    def set_root(self):
        global pivot,root
        root=pivot

    def rotation_type(self,new_tree):
        global pivot,pivot_height
        if (self.balance==2):
            if(self.left.data>new_tree.data):
                print("left-left")
                self.rotate_left_to_left()

            else:
                print("left-right")
                self.rotate_left_to_right()
        elif (self.balance==-2):
            if(self.right.data>new_tree.data):
                print("right-left")
                self.rotate_right_to_left()
            else:
                print("right-right")
                self.rotate_right_to_right()

        else:
            if(self.left!=None):
                self.left.rotation_type(new_tree)
            if(self.right!=None):
                self.right.rotation_type(new_tree)

    def rotate_left_to_left(self):
        global pivot,pivot_parent,root
        a_ptr=pivot.left

        if pivot_parent==None:
            root=a_ptr
        elif pivot_parent.left==pivot:
            pivot_parent.left=a_ptr
        else:
            pivot_parent.right=a_ptr

        pivot.left=a_ptr.right
        a_ptr.right=pivot

        return

    def rotate_right_to_right(self):
        global pivot,pivot_parent,root

        a_ptr=pivot.right

        if pivot_parent==None:
            root=a_ptr
        elif pivot_parent.left==pivot:
            pivot_parent.left=a_ptr
        else:
            pivot_parent.right=a_ptr

        pivot.right=a_ptr.left
        a_ptr.left=pivot

        return

    def rotate_left_to_right(self):
        global pivot,pivot_parent,root
        temp=pivot_parent
        temp_pivot=pivot
        pivot=pivot.left
        root.set_pivot_parent()

        self.left.rotate_right_to_right()

        pivot=temp_pivot
        root.set_pivot_parent()
        self.rotate_left_to_left()

        return

    def rotate_right_to_left(self):

        global pivot,pivot_parent,root
        temp=pivot_parent
        temp_pivot=pivot
        pivot=pivot.right
        root.set_pivot_parent()

        self.right.rotate_left_to_left()

        pivot=temp_pivot
        root.set_pivot_parent()
        self.rotate_right_to_right()

        return

def run():
    global root,pivot,pivot_height
    ch=0
    a_tree=None
    new_tree=None
    new_tree=None
    pivot_height=10000

    while(ch!=4):
        print("1.Create tree\n2.Insert Node\n3.Print tree\n4.Exit\nEnter Choice:")
        ch=int(input())
        print(ch,"\n")
        if ch==1:
            print("Enter Root node Value")
            val=int(input())
            print(val)
            a_tree=tree(val)
            root=a_tree

        elif ch==2:

            a_tree=root
            if(a_tree!=None):
                print("Enter node value")
                val=int(input())
                print(val,"\n")

                new_tree=tree(val)
                a_tree.insert_node(new_tree)

                a_tree=root
                a_tree.set_balance_factor()

                print("Tree after node insertion")
                a_tree.print_tree()

                a_tree=root
                pivot_height=10000
                a_tree.get_pivot()
                a_tree.set_pivot_parent()

                a_tree=pivot
                if (a_tree!=None):
                    a_tree.rotation_type(new_tree)

                    a_tree=root
                    a_tree.set_balance_factor()

                    print("Tree after rotation")
                    a_tree=root
                    a_tree.print_tree()

            else:
                print("Create a tree first")

        elif ch==3:
            a_tree=root
            if a_tree!=None:
                a_tree.print_tree()
            else:
                print("No tree created\n")

        elif ch==4:
            print("You choose to exit\n")

        else:
            print("Wrong Choice\n")


run()
