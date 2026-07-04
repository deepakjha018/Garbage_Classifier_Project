import os
import json
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array



BASE_DIR=os.path.dirname(
    os.path.dirname(__file__)
)



MODEL_PATH=os.path.join(

    BASE_DIR,

    "model",

    "model.keras"

)



LABEL_PATH=os.path.join(

    BASE_DIR,

    "model",

    "label_map.json"

)



model=load_model(
    MODEL_PATH
)



with open(
    LABEL_PATH,
    "r"
) as file:

    label_map=json.load(
        file
    )



reverse_label_map={

    value:key

    for key,value in label_map.items()

}




def predict_image(image_path):


    try:


        image=load_img(

            image_path,

            target_size=(224,224)

        )



        image_array=img_to_array(
            image
        )



        image_array=np.expand_dims(

            image_array,

            axis=0

        )



        predictions=model.predict(
            image_array
        )



        index=np.argmax(
            predictions[0]
        )



        confidence=float(

            np.max(
                predictions[0]
            )

        )



        label=reverse_label_map[
            index
        ]



        return {


            "prediction":label,


            "confidence":round(

                confidence*100,

                2

            )


        }



    except Exception as e:


        return {

            "error":str(e)

        }