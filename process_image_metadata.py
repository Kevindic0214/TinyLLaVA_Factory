import json
import sys
import os
from PIL import Image

testdata=[]
with open('/nfs/RS2416RP/Workspace/spec/TPTS/青春咱的夢.txt', 'r') as file:
    for line in file:
        text = line.strip( )
        text1,text2 = text.split(" ",1)
        image_path='/nfs/RS2416RP/Workspace/spec/TPTS/picture/青春咱的夢/'+ text1
        try:
            text2=text2.replace("\\"," ")
        except:
            text2=text2
        testdata.append(image_path+" "+text2)
with open('/nfs/RS2416RP/Workspace/spec/TPTS/wrong青春咱的夢.txt', 'r') as file:
    for line in file:
        text = line.strip( )
        text1,text2 = text.split(" ",1)
        image_path='/nfs/RS2416RP/Workspace/spec/TPTS/picture/wrong青春咱的夢/'+ text1
        try:
            text2=text2.replace("\\"," ")
        except:
            text2=text2
        testdata.append(image_path+" "+text2)

        
with open('data/青春咱的夢.txt', 'w') as f:
    for line in testdata:
        f.write(line+" \n")
