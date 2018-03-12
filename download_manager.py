# Download Manager
# The purpose of this code is to automatically sort files in my Downloads folder

import os

for file in os.listdir("../Downloads"):
    if os.path.isdir("../Downloads/" + str(file)) == True:    # This skips directories
        continue

    if file.lower().endswith(('.exe')):
        print("Installer: " + file)
        os.rename("../Downloads/" + file, "../Downloads/Installers/" + file)
