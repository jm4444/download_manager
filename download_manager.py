# Download Manager
# The purpose of this code is to automatically sort files in my Downloads folder

import magic
import os

for file in os.listdir("../Dummy"):
    print("\nFile Name: " + str(file) + "\n")
    print(magic.from_file("../Dummy/" + str(file)))
#print(magic.from_file("../Dummy/1997.jpg"))
