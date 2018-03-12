# Download Manager
# The purpose of this code is to automatically sort files in my Downloads folder

import os

for file in os.listdir("../Downloads"):
    if os.path.isdir("../Downloads/" + str(file)) == True:    # This skips directories
        continue

    if file.lower().endswith('.exe'):
        print("Installer: " + file)
        os.rename("../Downloads/" + file, "../Downloads/Installers/" + file)
    elif file.lower().endswith(('.jpg', '.jpeg', '.png')) or file.lower().endswith(('.gif')):
        os.rename("..Downloads/" + file, "../Downloads/Images/" + file)
    elif file.lower().endswith(('.doc', '.docx', '.xls')) or file.lower().endswith(('.xlsx', '.ppt', '.pptx')):
        os.rename("../Downloads/" + file, "../Downloads/MicrosoftOffice Files/" + file)
    elif file.lower().endswith(('.pdf')):
        os.rename("../Downloads/" + file, "../Downloads/PDFs/" + file)
    else:
        os.rename("../Downloads/" + file, "../Downloads/Misc/" + file)
