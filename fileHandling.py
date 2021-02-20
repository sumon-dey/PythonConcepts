# FileHandling

# Opening and Reading File
sampleFile1 = open("SampleFile1.txt", "r")
extractData = sampleFile1.read()
print(extractData)
sampleFile1.close()
print(sampleFile1.closed)
print("*************************************************************")

# Opening and Reading File (using "with")
with open("SampleFile1.txt", "r") as sampleFile1:
    extractData = sampleFile1.read()
    print(extractData)
print(sampleFile1.closed)
print("*************************************************************")

# Other File Handling Methods
sampleFile1 = open("SampleFile1.txt", "r")
sampleFile2 = open("SampleFile1.txt", "r")

# with the multiline file
extractData = sampleFile1.read()
print(extractData)
print(sampleFile1.seek(0))
print(sampleFile1.readline())
print(sampleFile1.readline())
print(sampleFile1.readline())
print(sampleFile1.readline())

# with the binary file
print(sampleFile2.seek(2))
print(sampleFile2.seek(4))
print(sampleFile2.read(1))

# closing both the files
sampleFile1.close()
sampleFile2.close()
print("*************************************************************")
