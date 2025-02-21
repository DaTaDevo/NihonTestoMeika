import os

def getFileData(file_name: String, list_var):
   pass
   #gets data out of file and stores it into local list

def main():
   with open("file.txt", "r") as file:
      # print(file.seek(0, os.SEEK_END))
      var context: String = file.read()
      print(file.seek(0,os.SEEK_SET))
      print(file.seek(0, os.SEEK_CUR))
      print(file.seek(0, os.SEEK_END))
      print(file.seek(0,os.SEEK_CUR) == file.seek(0, os.SEEK_END))
      # while( file.seek(0,os.SEEK_CUR) != file.seek(0, os.SEEK_END) or True):
         # print("Hello World")
   #1. Get access to file with list of words
   #2. Move words into local list
   #3. Display the list of words in random order   