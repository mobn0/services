from fastapi import UploadFile
from sqlalchemy.orm import Session
from uuid import uuid4
from backend.app.core.config import IMAGESTORE_DB_PATH
from backend.app.apikey.model import Apikey
from backend.app.imagestore.model import StoredImage


async def add_image(uploader: Apikey, image: UploadFile, db: Session) -> StoredImage:
    user = uploader.user

    if not (imagestore_db/str(user.id)).exists():
        imagestore_db.mkdir(str(user.id))
    
    userpath = imagestore_db/str(user.id)
    stored_image_id = uuid4()
    
    storedimage = StoredImage(filename=image.filename, stored_filename=stored_image_id, apikey=uploader)
    db.add(storedimage)
    
    with open(userpath/stored_image_id, "wb") as file:
        file.write(await image.read())
    
    db.commit()

    return storedimage

        
