; Auto-generated. Do not edit!


(cl:in-package bebob2_pkg-msg)


;//! \htmlinclude Pos_XYZ_th.msg.html

(cl:defclass <Pos_XYZ_th> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0)
   (th
    :reader th
    :initarg :th
    :type cl:float
    :initform 0.0))
)

(cl:defclass Pos_XYZ_th (<Pos_XYZ_th>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Pos_XYZ_th>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Pos_XYZ_th)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bebob2_pkg-msg:<Pos_XYZ_th> is deprecated: use bebob2_pkg-msg:Pos_XYZ_th instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Pos_XYZ_th>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bebob2_pkg-msg:x-val is deprecated.  Use bebob2_pkg-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Pos_XYZ_th>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bebob2_pkg-msg:y-val is deprecated.  Use bebob2_pkg-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <Pos_XYZ_th>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bebob2_pkg-msg:z-val is deprecated.  Use bebob2_pkg-msg:z instead.")
  (z m))

(cl:ensure-generic-function 'th-val :lambda-list '(m))
(cl:defmethod th-val ((m <Pos_XYZ_th>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bebob2_pkg-msg:th-val is deprecated.  Use bebob2_pkg-msg:th instead.")
  (th m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Pos_XYZ_th>) ostream)
  "Serializes a message object of type '<Pos_XYZ_th>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'th))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Pos_XYZ_th>) istream)
  "Deserializes a message object of type '<Pos_XYZ_th>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'th) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Pos_XYZ_th>)))
  "Returns string type for a message object of type '<Pos_XYZ_th>"
  "bebob2_pkg/Pos_XYZ_th")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Pos_XYZ_th)))
  "Returns string type for a message object of type 'Pos_XYZ_th"
  "bebob2_pkg/Pos_XYZ_th")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Pos_XYZ_th>)))
  "Returns md5sum for a message object of type '<Pos_XYZ_th>"
  "65f0f7e7047e6c995ec2215d89b172fa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Pos_XYZ_th)))
  "Returns md5sum for a message object of type 'Pos_XYZ_th"
  "65f0f7e7047e6c995ec2215d89b172fa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Pos_XYZ_th>)))
  "Returns full string definition for message of type '<Pos_XYZ_th>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 th~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Pos_XYZ_th)))
  "Returns full string definition for message of type 'Pos_XYZ_th"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 th~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Pos_XYZ_th>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Pos_XYZ_th>))
  "Converts a ROS message object to a list"
  (cl:list 'Pos_XYZ_th
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
    (cl:cons ':th (th msg))
))
