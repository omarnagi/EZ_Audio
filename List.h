#pragma once

#include <iostream>
#include <conio.h> // to use getch
using namespace std;
#include "String"

// A linked list node  
struct Node
{
public:
	string data;
	Node *next;
	Node *prev;

};

class LinkList {
public:
	void insert(Node** head_ref, string new_data);
	void deleteItem(Node **head_ref, string key);
	void printList(Node *node);
};

void LinkList::insert(Node** head_ref, string new_data)
{
	/* 1. allocate node */
	Node* new_node = new Node();

	Node *last = *head_ref; /* used in step 5*/

	/* 2. put in the data */
	new_node->data = new_data;

	/* 3. This new node is going to be
	the last node, so make next of
	it as NULL*/
	new_node->next = NULL;

	/* 4. If the Linked List is empty,
	then make the new node as head */
	if (*head_ref == NULL)
	{
		*head_ref = new_node;
		return;
	}

	/* 5. Else traverse till the last node */
	while (last->next != NULL)
		last = last->next;

	/* 6. Change the next of last node */
	last->next = new_node;
	return;
}


/* Given a reference (pointer to pointer) to the head of a list
   and a key, deletes the first occurrence of key in linked list */
void LinkList::deleteItem(Node **head_ref, string key)
{


	// Store head node 
	Node* temp = *head_ref;
	Node* prev = *head_ref;

	if (temp == NULL) {
		cout << "List is empty!" << endl;
		return;
	}
	// If head node itself holds the key to be deleted 
	if (temp != NULL && temp->data == key)
	{
		*head_ref = temp->next;   // Changed head 
		free(temp);               // free old head 
		return;
	}

	// Search for the key to be deleted, keep track of the 
	// previous node as we need to change 'prev->next' 
	while (temp != NULL && temp->data != key)
	{
		prev = temp;
		temp = temp->next;
	}

	// If key was not present in linked list 
	if (temp == NULL) {
		cout << "The url you entered is not found \n";
		return;
	}


	// Unlink the node from linked list 
	prev->next = temp->next;

	free(temp);  // Free memory 
}

// This function prints contents of 
// linked list starting from head  
void LinkList::printList(Node *node)
{
	if (node == NULL) {
		cout << "List is empty!" << endl;
		return;
	}

	while (node != NULL)
	{
		cout << node->data << " ";
		node = node->next;
	}
	cout << endl;
}