import streamlit as st
import tensorflow as tf
import numpy as np
import json
import os

from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array


# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="Garbage Image Classifier",
    page_icon="♻️",
    layout="centered"
)


# ==============================
# CUSTOM CSS
# ==============================

st.markdown(
"""
<style>

.stApp {
    background-color:#0E1117;
}


.title {

    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#22c55e;

}


.subtitle {

    text-align:center;
    color:#9ca3af;
    font-size:17px;

}


.footer {

    text-align:center;
    color:#777;
    margin-top:50px;

}

</style>
""",
unsafe_allow_html=True
)



# ==============================
# LOAD MODEL
# ==============================

@st.cache_resource
def load_ai_model():

    model_path=os.path.join(
        "model",
        "model.keras"
    )


    model=tf.keras.models.load_model(
        model_path
    )


    return model



model=load_ai_model()



# ==============================
# LOAD LABELS
# ==============================

with open(
    os.path.join(
        "model",
        "label_map.json"
    ),
    "r"
) as file:

    label_map=json.load(file)



classes={

    value:key

    for key,value in label_map.items()

}



# ==============================
# PREDICTION FUNCTION
# ==============================

def predict_image(image):


    image=image.convert(
        "RGB"
    )


    image=image.resize(
        (224,224)
    )


    image_array=img_to_array(
        image
    )


    image_array=np.expand_dims(
        image_array,
        axis=0
    )



    prediction=model.predict(
        image_array
    )



    index=np.argmax(
        prediction[0]
    )



    confidence=float(
        np.max(
            prediction[0]
        )
    )



    label=classes[
        index
    ]



    return (

        label,

        round(
            confidence*100,
            2
        )

    )



# ============================
# UI
# ============================


st.markdown(
"""
<style>

.main-title{
text-align:center;
font-size:48px;
font-weight:800;
color:#22c55e;
}


.sub{
text-align:center;
font-size:18px;
color:#9ca3af;
}


.card{

background:#161b22;
padding:25px;
border-radius:15px;
margin-top:20px;

}


.metric{

font-size:22px;
font-weight:bold;

}


</style>

""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="main-title">
♻️ Garbage Image Classifier
</div>

<div class="sub">

AI-powered smart waste classification system using Transfer Learning

</div>

""",
unsafe_allow_html=True
)


st.write("")


col1,col2,col3=st.columns(3)


with col1:

    st.metric(
        "Model",
        "MobileNetV2"
    )


with col2:

    st.metric(
        "Accuracy",
        "86.34%"
    )


with col3:

    st.metric(
        "Classes",
        "6"
    )


st.write("---")


st.info(
"""
Upload an image of waste material and the AI model will classify it into:

📦 Cardboard | 🍾 Glass | 🔩 Metal | 📄 Paper | 🧴 Plastic | 🗑️ Trash
"""
)


uploaded_file=st.file_uploader(

    "📤 Upload Garbage Image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)


if uploaded_file:


    image=Image.open(uploaded_file)


    st.image(

        image,

        caption="Uploaded Image",

        use_container_width=True

    )


    with st.spinner(
        "🧠 AI is analyzing image..."
    ):


        label,confidence=predict_image(
            image
        )


    st.success(

        f"✅ Prediction : {label.upper()}"

    )


    st.progress(
        confidence/100
    )


    st.info(

        f"🎯 Confidence Score : {confidence}%"

    )



    tips={

        "plastic":
        "🧴 Plastic waste should be recycled properly to reduce pollution.",


        "paper":
        "📄 Paper can be reused and recycled to save trees.",


        "cardboard":
        "📦 Flatten cardboard before sending it for recycling.",


        "metal":
        "🔩 Metal waste has high recycling value.",


        "glass":
        "🍾 Separate glass items for safe recycling.",


        "trash":
        "🗑️ Dispose general waste responsibly."

    }



    st.success(
        tips.get(
            label.lower(),
            ""
        )
    )



st.write("---")


st.markdown(
"""
### 🚀 About Project

This deep learning project uses **MobileNetV2 Transfer Learning**
to classify waste images and promote smart recycling.

**Tech Stack**

- Python
- TensorFlow / Keras
- MobileNetV2
- Streamlit

"""
)


st.caption(
"Developed as an upgraded version of Edunet Foundation Internship Project"
)