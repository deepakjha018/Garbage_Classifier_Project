import os
from PIL import Image
import shutil



RAW_DIR="data/raw"

PROCESSED_DIR="data/processed"


IMAGE_SIZE=(224,224)



def preprocess_images():


    if os.path.exists(
        PROCESSED_DIR
    ):
        shutil.rmtree(
            PROCESSED_DIR
        )


    os.makedirs(
        PROCESSED_DIR,
        exist_ok=True
    )



    for category in os.listdir(
        RAW_DIR
    ):


        source=os.path.join(
            RAW_DIR,
            category
        )


        if not os.path.isdir(
            source
        ):
            continue



        destination=os.path.join(
            PROCESSED_DIR,
            category
        )


        os.makedirs(
            destination,
            exist_ok=True
        )



        for image in os.listdir(source):


            try:

                img=Image.open(
                    os.path.join(
                        source,
                        image
                    )
                ).convert(
                    "RGB"
                )


                img=img.resize(
                    IMAGE_SIZE
                )


                img.save(
                    os.path.join(
                        destination,
                        image
                    )
                )


            except Exception:

                pass



    print(
        "Preprocessing Completed"
    )



if __name__=="__main__":

    preprocess_images()