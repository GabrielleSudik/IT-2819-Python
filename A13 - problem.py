All the code does at this point is create a Linked List and add 3 items, 'a', 'b' and 'c'.
All that I want you to do (and this is easy for me to say ) is to add a method called remove() that will
remove a node from the list. Hint: you can use the search() method to implement the remove() method.
The final output should look something like this: [remove b from the abc list]

        

class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
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
			while p.next != None :
				if ( p.data == k ) :
					return p				
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



