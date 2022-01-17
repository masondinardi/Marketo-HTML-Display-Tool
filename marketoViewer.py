# imports
import shutil
import re

# Open user input file and copy to temp file location
def file_open(fname):
    
    destination = "temp.html"

    try:
        f = open(fname, 'r')
    except IOError:
        print("ERROR: No file by this name " + fname)    

    try:
        shutil.copy(fname, destination)
        print("file copied succesfully to " + destination)
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    
    dest = open(destination, 'r')
    parse_file(f)

# Parse out all meta tags and save them in a dictionary to be injected into temp file
def parse_file(inp):
    marketoVars = dict()
    valIndex = 0
    for i, line in enumerate(inp):
        #stop if style tag is found
        if "<style>" in line:
            break
        #search for meta tags holding marketo vars
        
        if "<meta" in line:
            if "class" in line:
                
                # extract = re.compile(r'"([^"]*)"')

                #use regex to find id and insert into dictionary
                idSubString = re.findall('id="(.*?)"', line)

                defaultValue = re.findall('default="(.*?)"', line)
                #check if marketo variable is of "mktoNumber" datatype
                if "units" in line:
                    unit = re.findall('units="(.*?)"', line)
                    defaultValue[0] = defaultValue[0] + unit[0]

                marketoVars[idSubString[0]] = defaultValue
                valIndex += 1
                
    print(marketoVars.items())
                        
    

# Driver
def main():
    fname = input("Enter the html file you would like to view : ")
    file_open(fname)


if __name__=="__main__":
    main()