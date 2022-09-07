import tensorflow.compat.v1 as tf
import pickle
import os 
import cv2, random, math
import numpy as np

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

def load_dataset():
  xlist =[]
  ylist =[]

  #왼쪽 이동 데이터셋
  path = 'WorkSpace/Dataset/0'
  file_list = os.listdir(path)
  for i in range(0,len(file_list)):
      img =cv2.imread(path+"/"+file_list[i])
      xlist.append(img)
      ylist.append([1,0,0])

  #정면 이동 데이터 셋
  path = 'WorkSpace/Dataset/1'
  file_list = os.listdir(path)
  for i in range(0,len(file_list)):
      img =cv2.imread(path+"/"+file_list[i])
      xlist.append(img)
      ylist.append([0,1,0])

  #오른쪽 이동 데이터셋
  path = 'WorkSpace/Dataset/2'
  file_list = os.listdir(path)
  for i in range(0,len(file_list)):
      img =cv2.imread(path+"/"+file_list[i])
      xlist.append(img)
      ylist.append([0,0,1])
 	
  return xlist,ylist

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

def main():
  save_dir = "WorkSpace\CNN_Model\MODEL_2017113547"

  xlist,ylist= load_dataset()
  x_test = np.array(xlist)
  y_test = np.array(ylist)

  x = tf.placeholder(tf.float32, shape=[None, x_test.shape[1], x_test.shape[2], 3])
  y = tf.placeholder(tf.float32, shape=[None, 3])
  prob = tf.placeholder(tf.float32)
  y_pred, logits = build_CNN_classifier(x, prob)
  correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits))
  train_step = tf.train.AdamOptimizer(1e-3).minimize(loss)

  checkpoint_patch = os.path.join(save_dir, "model")
  saver = tf.train.Saver()

  # 세션을 열어 실제 학습을 진행합니다.
  print("%%%%%%%%%%TRAIN START%%%%%%%%%%")
  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(100):
      batch = get_next_batch(10, x_test, y_test)
      train_accuracy = accuracy.eval(feed_dict={x: batch[0], y: batch[1], prob: 1.0})
      loss_print = loss.eval(feed_dict={x: batch[0], y: batch[1], prob: 1.0})
      print("Epoch: %d, accuracy: %f, loss: %f" % (i, train_accuracy, loss_print))
      sess.run(train_step, feed_dict={x: batch[0], y: batch[1], prob: 0.8})
    saver.save(sess, checkpoint_patch)
    sess.close()
  print("%%%%%%%%%TRAIN FINISHED%%%%%%%%%%")
  # 

main()

## 수정 가능 종료 구역
##################################################




