def compareFiles():
    file1 = open("aula06/doc.txt", 'rb')
    #file2 = open(fname, 'rb')
    byte=file1.read(1024)
    print(byte)

compareFiles()