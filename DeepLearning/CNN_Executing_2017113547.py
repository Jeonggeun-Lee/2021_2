import rospy, rospkg
import numpy as np
import cv2, random, math
from DGU_bridge import CvBridge
from sensor_msgs.msg import Image
from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan
import sys
import os
import signal
import DGU
import tensorflow.compat.v1 as tf
import numpy as np

def signal_handler(sig, frame):
    os.system('killall -9 python rosout')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def init_tensorflow():
  #텐서플로어 초기화 *건들지 말것*)
  gpus = tf.config.experimental.list_physical_devices('GPU')
  if gpus:
    # 텐서플로가 첫 번째 GPU만 사용하도록 제한
    try:
      #원격의 안정성을 위해 256으로 고정할 것.
      tf.config.experimental.set_virtual_device_configuration(gpus[0],[tf.config.experimental.VirtualDeviceConfiguration(memory_limit=256)])
    except RuntimeError as e:
      # 프로그램 시작시에 접근 가능한 장치가 설정되어야만 합니다
      print(e)
  old_v = tf.logging.get_verbosity()
  tf.logging.set_verbosity(tf.logging.ERROR)
  tf.disable_v2_behavior()
  tf.reset_default_graph()
  #
init_tensorflow()


bridge = CvBridge()

def lidar_callback(_data):  # lidar 노드에서 데이터 받아 ranges_l에 전달
    global ranges_l 
    ranges_l = _data.ranges #lidar data에서 ranges만 받아서 ranges_l에 저장
    t = ranges_l[90]
    if t<=0.3:
      print(ranges_l[90])

def drive_out(): 
    global pub
    msg = Range()
    msg.min_range = 0
    msg.max_range = 0
    pub.publish(msg)

    
def drive_lidar(range1, range2):
    ok = 0  # cheking the obstacle
    for degree in range(range1, range2): # 62도에서 117도 범위에 라이다가 장애물을 감지할 때 ok변수에 1을 더한다.
        if ranges_l[degree] <= 0.3:
            ok += 1
        if ok > 3: # ok가 3보다 커질때 (앞에 장애물이 있다고 판단) 주행을 멈춘다.
          print("Effect!!")
          drive_out() 
          return True
        else:
          return False
    
def img_callback(data):
    global image
    image = bridge.imgmsg_to_cv2(data, "bgr8")

# publish xycar_motor msg
def drive(Angle, Speed): 
    global pub
    msg = Range()
    msg.min_range = Angle
    msg.max_range = Speed
    pub.publish(msg)


##################################################
## 수정 가능 시작 구역

