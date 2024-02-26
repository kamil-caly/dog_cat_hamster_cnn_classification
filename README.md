# dog_cat_hamster_cnn_classification

## This project is an implementation of a convolutional neural network for multiclass classification of three types of images: cats, dogs, and hamsters.
After processing, there were 1320 images of each type.

1) Model
'''
model = Sequential()
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(units=1024, activation='relu'))
model.add(layers.Dense(units=512, activation='relu'))
model.add(layers.Dense(units=256, activation='relu'))
model.add(layers.Dense(units=3, activation='softmax'))

model.compile(optimizer=optimizers.RMSprop(lr=1e-5),
             loss='categorical_crossentropy',
             metrics=['accuracy'])
'''

2) Results after 80 epochs training (not very good)
![acc](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/aa5c7af3-68d6-487d-b80b-718bdfe3a8a8)
![loss](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/ebb8ab7b-364e-4155-b627-44a61b97649a)

3) Confusion matrix
![confusion_matrix](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/0102ea60-ae66-4675-92ea-813b678397d6)

4) Possibilities for improvement
- On the 'loss' and 'accuracy' plots, there is potential for further training of the model.
- Additionally, parameters can be adjusted, or a pre-trained model such as 'VGG19' can be applied.

<em>Data was download from: 
- https://images.cv/dataset/hamster-image-classification-dataset
- https://images.cv/dataset/cat-image-classification-dataset
- https://www.tensorflow.org/datasets/catalog/stanford_dogs?hl=pl
 </em>









