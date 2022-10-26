import glob
import os
from logging import INFO, getLogger
from typing import List

from fastapi import FastAPI, Response
from pydantic import BaseModel

# 自分で変更
media_file_path = "../dummy_media"


class Media(BaseModel):
    title: str


logger = getLogger(__name__)
logger.setLevel(INFO)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/media", response_model=List[Media])
async def get_media_list():
    media_files = glob.glob(media_file_path + "/*")
    return [Media(title=file) for file in media_files]


# TODO:クエリをtitleじゃなくてuniqueなパラメータにしたい
@app.delete("/api/v1/media/{title}")
async def delete_media(title: str):
    try:
        os.remove(media_file_path + "/" + title)
        return Response(content="success", status_code=200)
    except OSError as e:
        logger.error(e)
