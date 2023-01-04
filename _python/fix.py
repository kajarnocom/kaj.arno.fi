# python för att fixa på innehåll

import os 
import re

path = "/Users/robertsilen/hugo/kaj.arno.fi/content/post/"
outputpath = "/Users/robertsilen/hugo/kaj.arno.fi/content/output/"

#list all md-files within path given
def list_md_files(path):
    files = []
    for file in os.listdir(path):
        if file.endswith(".md"):
            files.append(file)
    return files

#read file, regex replace and write to outputpath
def searchreplace(inputpath, file, outputpath):
    search = "coverImage: .*"
    with open(inputpath+file, 'r') as f:
        text=f.read()
        try:
            found = re.search(search, text).group(0)
            if found:
                new = found.replace("coverImage: \"", "images: [\"/images/")+"]"
                text = (re.sub(found,new,text))
                with open(outputpath+file, 'w') as f:
                    f.write(text)
        except AttributeError:
            pass

list = list_md_files(path)
for l in list:
    searchreplace(path, l, outputpath)