def build_CNN_classifier(x, prob):
  one_hot_size=3
  
  x_image = tf.reshape(x, [-1, x.shape[1], x.shape[2], x.shape[3]])
  # conv1
  W_conv1 = tf.Variable(tf.truncated_normal(shape=[3, 3, 3, 16], stddev=5e-2))
  b_conv1 = tf.Variable(tf.constant(0.1, shape=[16]))
  h_conv1 = tf.nn.conv2d(x_image, W_conv1, 
                                    strides=[1, 1, 1, 1], 
                                    padding='SAME') + b_conv1
  print("h_conv1 : ")
  print(h_conv1.shape)
  h_conv1 = tf.nn.dropout(h_conv1, prob)
  h_conv1 = tf.nn.relu(h_conv1) # 256, 256, 16
  h_pool1 = tf.nn.max_pool(h_conv1, 
                           ksize=[1, 2, 2, 1], 
                           strides=[1, 2, 2, 1], 
                           padding='SAME') # 128, 128, 16
  print("h_pool1 : ")
  print(h_pool1.shape)
  # conv2
  W_conv2 = tf.Variable(tf.truncated_normal(shape=[3, 3, 16, 16], stddev=5e-2))
  b_conv2 = tf.Variable(tf.constant(0.1, shape=[16]))
  h_conv2 = tf.nn.conv2d(h_pool1, W_conv2, 
                                    strides=[1, 1, 1, 1], 
                                    padding='SAME') + b_conv2
  h_conv2 = tf.nn.dropout(h_conv2, prob)
  h_conv2 = tf.nn.relu(h_conv2) # 128, 128, 16
  print("h_conv2 : ")
  print(h_conv2.shape)
  h_pool2 = tf.nn.max_pool(h_conv2, 
                           ksize=[1, 2, 2, 1], 
                           strides=[1, 2, 2, 1], 
                           padding='SAME') # 64, 64, 16
  print("h_pool2 : ")
  print(h_pool2.shape)
  
  # conv3
  W_conv3 = tf.Variable(tf.truncated_normal(shape=[3, 3, 16, 16], stddev=5e-2))
  b_conv3 = tf.Variable(tf.constant(0.1, shape=[16]))
  h_conv3 = tf.nn.conv2d(h_pool2, W_conv3, 
                                    strides=[1, 1, 1, 1], 
                                    padding='SAME') + b_conv3
  h_conv3 = tf.nn.dropout(h_conv3, prob)
  h_conv3 = tf.nn.relu(h_conv3) # 64, 64, 16
  print("h_conv3 : ")
  print(h_conv3.shape)
  h_pool3 = tf.nn.max_pool(h_conv3, 
                           ksize=[1, 2, 2, 1], 
                           strides=[1, 2, 2, 1], 
                           padding='SAME') # 32, 32, 16
  print("h_pool3 : ")
  print(h_pool3.shape)
  
  # conv4
  W_conv4 = tf.Variable(tf.truncated_normal(shape=[3, 3, 16, 32], stddev=5e-2))
  b_conv4 = tf.Variable(tf.constant(0.1, shape=[32]))
  h_conv4 = tf.nn.conv2d(h_pool3, W_conv4, 
                                    strides=[1, 1, 1, 1], 
                                    padding='SAME') + b_conv4
  h_conv4 = tf.nn.dropout(h_conv4, prob)
  h_conv4 = tf.nn.relu(h_conv4) # 32, 32, 32
  print("h_conv4 : ")
  print(h_conv4.shape)
  h_pool4 = tf.nn.max_pool(h_conv4, 
                           ksize=[1, 2, 2, 1], 
                           strides=[1, 2, 2, 1], 
                           padding='SAME') # 16, 16, 32
  print("h_pool4 : ")
  print(h_pool4.shape)
  
  # conv5
  W_conv5 = tf.Variable(tf.truncated_normal(shape=[3, 3, 32, 32], stddev=5e-2))
  b_conv5 = tf.Variable(tf.constant(0.1, shape=[32]))
  h_conv5 = tf.nn.conv2d(h_pool4, W_conv5, 
                                    strides=[1, 1, 1, 1], 
                                    padding='SAME') + b_conv5
  h_conv5 = tf.nn.dropout(h_conv5, prob)
  h_conv5 = tf.nn.relu(h_conv5) # 16, 16, 32
  print("h_conv5 : ")
  print(h_conv5.shape)
  h_pool5 = tf.nn.max_pool(h_conv5, 
                           ksize=[1, 2, 2, 1], 
                           strides=[1, 2, 2, 1], 
                           padding='SAME') # 8, 8, 32
  print("h_pool5 : ")
  print(h_pool5.shape)
  '''
  # conv6
  W_conv6 = tf.Variable(tf.truncated_normal(shape=[3, 3, 32, 32], stddev=5e-2))
  b_conv6 = tf.Variable(tf.constant(0.1, shape=[32]))
  h_conv6 = tf.nn.conv2d(h_pool5, W_conv6, 
                                    strides=[1, 1, 1, 1], 
                                    padding='SAME') + b_conv6
  h_conv6 = tf.nn.dropout(h_conv6, prob)
  h_conv6 = tf.nn.relu(h_conv6) # 8, 8, 32
  print("h_conv6 : "+h_conv6.shape)
  h_pool6 = tf.nn.max_pool(h_conv6, 
                           ksize=[1, 2, 2, 1], 
                           strides=[1, 2, 2, 1], 
                           padding='SAME') # 4, 4, 32
  print("h_pool6 : "+h_pool6.shape)
  
  
  # Fully connected layer 1
  W_fc1 = tf.Variable(tf.truncated_normal(shape=[4*4*32, 1024], stddev=5e-2))
  b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))
  h_pool6_flat = tf.reshape(h_pool6, [-1, 4*4*32])
  h_fc1 = tf.matmul(h_pool6_flat, W_fc1) + b_fc1
  h_fc1 = tf.nn.dropout(h_fc1, prob)
  h_fc1 = tf.nn.relu(h_fc1)
  print("h_fc1 : "+h_fc1.shape)
  '''

  # Fully connected layer 1
  W_fc1 = tf.Variable(tf.truncated_normal(shape=[8*8*32, 1024], stddev=5e-2))
  b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))
  h_pool5_flat = tf.reshape(h_pool5, [-1, 8*8*32])
  h_fc1 = tf.matmul(h_pool5_flat, W_fc1) + b_fc1
  h_fc1 = tf.nn.dropout(h_fc1, prob)
  h_fc1 = tf.nn.relu(h_fc1)
  print("h_fc1 : ")
  print(h_fc1.shape)
  
  # Fully connected layer 2
  W_fc2 = tf.Variable(tf.truncated_normal(shape=[1024, 1024], stddev=5e-2))
  b_fc2 = tf.Variable(tf.constant(0.1, shape=[1024]))
  h_fc2 = tf.matmul(h_fc1, W_fc2) + b_fc2
  h_fc2 = tf.nn.dropout(h_fc2, prob)
  h_fc2 = tf.nn.relu(h_fc2)
  print("h_fc2 : ")
  print(h_fc2.shape)
  
  # Fully connected layer 3
  W_fc3 = tf.Variable(tf.truncated_normal(shape=[1024, 512], stddev=5e-2))
  b_fc3 = tf.Variable(tf.constant(0.1, shape=[512]))
  h_fc3 = tf.matmul(h_fc2, W_fc3) + b_fc3
  h_fc3 = tf.nn.dropout(h_fc3, prob)
  h_fc3 = tf.nn.relu(h_fc3)
  print("h_fc3 : ")
  print(h_fc3.shape)
  
  # output
  W_output = tf.Variable(tf.truncated_normal(shape=[512, one_hot_size], stddev=5e-2))
  b_output = tf.Variable(tf.constant(0.1, shape=[one_hot_size]))
  logits = tf.matmul(h_fc3, W_output) + b_output
  y_pred = tf.nn.softmax(logits)
  
  return y_pred, logits

