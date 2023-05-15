# %%
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

'''
Készíts egy metódust ami a cifar100 adatbázisból betölti a train és test adatokat. (tf.keras.datasets.cifar100.load_data())
Majd a tanitó, és tesztelő adatokat normalizálja, és vissza is tér velük.


Egy példa a kimenetre: train_images, train_labels, test_images, test_labels
függvény neve: cifar100_data
'''
def cifar100_data():
    (train_images, train_labels), (test_images, test_labels)=tf.keras.datasets.cifar100.load_data()
    train_images = train_images.astype('float32') / 255.0
    test_images = test_images.astype('float32') / 255.0

    return train_images, train_labels, test_images, test_labels

# %%
'''
Készíts egy konvolúciós neurális hálót, ami képes felismerni a képen mi van a 100 osztály közül.
A háló kimenete legyen 100 elemű, és a softmax aktivációs függvényt használja.
Hálon belül tetszőleges számú réteg lehet..


Egy példa a kimenetre: model,
return type: keras.engine.sequential.Sequential
függvény neve: cifar100_model
'''

def cifar100_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(100, activation='softmax'))

    return model


# %%
'''
Készíts egy metódust, ami a bemeneti hálot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy példa a bemenetre: model
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_compile
'''
def model_compile(model):
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
    return model

# %%
'''
Készíts egy metódust, ami a bemeneti hálót feltanítja.

Egy példa a bemenetre: model,epochs, train_images, train_labelsz
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_fit
'''
def model_fit(model, epochs, train_images, train_labels):
    model.fit(train_images, train_labels, epochs=epochs, verbose=1)
    return model

# %%
'''
Készíts egy metódust, ami a bemeneti hálót kiértékeli a teszt adatokon.

Egy példa a bemenetre: model, test_images, test_labels
Egy példa a kimenetre: test_loss, test_acc
return type: float, float
függvény neve: model_evaluate
'''
def model_evaluate(model, test_images, test_labels):
    results = model.evaluate(test_images, test_labels, verbose=0)
    test_loss, test_acc = results[0], results[1]
    return test_loss, test_acc




