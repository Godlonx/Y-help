import hashlib

def getHashPhoto(imgPath):
    with open(imgPath, "rb") as f:
        hash = hashlib.sha256(f.read()).hexdigest()
    return hash

print(getHashPhoto('static\images\logo.png'))

hashPicture = getHashPhoto('static\images\highlight\hades.png')


