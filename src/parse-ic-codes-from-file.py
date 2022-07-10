# Open a text file call "idle-codes.txt" and parse the Idle Champion codes from it and write out the codes 
# that match the format below to another text file called "ic-codes-parsed.txt"
# Idle Champion codes are in the format of:
#   XXXX-XXXX-XXXX or XXXX-XXXX-XXXX-XXXX
#  where X is a character in the range of A-Z, 0-9, or !
#  The codes in the file are inline with other text. Each code will be inline with other text and be on their own lines.
#  The codes in the file are not in any particular order.
#  Each code in the file are unique.
#  The text file is extracted from the Idle Champions Discord server, Combinations channel

# import required modules
import re

# function getCodes() takes a list of lines and returns a list of codes
def getCodes(lines):
    # initialize an empty list to store the codes
    codes = []
    # loop through each line in the list
    for line in lines:
        # strip the line of any whitespace
        line = line.strip()
        # if the line is not empty
        if line:
            # parse the line and find the code in the format XXXX-XXXX-XXXX or XXXX-XXXX-XXXX-XXXX
            # where X is a character in the range of A-Z, 0-9, !
            # if the code is found, add it to the list of codes
            code = re.findall(r'[A-Z0-9!]{4}-[A-Z0-9!]{4}-[A-Z0-9!]{4}|[A-Z0-9!]{4}-[A-Z0-9!]{4}-[A-Z0-9!]{4}-[A-Z0-9!]{4}', line)
            if code:
                # append the line to the list of codes
                codes.append(code[0])
    # return the list of codes
    return codes

# function writeCodes() takes a list of codes and writes them to a text file called "ic-codes-parsed.txt"
def writeCodes(codes):
    # open a text file called "ic-codes-parsed.txt" and write the codes to it
    with open("ic-codes-parsed.txt", "w") as f:
        # loop through each code in the list
        for code in codes:
            # write the code to the text file
            f.write(code + "\n")
    # close the text file
    f.close()
    # print a message to the console
    print("Codes written to ic-codes-parsed.txt")
    # return the list of codes
    return codes

# Open a text file call "idle-codes.txt" and parse all lines into a list
with open("idle-codes.txt", "r") as f:
    lines = f.readlines()
    # call function getCodes() to read each line and return a list of codes
    codes = getCodes(lines)
    # call function writeCodes() to write the codes to a text file
    writeCodes(codes)







