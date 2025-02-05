# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12xrEmKVF_tt0wu3Ou8GSk6vmc6dhn0fb
"""

import os
print(os.listdir('/content'))

import os

# Create a folder named "images" in /content
folder_path = '/content/images'
os.makedirs(folder_path, exist_ok=True)

import shutil

# List all files in /content
for file_name in os.listdir('/content'):
    # Check if it's an image file
    if file_name.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.gif')):
        # Move the image to the folder
        shutil.move(f'/content/{file_name}', f'{folder_path}/{file_name}')

# List all files in the folder
print("Images in the folder:")
print(os.listdir(folder_path))

import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Parameters
image_size = (128, 128)  # Resize images to 128x128
folder_path = '/content/images'

# Create folder for images (if not already done)
os.makedirs(folder_path, exist_ok=True)

# Move all images into the folder
def organize_images():
    for file_name in os.listdir('/content'):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            os.rename(f'/content/{file_name}', f'{folder_path}/{file_name}')
    print("Images moved to folder:", folder_path)

# Preprocessing function
def preprocess_images(folder_path, image_size):
    images = []
    labels = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            # Load and resize the image
            img_path = os.path.join(folder_path, file_name)
            img = load_img(img_path, target_size=image_size)
            img_array = img_to_array(img) / 255.0  # Normalize pixel values to [0, 1]
            images.append(img_array)

            # Binary classification based on file names
            if "class_1" in file_name:  # Check for "class_1" in file name
                labels.append(0)  # Class 0
            elif "class_2" in file_name:  # Check for "class_2" in file name
                labels.append(1)  # Class 1

    return np.array(images), np.array(labels)

# Split data
def split_data(images, labels):
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    # One-hot encode labels
    y_train = to_categorical(y_train, num_classes=2)  # Adjust num_classes for more classes
    y_test = to_categorical(y_test, num_classes=2)

    return X_train, X_test, y_train, y_test

# Main workflow
organize_images()  # Organize images into a folder
images, labels = preprocess_images(folder_path, image_size)  # Preprocess images
X_train, X_test, y_train, y_test = split_data(images, labels)  # Split data

# Check data shapes
print(f"Training images: {X_train.shape}, Training labels: {y_train.shape}")
print(f"Testing images: {X_test.shape}, Testing labels: {y_test.shape}")

print(os.listdir(folder_path))

if "class_1" in file_name:
    labels.append(0)
    print(f"Label 0 assigned to {file_name}")
elif "class_2" in file_name:
    labels.append(1)
    print(f"Label 1 assigned to {file_name}")

!pip install tensorflow scikit-learn

import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Parameters
image_size = (128, 128)  # Resize images to 128x128
folder_path = '/content/images'

# Create folder for images (if not already done)
os.makedirs(folder_path, exist_ok=True)

# Move all images into the folder
def organize_images():
    for file_name in os.listdir('/content'):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            try:
                os.rename(f'/content/{file_name}', f'{folder_path}/{file_name}')
                print(f"Moved: {file_name}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

# Preprocessing function
def preprocess_images(folder_path, image_size):
    images = []
    labels = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(folder_path, file_name)

            # Load and resize the image
            try:
                img = load_img(img_path, target_size=image_size)
                img_array = img_to_array(img) / 255.0  # Normalize pixel values to [0, 1]
                images.append(img_array)

                # Label based on file names
                if "class_1" in file_name:
                    labels.append(0)  # Class 0
                    print(f"Label 0 assigned to {file_name}")
                elif "class_2" in file_name:
                    labels.append(1)  # Class 1
                    print(f"Label 1 assigned to {file_name}")
                else:
                    print(f"Warning: No label for {file_name}")

            except Exception as e:
                print(f"Error processing {file_name}: {e}")

    return np.array(images), np.array(labels)

# Split data
def split_data(images, labels):
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    # One-hot encode labels for multi-class classification
    y_train = to_categorical(y_train, num_classes=2)  # Adjust num_classes if needed
    y_test = to_categorical(y_test, num_classes=2)

    return X_train, X_test, y_train, y_test

# Main workflow
organize_images()  # Organize images into a folder
images, labels = preprocess_images(folder_path, image_size)  # Preprocess images

if images.size > 0 and labels.size > 0:
    X_train, X_test, y_train, y_test = split_data(images, labels)  # Split data
    # Check data shapes
    print(f"Training images: {X_train.shape}, Training labels: {y_train.shape}")
    print(f"Testing images: {X_test.shape}, Testing labels: {y_test.shape}")
else:
    print("No images or labels processed.")

import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Parameters
image_size = (128, 128)  # Resize images to 128x128
folder_path = '/content/images'

# Create folder for images (if not already done)
os.makedirs(folder_path, exist_ok=True)

# Move all images into the folder
def organize_images():
    for file_name in os.listdir('/content'):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            try:
                os.rename(f'/content/{file_name}', f'{folder_path}/{file_name}')
                print(f"Moved: {file_name}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

# Preprocessing function with flexible labeling
def preprocess_images(folder_path, image_size):
    images = []
    labels = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(folder_path, file_name)

            # Load and resize the image
            try:
                img = load_img(img_path, target_size=image_size)
                img_array = img_to_array(img) / 255.0  # Normalize pixel values to [0, 1]
                images.append(img_array)

                # Assign label based on custom conditions
                if "class_1" in file_name:
                    labels.append(0)  # Class 0
                    print(f"Label 0 assigned to {file_name}")
                elif "class_2" in file_name:
                    labels.append(1)  # Class 1
                    print(f"Label 1 assigned to {file_name}")
                else:
                    # If no label found, assign a default label (you can also manually check later)
                    labels.append(0)  # Default to Class 0 or adjust as necessary
                    print(f"Default label 0 assigned to {file_name}")

            except Exception as e:
                print(f"Error processing {file_name}: {e}")

    return np.array(images), np.array(labels)

# Split data
def split_data(images, labels):
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    # One-hot encode labels for multi-class classification
    y_train = to_categorical(y_train, num_classes=2)  # Adjust num_classes if needed
    y_test = to_categorical(y_test, num_classes=2)

    return X_train, X_test, y_train, y_test

# Main workflow
organize_images()  # Organize images into a folder
images, labels = preprocess_images(folder_path, image_size)  # Preprocess images

if images.size > 0 and labels.size > 0:
    X_train, X_test, y_train, y_test = split_data(images, labels)  # Split data
    # Check data shapes
    print(f"Training images: {X_train.shape}, Training labels: {y_train.shape}")
    print(f"Testing images: {X_test.shape}, Testing labels: {y_test.shape}")
else:
    print("No images or labels processed.")

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Define CNN model
model = Sequential()

# Add layers to the model
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))  # Adjust number of output classes

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

import matplotlib.pyplot as plt

# Extract the training and validation accuracy from the history object
train_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

# Plotting the accuracy graph
plt.plot(train_accuracy, label='Training Accuracy')
plt.plot(val_accuracy, label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

# Extract loss values
train_loss = history.history['loss']
val_loss = history.history['val_loss']

# Plot loss vs. epochs
plt.plot(train_loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.title('Training and Validation Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np

# Generate predictions on test data
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Calculate confusion matrix
conf_matrix = confusion_matrix(np.argmax(y_test, axis=1), y_pred_classes)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

from sklearn.metrics import roc_curve, auc

# Compute ROC curve
fpr, tpr, _ = roc_curve(np.argmax(y_test, axis=1), y_pred[:, 1])
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.show()