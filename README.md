# Defect Detection and Classification with MobileNet-V2

### Task:
the aim of the project is to classify the images and, if the image is defective, detect the location of the defect.

### Project Information:
- Dataset: (Class 1, Class 2 and Class 3 used):
  - In the dataset, 1000 normal and 750 abnormal images were selected for each class. There are 3 classes in total. 2400 normal images and 2160 abnormal  images were randomly selected for training.
  - 5250 images in total, 4560 for training, 690 for testing.
  -All data distributions are equal.
  
- Used model for classification: **MobileNet-V2** 
  -Although different state-of-the-art models such as ResNet18, MobileNet-V3 and Densenet-121 have been tried, the best model has been MobileNet-V2 in  terms of inference speed and model success.
 
- Used model for detection : **YoloV4_tiny**
  - Yolov4-tiny has been better than other models  in terms of inference speed and model success.

- Environment:
  - Python 3.8.5
  - Required packages are given in requirements.txt.
  
  
### Usage
- Inference on test images for classification:
```
python3 test_classifier.py checkpoints/model_epoch_23.pth data/test/class2_withdef/121.png
```
- Inference on test images for detection:
 ```
 python3 test_detection.py detection/weights_best.pth data/test/class2_withdef/121.png
 ```
 - train for classification
 ```
 python3 train_class_torch.py 
 ```

  


