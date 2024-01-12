import hashlib
import os

def getHashPhoto(imgPath):
    with open(imgPath, "rb") as f:
        hash = hashlib.sha256(f.read()).hexdigest()
    return hash


def getPicture(request):
    if 'picture' not in request.files:
        return 'No files sent'
    picture = request.files['picture']
    if picture.filename == '':
        return 'No file selected'
    picture_hash = hashlib.md5(picture.filename.encode()).hexdigest()
    picture_hash_with_extension = picture_hash + ".png"
    picture.save(os.path.join("static/images/highlights", picture_hash_with_extension))
    return picture_hash
