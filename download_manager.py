# Download Manager
# The purpose of this code is to automatically sort files in my Downloads folder

import os

for file in os.listdir("../"):
    if os.path.isdir("../" + str(file)) == True:    # This skips directories
        continue

    if file.lower().endswith(('.exe', '.whl')):
        os.rename("../" + file, "../Installers/" + file)
    elif file.lower().endswith(('.jpg', '.jpeg', '.png')) or file.lower().endswith(('.gif')):
        os.rename("../" + file, "../Images/" + file)
    elif file.lower().endswith(('.doc', '.docx', '.xls')) or file.lower().endswith(('.xlsx', '.ppt', '.pptx')):
        os.rename("../" + file, "../MicrosoftOffice Files/" + file)
    elif file.lower().endswith(('.pdf')):
        os.rename("../" + file, "../PDFs/" + file)
    else:
        os.rename("../" + file, "../Misc/" + file)
