#include<iostream>
#include <string>
using namespace std;
int main()
{
	string url;
	string host;
	
		cout << "Please enter the URL" << endl;
		cin >> url;

		size_t found = url.find_first_of("//");
		host = url.substr(found + 2, 15);

	 while (host != "www.youtube.com")
	{
		cout << "the URL is NOT a YouTube URL  " << endl;
		cout << "Please enter a new URL " << endl;
		cin >> url;
		size_t found = url.find_first_of("//");
		host = url.substr(found + 2, 15);
	}
	cout << "the URL is a YouTube URL  " << endl;

	return 0;
}
