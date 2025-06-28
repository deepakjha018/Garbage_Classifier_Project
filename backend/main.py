from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from predict import predict_image

app = FastAPI()

# Enable CORS for frontend communication (Streamlit or browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route to check API is running
@app.get("/")
def read_root():
    return {"message": "Garbage Classifier API is running"}

# Predict route
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        temp_file_path = f"temp_{file.filename}"
        
        # Save uploaded image temporarily
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run prediction
        result = predict_image(temp_file_path)

        # Delete temporary image
        os.remove(temp_file_path)

        return result

    except Exception as e:
        return {"error": str(e)}
