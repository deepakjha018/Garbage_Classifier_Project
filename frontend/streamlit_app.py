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



# ==============================
# USER INTERFACE
# ==============================


st.markdown(
"<div class='title'>♻️ Garbage Image Classifier</div>",
unsafe_allow_html=True
)



st.markdown(
"<div class='subtitle'>AI Powered Waste Classification System using Deep Learning</div>",
unsafe_allow_html=True
)



st.write("---")



uploaded_file=st.file_uploader(

    "📤 Upload Waste Image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)



if uploaded_file:


    image=Image.open(
        uploaded_file
    )


    st.image(

        image,

        caption="Uploaded Image",

        use_container_width=True

    )



    with st.spinner(
        "🧠 AI is analyzing waste..."
    ):


        label,confidence=predict_image(
            image
        )



    st.success(
        f"✅ Predicted Class : {label.upper()}"
    )



    st.progress(
        confidence/100
    )



    st.info(
        f"🎯 Confidence : {confidence}%"
    )



    recycle_tips={


        "plastic":

        "♻️ Plastic waste should be cleaned and recycled properly.",



        "paper":

        "📄 Paper waste can be reused or sent for recycling.",



        "cardboard":

        "📦 Flatten cardboard boxes before recycling.",



        "metal":

        "🔩 Metal waste is highly recyclable.",



        "glass":

        "🍾 Glass should be separated and recycled safely.",



        "trash":

        "🗑️ Dispose general waste responsibly."


    }



    if label.lower() in recycle_tips:


        st.write(
            recycle_tips[
                label.lower()
            ]
        )



st.write("---")


st.markdown(
"<div class='footer'>Built using TensorFlow • MobileNetV2 • Streamlit</div>",
unsafe_allow_html=True
)