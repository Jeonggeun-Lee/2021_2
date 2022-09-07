; Auto-generated. Do not edit!


(cl:in-package turtlesim_cleaner-srv)


;//! \htmlinclude AngleDistance-request.msg.html

(cl:defclass <AngleDistance-request> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass AngleDistance-request (<AngleDistance-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AngleDistance-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AngleDistance-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtlesim_cleaner-srv:<AngleDistance-request> is deprecated: use turtlesim_cleaner-srv:AngleDistance-request instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <AngleDistance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlesim_cleaner-srv:angle-val is deprecated.  Use turtlesim_cleaner-srv:angle instead.")
  (angle m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <AngleDistance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlesim_cleaner-srv:distance-val is deprecated.  Use turtlesim_cleaner-srv:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AngleDistance-request>) ostream)
  "Serializes a message object of type '<AngleDistance-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AngleDistance-request>) istream)
  "Deserializes a message object of type '<AngleDistance-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AngleDistance-request>)))
  "Returns string type for a service object of type '<AngleDistance-request>"
  "turtlesim_cleaner/AngleDistanceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AngleDistance-request)))
  "Returns string type for a service object of type 'AngleDistance-request"
  "turtlesim_cleaner/AngleDistanceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AngleDistance-request>)))
  "Returns md5sum for a message object of type '<AngleDistance-request>"
  "fbefd3cff303f581eade4044f471e589")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AngleDistance-request)))
  "Returns md5sum for a message object of type 'AngleDistance-request"
  "fbefd3cff303f581eade4044f471e589")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AngleDistance-request>)))
  "Returns full string definition for message of type '<AngleDistance-request>"
  (cl:format cl:nil "float64 angle~%float64 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AngleDistance-request)))
  "Returns full string definition for message of type 'AngleDistance-request"
  (cl:format cl:nil "float64 angle~%float64 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AngleDistance-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AngleDistance-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AngleDistance-request
    (cl:cons ':angle (angle msg))
    (cl:cons ':distance (distance msg))
))
;//! \htmlinclude AngleDistance-response.msg.html

(cl:defclass <AngleDistance-response> (roslisp-msg-protocol:ros-message)
  ((complete
    :reader complete
    :initarg :complete
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AngleDistance-response (<AngleDistance-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AngleDistance-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AngleDistance-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name turtlesim_cleaner-srv:<AngleDistance-response> is deprecated: use turtlesim_cleaner-srv:AngleDistance-response instead.")))

(cl:ensure-generic-function 'complete-val :lambda-list '(m))
(cl:defmethod complete-val ((m <AngleDistance-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader turtlesim_cleaner-srv:complete-val is deprecated.  Use turtlesim_cleaner-srv:complete instead.")
  (complete m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AngleDistance-response>) ostream)
  "Serializes a message object of type '<AngleDistance-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'complete) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AngleDistance-response>) istream)
  "Deserializes a message object of type '<AngleDistance-response>"
    (cl:setf (cl:slot-value msg 'complete) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AngleDistance-response>)))
  "Returns string type for a service object of type '<AngleDistance-response>"
  "turtlesim_cleaner/AngleDistanceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AngleDistance-response)))
  "Returns string type for a service object of type 'AngleDistance-response"
  "turtlesim_cleaner/AngleDistanceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AngleDistance-response>)))
  "Returns md5sum for a message object of type '<AngleDistance-response>"
  "fbefd3cff303f581eade4044f471e589")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AngleDistance-response)))
  "Returns md5sum for a message object of type 'AngleDistance-response"
  "fbefd3cff303f581eade4044f471e589")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AngleDistance-response>)))
  "Returns full string definition for message of type '<AngleDistance-response>"
  (cl:format cl:nil "bool complete~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AngleDistance-response)))
  "Returns full string definition for message of type 'AngleDistance-response"
  (cl:format cl:nil "bool complete~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AngleDistance-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AngleDistance-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AngleDistance-response
    (cl:cons ':complete (complete msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AngleDistance)))
  'AngleDistance-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AngleDistance)))
  'AngleDistance-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AngleDistance)))
  "Returns string type for a service object of type '<AngleDistance>"
  "turtlesim_cleaner/AngleDistance")