import numpy as np
import pandas as pd
import os 
import matplotlib.pyplot as plt
import cv2 
import keras
from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
from keras.models import Sequential
from sklearn.utils import shuffle
import random


train_dir = "c:/users/hamid/pictures"


classes = ["dry", "wet", "hazardous", "recycle"]
len(classes)

one_from_each = []
titles = []
classes = os.listdir(train_dir)
n_classes = len(classes)
for x in classes:
    unique_img_dir = train_dir + "/" + x 
    temp_directory = os.listdir(unique_img_dir)
    temp_img = unique_img_dir + "/" + temp_directory[random.randint(1, 10)]
    image = cv2.imread(temp_img)
    image = np.array(image)
    image = image.astype("float32")/255.0
    one_from_each.append(image)
    titles.append(x)

for i in range(5):
    imageshow = one_from_each[i]
    plt.imshow(imageshow[:,:,::-1])
    plt.title(titles[i])
    plt.show()

print(classes)
labels_dict = {
    0: classes[0],
    1: classes[1], 
    2: classes[2],
    3: classes[3]
}

def load_data(directory):
    size = 150, 150
    images = []
    labels = []

    for folder in os.listdir(directory):
        print("Loading images from : ", folder, ": ", end="")
        for file in os.listdir(directory + "/" + folder):
            img_path = directory + "/" + folder + "/" + file
            curr_img = cv2.imread(img_path)
            curr_img = cv2.resize(curr_img, size)
            images.append(curr_img)
            if folder == labels_dict[0]:
                current_label = 0
            elif folder == labels_dict[1]:
                current_label = 1
            elif folder == labels_dict[2]:
                current_label = 2
            elif folder == labels_dict[3]:
                current_label = 3

            labels.append(current_label)
        print("completed")
    images, labels = shuffle(images, labels)

    images = np.array(image)
    images = images.astype("float32")/255.0
    labels = np.array(labels)
    labels = keras.utils.to_categorical(labels, n_classes)

    return images, labels


X_train, Y_train = load_data(train_dir)


model = Sequential()

model.add(Conv2D(32, kernel_size =[5,5], strides = 2, activation = 'relu', input_shape = (150,150,3)))
model.add(MaxPool2D(pool_size = [2,2], strides = 2))
model.add(Conv2D(64, kernel_size = [3,3], padding = 'same', activation = "relu"))
model.add(Conv2D(64, kernel_size = [3,3], padding = 'same', activation = "relu"))
model.add(MaxPool2D(pool_size = [2,2], strides = 2))
model.add(Conv2D(128, kernel_size = [3,3], activation = "relu"))
model.add(Conv2D(128, kernel_size = [3,3], activation = "relu"))
model.add(MaxPool2D(pool_size = [2,2], strides = 2))
model.add(Conv2D(256, kernel_size = [3,3], activation = "relu"))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(512, activation = 'relu'))
model.add(Dense(n_classes, activation = 'softmax'))

model.summary()


model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model_hist =  model.fit(X_train, Y_train, epochs = 10, validation_split = 0.1, batch_size = 32)


plt.plot(model_hist.history['acc'])
plt.plot(model_hist.history['val_acc'])
plt.title("training vs Validation accuracy")
plt.legend(['train acc.','validation acc.'], loc = 'lower right')
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()

plt.plot(model_hist.history['loss'])
plt.plot(model_hist.history['val_loss'])
plt.title("Loss plot (train vs validation)")
plt.legend(['training loss','validation loss'], loc = 'upper right')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()


# test data
# put model on test data to check results 

# get test data 
# users need to change to your path 
test_dir = "../yzheng070/Desktop/seg_test"

X_test, Y_test = load_data(test_dir)
# get accuracy on test data 
metrics = model.evaluate(X_test, Y_test)
print("Model metrics = ",model.metrics_names)
print("Testing Accuracy = ", metrics[1])