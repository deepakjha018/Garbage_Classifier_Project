import streamlit as st
import requests
from PIL import Image


API_URL="http://127.0.0.1:8000/predict"



st.set_page_config(
    page_title="Garbage Classifier",
    page_icon="♻️",
    layout="centered"
)



st.markdown(
"""
<style>


.stApp{
background-color:#0E1117;
}


.title{

text-align:center;
font-size:45px;
font-weight:bold;
color:#16a34a;

}


.subtitle{

text-align:center;
color:gray;
font-size:18px;

}


.result{

padding:20px;
border-radius:12px;
background:#14532d;
color:white;
font-size:20px;

}


</style>


""",
unsafe_allow_html=True
)



st.markdown(
"<div class='title'>♻️ Garbage Image Classifier</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='subtitle'>AI powered waste classification system</div>",
unsafe_allow_html=True
)


st.write("---")


uploaded_file=st.file_uploader(
    "Upload Waste Image",
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
        "Analyzing image..."
    ):


        response=requests.post(

            API_URL,

            files={
                "file":
                (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
        )



    if response.status_code==200:


        data=response.json()


        if "error" in data:

            st.error(
                data["error"]
            )


        else:


            prediction=data["prediction"]

            confidence=data["confidence"]



            st.success(
                f"Prediction : {prediction.upper()}"
            )


            st.progress(
                confidence/100
            )


            st.info(
                f"Confidence : {confidence}%"
            )



            tips={

                "plastic":
                "Recycle plastic waste properly.",

                "paper":
                "Paper waste can be reused or recycled.",

                "cardboard":
                "Flatten cardboard before recycling.",

                "glass":
                "Dispose glass carefully.",

                "metal":
                "Metal items are recyclable.",

                "trash":
                "General waste category."

            }



            if prediction.lower() in tips:

                st.write(
                    "♻️",
                    tips[prediction.lower()]
                )



    else:

        st.error(
            "Server Error"
        )



st.write("---")

st.caption(
    "Built using TensorFlow • FastAPI • Streamlit"
)