import os
import subprocess

"""
Returns the absolute path to the relative path that was specified
    @param file  The file which's path is requested. Can specify file in multiple subfolders
    @return  The absolute path to the file
"""
def getPathToFile(file):
        directory = os.getcwd()
        joined = os.path.join(directory, file)
        return joined

"""
Unzips a specified '.laz' file to a '.las' file. By default this method uses the
'laszip-cli.exe' located in the current directory
"""
def unzipLAZFile(pathToFile, pathToLASZIP=getPathToFile("laszip-cli.exe")):
    subprocess.call([pathToLASZIP, pathToFile])
