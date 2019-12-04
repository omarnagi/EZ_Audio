import subprocess 
import pathlib

### To convert, create an instance of converter like "ci = converter()"
### Then you can call "setAudioFormat("flac")" with mp3 or m4a as arguments
### when you want to hit buttons to switch formats
### Can also use "myIntstanceOfConverter.setAudioQuality("228k")" func
### to to set a given bitrate
### When you want to convert, call the transcodeURL func with URL string as only arg
### as in myIntstanceOfConverter.transcodeURL("youtube.com/blablabla")
### See also the example driver program at the bottom


class converter:
   
    def __init__(self):
        self.settingsInstance = convSettings()
        currentDir = pathlib.PureWindowsPath(__file__).parent
        currentDir = currentDir.as_posix()
        self.settingsInstance.directoryLocation(currentDir)
        
    #performs input validation then calls private class
    def setAudioFormat(self, format):
        if format == "mp3":
            self.settingsInstance.setAF("mp3")
        elif format == "m4a":
            self.settingsInstance.setAF("m4a")
        elif format == "flac":
            self.settingsInstance.setAF("mp3")
        elif format == "opus":
            self.settingsInstance.setAF("opus")
        else:
            return False
        return True

    #performs input validation then calls private class
    def setAudioQuality(self, bitrate):
        bps, k = bitrate [:-1], bitrate [-1]
        #print(bps + " " + k)
        bps = int(bps)
        if (k != "k") and (k != "K"): #if 
            return False
        elif (bps > 256):
            return False ##not a sensible input to have >256k
        elif (bps < 32):
            return False
        else:
            self.settingsInstance.setAQ(bitrate)
            return True

    def transcodeURL(self, url):
        self.settingsInstance.assembleString(url)

    
class convSettings:
    alwaysEnabledFlags = " -4 --restrict-filenames -x" 

    def __init__(self): #default values
        self.settings = self.alwaysEnabledFlags
        self.audioFormatString = self.setAF("128k")
        self.audioQualityString = self.setAQ("mp3")

    def directoryLocation(self, curDir):
        self.settings = self.alwaysEnabledFlags + " --ffmpeg-location " \
                        + "\"" + curDir + "/ffmpeg.exe\" "
        self.currentDirectory = curDir
        
    ##below two functions store the formatted string and bitrate of conversion as local vars        
    def setAF(self, aformat = None):
        if aformat is None:
            self.audioFormat = ""
            self.audioFormatString = " "
        else:
            self.audioFormat = aformat
            self.audioFormatString = " --audio-format " + str(aformat)
            
    def setAQ(self, bitrate = None):
        if bitrate is None:
            self.audioQuality = ""
            self.audioQualityString = " "
        else:
            self.audioQuality = bitrate
            self.audioQualityString = " --audio-quality " + str(bitrate)

    def assembleString(self, url):
        #fileDest = " -o \"" + self.currentDirectory + "\"" \
                   #+ "/%(title)s.%(ext)s\" "
        ext =  " /%(title)s.%(ext)s\" "
        s = "youtube-dl.exe" + self.settings + self.audioFormatString \
            + " " + url + ".%(ext)s\" " + ""
        exec = subprocess.run(s)
        return exec
    

###Driver program, for testing. Uncomment these lines to test###
##ci = converter()
##formatBool = ci.setAudioFormat("mp3")
##fo = ci.setAudioQuality("228k")
##print(fo)
##exurl = "https://www.youtube.com/watch?v=1Wytn-_MSBo"
##a = ci.transcodeURL(exurl)
##print(a)
