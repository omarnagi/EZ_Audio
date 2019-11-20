import subprocess 
import pathlib 

##Call this function to download and transcode a given video
##Must be called with a string for valid YT video as first argument
##Second argument is optional, a number 0 (best quality) thru
##  9 (smallest file size) to specify file size and quality
##Third argument, optional, is a string that specifies a format for end audio file

def ytdlExec(videoString, audioQuality = 5, audioFormat = "mp3"):
    
    def ytdlFlags(aquality, aformat):  
        alwaysEnabledFlags = " -4 --restrict-filenames -x --ffmpeg-location "
        audioQualityFlag = " --audio-quality " + str(aquality)
        audioFormatFlag = " --audio-format " + str(aformat)
        flagString = audioQualityFlag + audioFormatFlag + alwaysEnabledFlags
        return flagString

    currentDir = pathlib.PureWindowsPath(__file__).parent
    currentDir = currentDir.as_posix()
    ytdlExecString = "youtube-dl.exe "
    ytdlPathString1 = " -o \""
    dlFileNameString="/%(title)s.%(ext)s\""
    ytdlFlagsString = ytdlFlags(audioQuality, audioFormat) + "\"" + currentDir \
                    + "/ffmpeg.exe\" " + ytdlPathString1 \
                    + currentDir + dlFileNameString
    videoString = " " + videoString
 
    ytdlcliString = ytdlExecString + ytdlFlagsString + videoString
    print(ytdlcliString)
    ytdl_exec = subprocess.run(ytdlcliString)
    return


###Driver program, for testing. Uncomment these two lines to test###
#ytString="https://www.youtube.com/watch?v=z8RkR4rd7dM"
#ytdlExec(ytString)
