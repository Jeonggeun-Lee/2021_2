;; Auto-generated. Do not edit!


(when (boundp 'turtlesim_cleaner::AngleDistance)
  (if (not (find-package "TURTLESIM_CLEANER"))
    (make-package "TURTLESIM_CLEANER"))
  (shadow 'AngleDistance (find-package "TURTLESIM_CLEANER")))
(unless (find-package "TURTLESIM_CLEANER::ANGLEDISTANCE")
  (make-package "TURTLESIM_CLEANER::ANGLEDISTANCE"))
(unless (find-package "TURTLESIM_CLEANER::ANGLEDISTANCEREQUEST")
  (make-package "TURTLESIM_CLEANER::ANGLEDISTANCEREQUEST"))
(unless (find-package "TURTLESIM_CLEANER::ANGLEDISTANCERESPONSE")
  (make-package "TURTLESIM_CLEANER::ANGLEDISTANCERESPONSE"))

(in-package "ROS")





(defclass turtlesim_cleaner::AngleDistanceRequest
  :super ros::object
  :slots (_angle _distance ))

(defmethod turtlesim_cleaner::AngleDistanceRequest
  (:init
   (&key
    ((:angle __angle) 0.0)
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _angle (float __angle))
   (setq _distance (float __distance))
   self)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; float64 _angle
    8
    ;; float64 _distance
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _angle
     (setq _angle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distance
     (setq _distance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass turtlesim_cleaner::AngleDistanceResponse
  :super ros::object
  :slots (_complete ))

(defmethod turtlesim_cleaner::AngleDistanceResponse
  (:init
   (&key
    ((:complete __complete) nil)
    )
   (send-super :init)
   (setq _complete __complete)
   self)
  (:complete
   (&optional __complete)
   (if __complete (setq _complete __complete)) _complete)
  (:serialization-length
   ()
   (+
    ;; bool _complete
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _complete
       (if _complete (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _complete
     (setq _complete (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass turtlesim_cleaner::AngleDistance
  :super ros::object
  :slots ())

(setf (get turtlesim_cleaner::AngleDistance :md5sum-) "fbefd3cff303f581eade4044f471e589")
(setf (get turtlesim_cleaner::AngleDistance :datatype-) "turtlesim_cleaner/AngleDistance")
(setf (get turtlesim_cleaner::AngleDistance :request) turtlesim_cleaner::AngleDistanceRequest)
(setf (get turtlesim_cleaner::AngleDistance :response) turtlesim_cleaner::AngleDistanceResponse)

(defmethod turtlesim_cleaner::AngleDistanceRequest
  (:response () (instance turtlesim_cleaner::AngleDistanceResponse :init)))

(setf (get turtlesim_cleaner::AngleDistanceRequest :md5sum-) "fbefd3cff303f581eade4044f471e589")
(setf (get turtlesim_cleaner::AngleDistanceRequest :datatype-) "turtlesim_cleaner/AngleDistanceRequest")
(setf (get turtlesim_cleaner::AngleDistanceRequest :definition-)
      "float64 angle
float64 distance
---
bool complete


")

(setf (get turtlesim_cleaner::AngleDistanceResponse :md5sum-) "fbefd3cff303f581eade4044f471e589")
(setf (get turtlesim_cleaner::AngleDistanceResponse :datatype-) "turtlesim_cleaner/AngleDistanceResponse")
(setf (get turtlesim_cleaner::AngleDistanceResponse :definition-)
      "float64 angle
float64 distance
---
bool complete


")



(provide :turtlesim_cleaner/AngleDistance "fbefd3cff303f581eade4044f471e589")


