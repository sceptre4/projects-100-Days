'''
import os,time

print("Welcome")
print("to")
print("Replit")
time.sleep(1.5)
for i in range(1,1000):
 print(i)
 os.system("cls")
#os.system("clear")

username = input("Username: ")
'''

'''
import os
os.path.abspath("U:\90sTop250a\004) Seal - Kiss From A Rose [1995].mp3"
)
#challenge
#OS.sys.cls,Time.sleep,def
from just_playback import Playback
playback = Playback() # creates an object for managing playback of a single audio file
playback.load_file('U:\90sTop250a\004) Seal - Kiss From A Rose [1995].mp3')
playback.play() # plays loaded audio file from the beginning
'''
'''
from pathlib import Path
print(Path.cwd())
'''
'''
import os
print('Get current working directory : ', os.getcwd())
'''
'''
import pathlib
 
# current working directory
print(pathlib.Path().absolute())
'''
from just_playback import Playback
playback = Playback() # creates an object for managing playback of a single audio file
playback.load_file('BlackOrWhite.mp3')
# or just pass the filename directly to the constructor
playback.play()