def get_next_batch(num, data, labels):
  idx = np.arange(0 , len(data))
  np.random.shuffle(idx)
  idx = idx[:num]
  data_shuffle = [data[ i] for i in idx]
  labels_shuffle = [labels[ i] for i in idx]
  return np.asarray(data_shuffle), np.asarray(labels_shuffle)

## 수정 가능 종료 구역
##################################################

  
def main():
  global pub
  global image
  pub = None
  
  image = np.empty(shape=[0])
  
  rospy.init_node('auto_drive')
  pub = rospy.Publisher('xycar_motor', Range, queue_size=1)
  image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, img_callback)
  rospy.Subscriber('/scan', LaserScan, lidar_callback, queue_size=1) 

  dir_id = 0

##################################################
## 수정 가능 시작 구역
  
  SAVE_DIR = "WorkSpace\CNN_Model\MODEL_2017113547"
  ckpt = tf.train.get_checkpoint_state(SAVE_DIR)

  if ckpt and ckpt.model_checkpoint_path:
    x = tf.placeholder(tf.float32, shape=[None, 256, 256, 3])
    y = tf.placeholder(tf.float32, shape=[None, 3])
    prob = tf.placeholder(tf.float32)
    y_pred, logits = build_CNN_classifier(x, prob)
    
    checkpoint_patch = os.path.join(SAVE_DIR, "model")
    saver = tf.train.Saver()

    with tf.Session() as sess:      
      sess.run(tf.global_variables_initializer())
      saver.restore(sess, ckpt.model_checkpoint_path)
      print("---------- Xycar A2 v1.0.1 ----------")
      rospy.sleep(2)
      print("**test**")
      while True:
        while not image.size == (640*480*3):
          continue  
        DGU.imshow(1,image)

        angle=0
        xlist =[]
        ylist =[]
        xlist.append(cv2.resize(image, (256, 256)))
        ylist.append([0,0,0])
        x_test = np.array(xlist)
        y_test = np.array(ylist)
        batch = get_next_batch(1, x_test, y_test)
        y_result = sess.run(logits, feed_dict={x: batch[0],y: batch[1], prob: 1.0})
        dir_id = y_result.argmax()

## 수정 가능 종료 구역
##################################################

        term_angle =10

        if dir_id==1:
          angle = 0
        elif dir_id==0:
          angle = -term_angle
        elif dir_id==2:
          angle = term_angle
        else:
          angle = 0
        
        drive(angle, 6)
        
        cv2.waitKey(1)
    
main()
