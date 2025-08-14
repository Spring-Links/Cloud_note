# file=open("grass.txt","r")
# file_write=open("附件","w")
#
# text=file.read()
# file_write.write(text)
#
# file.close()
# file_write.close()




file_read=open('grass.txt', "r")
file_write=open('big_file.txt','w')

while True:
    text=file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()