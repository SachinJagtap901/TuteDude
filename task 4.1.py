try:
    file1 = open("file1.txt","r+")
    print(file1.read())
except FileNotFoundError:
    print(f"Error : The file {file1} was not found.")
finally:
    print("Continue with the following code")

file1 = open("file1.txt","r+")
read_file = file1.read()
print(f"Reading the File Contents:\n",read_file)
file1.close()

