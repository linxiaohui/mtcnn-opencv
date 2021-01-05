MTCNN-OpenCV
============
MTCNN Face Detector using OpenCV, no reqiurement for tensorflow/pytorch.

# INSTALLATION
   * `pip3 install opencv-python` or `pip3 install opencv-python-headless`
   * `pip3 install mtcnn-opencv`

# USAGE
```python
import cv2
from mtcnn_cv2 import MTCNN

detector = MTCNN()
test_pic = "t.jpg"

image = cv2.cvtColor(cv2.imread(test_pic), cv2.COLOR_BGR2RGB)
result = detector.detect_faces(image)

# Result is an array with all the bounding boxes detected. Show the first.
print(result)

if len(result) > 0:
    keypoints = result[0]['keypoints']
    
    cv2.rectangle(image,
                  (bounding_box[0], bounding_box[1]),
                  (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0,155,255),
                  2)
    
    cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)
    
    cv2.imwrite("result.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

# 生成标记了的人脸的图片
with open(test_pic, "rb") as fp:
    marked_data = detector.mark_faces(fp.read())
with open("marked.jpg", "wb") as fp:
    fp.write(marked_data)
```
