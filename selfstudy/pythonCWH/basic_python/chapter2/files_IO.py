# types of files 
# text files (.txt, .c)
# binary files (.jpg, .dat)

#functions of file i/o

#open
# f = open("./selfstudy/python_CWH/chapter2/sample.txt","r")
# f = open("./selfstudy/python_CWH/chapter2/sample.txt")            #default mode is read
# data = f.read()
# data = f.read(10)              #reads only first 10 charachters from file
# print(data)
# f.close()

#modes of opening the file 
# r --> reading
# w --> writing
# a --> appending
# + --> updating (read/write) 
# rb --> reads in binary mode
# rt --> reads in text mode 

#readline
#this function reads file and returns one line(line by line)
# data = f.readline()     #firstline
# print(data)
# data = f.readline()     #secondline
# print(data)
# data = f.readline()     #thirdline
# print(data)
#data is changing in every line
# print(data)
# f.close()

#writing file
# f = open('./selfstudy/python_CWH/chapter2/another.txt','w')     #this will create file if not exists and overrite the file
# f.write("this text file is for file i/o\nPerforming write operation")
# f = open('./selfstudy/python_CWH/chapter2/another.txt','a')     #this will create file if not exists and append to it 
# f.write("\nthis text file is for file i/o\nPerforming append operation")
# f.close()

#with statement 
# opens and closes file automatically
# with open("./selfstudy/python_CWH/chapter2/sample.txt","r") as f:
#     print(f.read())

# with open("./selfstudy/python_CWH/chapter2/another.txt","w") as f:
#     print(f.write("something"))

# with open("./selfstudy/python_CWH/chapter2/another.txt","a") as f:
#     print(f.write("\nsomething more"))


# make some programs on file i/o

#replace word from file
# with open("./selfstudy/python_CWH/chapter2/replaceword.txt","w") as f:
#     f.write('''with statement 
# opens and closes file automatically
# with open("./selfstudy/python_CWH/chapter2/sample.txt","r") as f:
#     print(f.read()
# with open("./selfstudy/python_CWH/chapter2/another.txt","w") as f:
#     print(f.write("something")
# with open("./selfstudy/python_CWH/chapter2/another.txt","a") as f:
#     print(f.write("\nsomething more"))''')

# with open("./selfstudy/python_CWH/chapter2/replaceword.txt","r") as f:
#     data = f.read()

# data = data.replace("open","close")

# with open("./selfstudy/python_CWH/chapter2/replaceword.txt","w") as f:
#     f.write(data)
#complete and working

#replace words in file from list
# list = ["open","close","txt"]
# with open("./selfstudy/python_CWH/chapter2/replaceword.txt","w") as f:
#     f.write('''with statement 
# opens and closes file automatically
# with open("./selfstudy/python_CWH/chapter2/sample.txt","r") as f:
#     print(f.read()
# with open("./selfstudy/python_CWH/chapter2/another.txt","w") as f:
#     print(f.write("something")
# with open("./selfstudy/python_CWH/chapter2/another.txt","a") as f:
#     print(f.write("\nsomething more"))''')

# with open("./selfstudy/python_CWH/chapter2/replaceword.txt","r") as f:
#     data = f.read()

# for word in list:
#     data = data.replace(word,"######")

# with open("./selfstudy/python_CWH/chapter2/replaceword.txt","w") as f:
#     f.write(data)
#complete and working
