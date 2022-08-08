import shutil
import glob
import os
#this code opens a folder that contains txt files. In these txt files there are lists of locations of other files.
#these file locations are read and the corresponding files are moved to a specific folder

#there are different sequence numbers that correspond to one part number. These sequence number files had to be
#found and moved to their corresponding part number folder to be tested for Automated Testing System discrepancies

#txt_files holds an array with every text file
#in each of these files is the list of all the affected sequence numbers
txt_files= glob.glob(File Locations/*.txt')
folder = glob.glob(path\target folders\*')
def readFile():
    i=0
    for line in txt_files:
            with open(line,'r') as fd:
                #this prints every line in the corresponding txt file, each line will be a location where the sequence number is
                print('target folder: '+folder[i])
                allLocations=fd.read().splitlines()
                print(allLocations)
                for file in allLocations:
                    moveFile(file,folder[i])
            i += 1

def moveFile(originalFile, targetFolder):
    # Use a breakpoint in the code line below to debug your script.
    original = originalFile
    #add this after the target folders part \624016 \1150250 \1153112 \1153114 \51090308
    target = targetFolder

    #this is used to move the files
    # original will hold the line read
    shutil.move(original, target)

if __name__ == '__main__':
    readFile()

