#All the code does at this point is create a Linked List and add 3 items, 'a', 'b' and 'c'.
#All that I want you to do (and this is easy for me to say ) is to add a method called remove() that will
#remove a node from the list. Hint: you can use the search() method to implement the remove() method.
#The final output should look something like this: [remove b from the abc list]

        

class Node : #holds the data and the pointer to next data
        def __init__( self, data ) :
                self.data = data
                self.next = None #points to next node
                self.prev = None

class LinkedList :
        def __init__( self ) : #creates the linked list
                self.head = None                

        def add( self, data ) : #adds nodes to beginning of list
                node = Node( data )
                if self.head == None :  
                        self.head = node
                else :
                        node.next = self.head
                        node.next.prev = node                                           
                        self.head = node                        

        def search( self, k ) :
                p = self.head
                if p != None :
                        while p.next != None : #will look for nodes one at a time
                                if ( p.data == k ) :
                                        return p  #until it finds the data being looked for                              
                                p = p.next
                        if ( p.data == k ) :
                                return p
                return None     

        def __str__( self ) :
                s = ""
                p = self.head
                if p != None :          
                        while p.next != None :
                                s += p.data
                                p = p.next
                        s += p.data
                return s

#new code:
        def remove( self, r ) : #this "rearranges" the nodes, thereby removing the one you want
                r.prev.next = r.next #r's previous then next node (ie, r's current) is set to the next node


# example code
l = LinkedList()

print ("Add: a")
l.add( 'a' )
print ("List = ", l, "\n")

print ("Add: b")
l.add( 'b' )
print ("List = ", l, "\n")

print ("Add: c")
l.add( 'c' )
print ("List = ", l, "\n")

print ("Remove: b")
removeMe = l.search('b')
l.remove(removeMe)
print("List = ", l, "\n")

#practicing to confirm:

l2 = LinkedList()

print ("Add: ant")
l2.add( 'ant' )
print ("List = ", l2, "\n")

print ("Add: bat")
l2.add( 'bat' )
print ("List = ", l2, "\n")

print ("Add: cat")
l2.add( 'cat' )
print ("List = ", l2, "\n")

print ("Add: dog")
l2.add( 'dog' )
print ("List = ", l2, "\n")

print ("Add: ent")
l2.add( 'ent' )
print ("List = ", l2, "\n")

print ("Remove: dog")
l2.remove(l2.search('dog')) #2 steps put on one line
print("List = ", l2, "\n")
