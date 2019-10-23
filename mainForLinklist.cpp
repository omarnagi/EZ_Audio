#include <iostream>
#include <conio.h> // to use getch
using namespace std;
#include "String"
#include "list.h"
#include <fstream>

/* Driver code*/
int main()
{
	/* Start with the empty list */
	Node* head = NULL;

	LinkList modifyList;


	int selection = 0;
	string  url = "";

	cout << "Enter 1 to insert a url \n"
		"Enter 2 to delete a url \n"
		"Enetr 3 to print all url \n"
		"Enter 0 to exit \n"
		"Enter a selection --> ";
	cin >> selection;
	cout << endl;

	while (cin.fail()) {
		cin.clear();
		cin.ignore(numeric_limits<::streamsize>::max(), '\n');

		cout << "invaled input \n";

		cout << "Enter 1 to insert a url \n"
			"Enter 2 to delete a url \n"
			"Enetr 3 to print all url \n"
			"Enetr 4 to see which fle is converting \n"
			"Enter 0 to exit \n"
			"Enter a selection --> ";
		cin >> selection;
		cout << endl;
	}




	while (selection != 0) {
		switch (selection) {
		case 1:
			cout << "get the url --> ";
			//getline(cin, url);	
			cin >> url;
			cout << endl;
			modifyList.insert(&head, url);
			break;
		case 2:
			cout << "delete th ure --> ";
			cin >> url;
			modifyList.deleteItem(&head, url);
			break;
		case 3:
			modifyList.printList(head);
			break;
		case 4:
			modifyList.Convirting(head);
			break;
		default:
			cout << "invalid input \n";
		}


		cout << "Enter 1 to insert a url \n"
			"Enter 2 to delete a url \n"
			"Enetr 3 to print all url \n"
			"Enetr 4 to see which fle is converting \n"
			"Enter 0 to exit \n"
			"Enter a selection --> ";
		cin >> selection;
		cout << endl;

		while (cin.fail()) {
			cin.clear();
			cin.ignore(numeric_limits<::streamsize>::max(), '\n');

			cout << "invaled input \n";

			cout << "Enter 1 to insert a url \n"
				"Enter 2 to delete a url \n"
				"Enetr 3 to print all url \n"
				"Enetr 4 to see which fle is converting \n"
				"Enter 0 to exit \n"
				"Enter a selection --> ";
			cin >> selection;
			cout << endl;
		}
	}

	modifyList.processConvirting(head);


	// Show application close
	cout << "\nEnd of Program"
		<< endl;
	// Pause before application window closes
	cout << "Press any key to exit ..." << endl;
	_getch();
	return 0;

}
