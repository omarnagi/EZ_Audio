//#include "ConvEngine.h"
#include <iomanip>
#include <iostream>
#include <windows.h> 
#include <WinBase.h>
#include <winhttp.h>
//#include <windows.h> 
#include <string>
#include <strsafe.h>
#include <stdio.h>



int main() {
	BOOL showWindowForTesting = true;
	//typedef const char* LPCSTR;
	//char ytdlCommandLineEntry[200] = "youtube-dl.exe --version";
	//char ytdlCommandLineEntry[222] = "youtube-dl.exe --skip-download --get-title https://www.youtube.com/watch?v=PXYrgNBy7CI";

	//"youtube-dl.exe --version";
	/*
	bool noVideo = true;
	if (noVideo) {
		strcat_s(ytdlCommandLineEntry, " -vn");
	}
	*/
	//WinExec(ytdlCommandLineEntry, 11);
	/*
	ShellExecute(NULL, "youtube-dl.exe", "https://www.youtube.com/watch?v=PXYrgNBy7CI", "--version", NULL, SW_SHOWNORMAL);
	system("youtube-dl.exe");
*/


	const char * xd = { " \"https://www.youtube.com/watch?v=kJQP7kiw5Fk \" -f bestaudio" };
	char dx[555] = { " \"https://www.youtube.com/watch?v=kJQP7kiw5Fk \" -f bestaudio" };

	//std::string ee = "https://www.youtube.com/watch?v=kJQP7kiw5Fk";


	char * yturl[999];
	const char* exampleUrl = R"( "https://www.youtube.com/watch?v=kJQP7kiw5Fk" )";
	std::string convArgs = " --ignore-config  ";
	*yturl = _strdup(exampleUrl);
	//*yturl += convArgs;
	//--audio-format mp3 -x 
	//*yturl
	//std::cout << myString;
	//strcpy
	char * ytdlArgs = _strdup(*yturl);

	STARTUPINFO info = { sizeof(info) };
	PROCESS_INFORMATION processInfo;
	CreateProcessA("youtube-dl.exe", ytdlArgs, NULL, NULL, showWindowForTesting, 0, NULL, NULL, &info, &processInfo);


	//system("pause");
	return 0;
}