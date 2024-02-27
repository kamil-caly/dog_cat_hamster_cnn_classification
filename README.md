# dog_cat_hamster_cnn_classification

## This project is an implementation of a convolutional neural network for multiclass classification of three types of images: cats, dogs, and hamsters. After processing, there were 1320 images of each type.


1) Model

```python
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
```


2) Results after over 100 epochs training
   
![acc](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/aa5c7af3-68d6-487d-b80b-718bdfe3a8a8)
![loss](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/ebb8ab7b-364e-4155-b627-44a61b97649a)


3) Results after 200 epochs training
![metrics](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/a6eaa26e-b1f4-4dd0-b568-21bc1691b8d9)


4) Confusion matrix: over 100 epochs vs 200 epochs training
   
![confusion_matrix](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/0102ea60-ae66-4675-92ea-813b678397d6)
![conf_matrix2](https://github.com/kamil-caly/dog_cat_hamster_cnn_classification/assets/66841315/5e133e80-09be-4dc4-9913-1700a56468dc)
- The strange and interesting thing is that after 200 epochs of training, the model performs worse in recognizing images of dogs and hamsters.
- The model recognizes images of cats very well. It only incorrectly predicted cats as dogs in 18 cases and incorrectly predicted cats as hamsters in only 2 cases.
- 

6) Possibilities for improvement
- On the 'loss' and 'accuracy' plots, there is potential for further training of the model (although the accuracy on the validation set stops increasing towards the end).
- Additionally, parameters can be adjusted, or a pre-trained model such as 'VGG19' can be applied.


<em>Data was download from: 
- https://images.cv/dataset/hamster-image-classification-dataset
- https://images.cv/dataset/cat-image-classification-dataset
- https://www.tensorflow.org/datasets/catalog/stanford_dogs?hl=pl
 </em>









