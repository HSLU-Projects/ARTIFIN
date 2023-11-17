from roboflow import Roboflow


class RoboflowHelper:
    ROBOFLOW_TOKEN = "EQxthA4jdGAzqD67FiyQ"
    MODEL_VERSION = 2

    def __init__(self):
        self.model = Roboflow(api_key=self.ROBOFLOW_TOKEN).workspace().project("artifin").version(self.MODEL_VERSION).model

    def get_prediction(self, image_path, confidence=40, overlap=30):
        predictions = self.model.predict(image_path, confidence=confidence, overlap=overlap).json()['predictions']
        try:
            # Return most likely prediction
            return predictions[0]
        except Exception:
            # No prediction found
            return None
