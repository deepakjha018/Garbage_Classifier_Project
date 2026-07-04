from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from predict import predict_image

import shutil
import os
import uuid


app = FastAPI(
    title="Garbage Image Classifier API",
    description="AI based garbage classification system",
    version="2.0"
)


# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():

    return {
        "status": "running",
        "message": "Garbage Classifier API is active"
    }



@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    try:

        os.makedirs(
            "temp",
            exist_ok=True
        )


        extension = file.filename.split(".")[-1]


        filename = (
            str(uuid.uuid4())
            +
            "."
            +
            extension
        )


        filepath=os.path.join(
            "temp",
            filename
        )


        with open(filepath,"wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        result=predict_image(
            filepath
        )


        if os.path.exists(filepath):
            os.remove(filepath)


        return result


    except Exception as e:

        return {
            "error":str(e)
        }