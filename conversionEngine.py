import subprocess #for system calls
import os
import pathlib


class ytdlFlags():  
    alwaysEnabledFlags = "-4 --restrict-filenames -x --ffmpeg-location "
    flagString = ""  + alwaysEnabledFlags

currentDir = pathlib.PureWindowsPath(__file__).parent
currentDir = currentDir.as_posix()

ytString="https://www.youtube.com/watch?v=gvdf5n-zI14"
#
#Videos you can use for testing
#
#long video https://www.youtube.com/watch?v=wZZ7oFKsKzY
#
#short video https://www.youtube.com/watch?v=gvdf5n-zI14

ytdlExecString = "youtube-dl.exe"
ytdlFlagsString = ytdlFlags.flagString
ytdlPathString1 = " -o \""
dlFileNameString="/%(title)s.%(ext)s\""
ytdlcliString = (ytdlExecString + " " + ytdlFlagsString + "\""
                 + currentDir + "/ffmpeg.exe\" " + ytdlPathString1
                 + currentDir + dlFileNameString + " " + ytString)
ytdl_exec = subprocess.run(ytdlcliString)

print(ytdl_exec)
print(ytdlcliString)






