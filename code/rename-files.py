import os
import sys
import string
import re
import copy

files = []

# Create a list with the files upto the directory of this file
currentDir = os.path.dirname(os.path.realpath(__file__)).split(os.sep)

# add the path to the files
resourceDir = currentDir
resourceDir.extend(['resources', 'scrambled-images', 'prank'])
resourcePathDir = string.join(resourceDir, os.sep)

prankFiles = next(os.walk(resourcePathDir))[2]

if len(prankFiles) < 0:
    print "No files where found"
    sys.exit()

for filename in prankFiles:
    # If no digits present, skip the file
    if not bool(re.search(r'\d', filename)):
        continue

    # replace the digits
    newFilename = re.sub(r'\d', '', filename)
    # Alternative method to remove all the digits from the filename
    # newFilename = filename.translate(None, "0123456789", filename)

    # rename the file
    currentFilePath = copy.copy(resourceDir)
    currentFilePath.append(filename)
    currentFilePathString = string.join(currentFilePath, os.sep)

    newFilePath = copy.copy(resourceDir)
    newFilePath.append(newFilename)
    newFilePathString = string.join(newFilePath, os.sep)

    os.rename(currentFilePathString, newFilePathString)