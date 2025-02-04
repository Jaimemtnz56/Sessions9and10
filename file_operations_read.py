fp = open("text.txt") #this is open for reading
print(fp.read()) #print method gets the entire file printed
fp.close() #this is good practice, not really necessary for only reading the file

#There are more pythonic ways of writing this functionality, with a context manager
#Lets print the same thing using it!
with open("text.txt", "r") as f:
    print(f.read())
# no need to close, as when writing smth not indented it will close
# r specifies the way we open the text (read) if we put w it would be to write

#read the file line by line:
with open("text.txt", "r") as f:
    for line in f: #f is iterable and we get each individual line
        print(line, end="") #End will avoid the enter function at the end of each line
        print(line.rstrip()) #Takes out all the spaces and enters from the end of line