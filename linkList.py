


# Node class
class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function is defined in Linked List class
	# Appends a new node at the end. This method is
	# defined inside LinkedList class shown above */
	def insert(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next = new_node

	# Given a reference to the head of a list and a key,
	# delete the first occurence of key in linked list
	def deleteNode(self, key):

		# Store head node
		temp = self.head

		if(temp is None):
			print("List is empty!")
			return

		# If head node itself holds the key to be deleted
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				print(temp.data, " has been deleted successfully")
				temp = None
				return

		# Search for the key to be deleted, keep track of the
		# previous node as we need to change 'prev.next'
		while (temp is not None):
			if temp.data == key:
				print(temp.data, " has been deleted successfully")
				break
			prev = temp
			temp = temp.next

		# if key was not present in linked list
		if (temp == None):
			print("The url you entered is not found")
			return

		# Unlink the node from linked list
		prev.next = temp.next
		temp = None

	# this function is to get what is being converting it should be the fist elements

	def convirting(self):
		temp = self.head

		if(temp is None):
			print("List is empty!")
			return

		print(temp.data, "  is converting")




	# Utility function to print the linked list
	def printList(self):
		temp = self.head

		if (temp is None):
			print("List is empty!")
			return

		while (temp):
			print (temp.data)
			temp = temp.next

	# this function is to convert all file in the list
	def processConvirting(self):
		current = self.head

		while current is not None:
			self.convirting()
			self.deleteNode(current.data)
			current = current.next


	# function to print the menu
	def menu(self):
		print("\nEnter 1 to insert a url \n"
		"Enter 2 to delete a url \n"
		"Enter 3 to print all url \n"
		"Enter 0 to exit \n"
		"Enter a selection --> ")




# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	my_list = LinkedList()

	my_list.menu()
	selection = input()



	while selection != "0":


		if selection == "1":
			url = input("Enter url --> ")
			my_list.insert(url)

		elif selection == "2":
			url = input("Inter url to delete ")
			my_list.deleteNode(url)

		elif selection == "3":
			print('Created linked list is:')
			my_list.printList()
		elif selection == "4":
			my_list.convirting()

		else:
			print("invalid input")


		my_list.menu()
		selection = input()


	my_list.processConvirting()





