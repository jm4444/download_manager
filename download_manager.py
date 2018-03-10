# Download Manager
# The purpose of this code is to automatically sort files in my Downloads folder

import magic
import os

for file in os.listdir("Downloads"):
    print(file)
