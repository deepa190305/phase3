import numpy as np
import pandas as pd
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
# Sample structural damage dataset (for predictive maintenance)
data = pd.DataFrame(('damage_level': [20, 30, 50, 65, 80, 95], "time': [1, 2, 3, 4, 5, 6]})
X_train = np.array(data['time']).reshape(-1, 1)
y_train = np.array(data['damage_level']).reshape(-1, 1)
# Build LSTM model for damage prediction
model = Sequential([
tf.keras.layers.Input(shape=(X_train.shape[1], 1)), # Corrected input shape format
LSTM(50, activation='relu'),
Dense(1)
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10, batch_size=2)
# Function to predict future damage levels
def predict_degradation(time_input):
prediction = model.predict(np.array([[time_input]]))
return f"Predicted Damage Level: (float(prediction[0][0]): 2f]%"

# Function for damage detection using OpenCV
def detect_damage(image_path):
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None: # Ensure the image was successfully loaded
return "Error: Unable to load image. Check the file path."
edges = cv2.Canny(image, 100, 200) # Apply edge detection (for crack detection)
cv2.imshow("Detected Damage", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
return "Damage detection completed! Check the displayed image."
def send_alert(damage_severity):
if damage_severity > 70:
return " Critical Structural Damage Alert! Immediate action required."
return

# Example usage:
print(detect_damage[r"C:\Users\krish\OneDrive\Pictures\rusty_bridgeshm.jpg"))
print(predict_degradation(5))
print(send_alert(80))

# Function to send alert if damage is high-risk

Damage severity within safe limits."