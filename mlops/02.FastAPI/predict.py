from PIL.Image import Image # pip install pillow
import tensorflow as tf
import numpy as np
from model_loader import model

def predict(image: Image): # pydantic -> type check
    # img => 규격화(인풋 이미지의 사이즈 정규화)
    image = np.asarray(image.resize((224, 224)))[..., :3] # Framework => () 값을 입력을 많이받습니다. | RGB
    print(f'Image first: {image}')
    image = np.expand_dims(image, 0)
    print(f'Image second: {image}')
    image = image / 127.5 - 1.0 # Scaler => -1 ~ 1 사이의 값을 갖게 됩니다.
    print(f'Image third: {image}') # IO => 영상까지도 건들게 되겠죠.
    
    results = tf.keras.applications.imagenet_utils.decode_predictions(
        model.predict(image),
        3
    )
    
    print(results)

    return results