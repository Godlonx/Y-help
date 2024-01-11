import hashlib

def getHashPhoto(imgPath):
    with open(imgPath, "rb") as f:
        hash = hashlib.sha256(f.read()).hexdigest()
    return hash

print(getHashPhoto('c:/Users/Remi LAURENT/Documents/Ynov/Hackaton/Y-help/static/images/mail.png'))