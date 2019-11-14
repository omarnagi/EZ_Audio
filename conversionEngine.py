import time #for sleep functionality
import subprocess #for system calls
import os
import pathlib

class Flags():

    ytdlFlags = ""
    #below line uses IPv4 for connection to avoid 426 errors
    #also restrict filenames to avoid filesystem issues on Windows
    alwaysEnabled = " -4 --restrict-filenames"

    #These flags/settings can be fleshed out with setter functions
    #Those functions then would be activated by the GUI
    audioFormat = " --audio-format m4a"
    writeMetadataToFile = " --add-metadata"

    #default constructor-like function
    def __init__(self):
        Flags.ytdlFlags = "" + Flags.alwaysEnabled
        if audioFormat != NULL:
            Flags.ytdlFlags += audioFormat
        if writeMetaDataToFile != NULL:
            Flags.ytdlFlags += audioFormat            

    #called by main function
    def obtain ():
        return Flags.ytdlFlags
        


currentDir = pathlib.PureWindowsPath(__file__).parent
currentDir = currentDir.as_posix()

ytString=r'https://www.youtube.com/watch?v=gvdf5n-zI14'

#
#Videos you can use for testing
#
#long video https://www.youtube.com/watch?v=wZZ7oFKsKzY
#
#short video https://www.youtube.com/watch?v=gvdf5n-zI14

ytdlExecString = "youtube-dl.exe"
ytdlFlagsString = Flags.obtain() 
#ytdlFlagsString = " -4 --restrict-filenames -x -q"
ytdlPathString1 = " -o \""
dlFileNameString="/%(title)s.%(ext)s\""
ytdlcliString=( ytdlExecString + ytdlFlagsString + ytdlPathString1
                 + currentDir + dlFileNameString + " " + ytString)
ytdl_exec = subprocess.run(ytdlcliString)

print(ytdl_exec)






