#include<iostream>
#include <string>
#include <conio.h> // For function getch()
using namespace std;
int main()
{
	string url;
	string host;
	
		cout << "Please enter the URL" << endl;
		cin >> url;

		size_t found = url.find_first_of("//");
		host = url.substr(found + 2, 15);

	 if (host != "www.youtube.com")
	{
		cout << "The URL is NOT a YouTube URL  " << endl;
		
	 }
	 else
	 {
		 cout << "Converting..." << endl;
	 }
	 _getch();

	return 0;
}
