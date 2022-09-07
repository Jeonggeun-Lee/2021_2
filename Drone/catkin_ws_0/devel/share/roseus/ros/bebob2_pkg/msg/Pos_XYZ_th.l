;; Auto-generated. Do not edit!


(when (boundp 'bebob2_pkg::Pos_XYZ_th)
  (if (not (find-package "BEBOB2_PKG"))
    (make-package "BEBOB2_PKG"))
  (shadow 'Pos_XYZ_th (find-package "BEBOB2_PKG")))
(unless (find-package "BEBOB2_PKG::POS_XYZ_TH")
  (make-package "BEBOB2_PKG::POS_XYZ_TH"))

(in-package "ROS")
;;//! \htmlinclude Pos_XYZ_th.msg.html


(defclass bebob2_pkg::Pos_XYZ_th
  :super ros::object
  :slots (_x _y _z _th ))

(defmethod bebob2_pkg::Pos_XYZ_th
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:th __th) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _th (float __th))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:th
   (&optional __th)
   (if __th (setq _th __th)) _th)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; float32 _th
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _th
       (sys::poke _th (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _th
     (setq _th (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get bebob2_pkg::Pos_XYZ_th :md5sum-) "65f0f7e7047e6c995ec2215d89b172fa")
(setf (get bebob2_pkg::Pos_XYZ_th :datatype-) "bebob2_pkg/Pos_XYZ_th")
(setf (get bebob2_pkg::Pos_XYZ_th :definition-)
      "float32 x
float32 y
float32 z
float32 th


")



(provide :bebob2_pkg/Pos_XYZ_th "65f0f7e7047e6c995ec2215d89b172fa")


