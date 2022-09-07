
(cl:in-package :asdf)

(defsystem "turtlesim_cleaner-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AngleDistance" :depends-on ("_package_AngleDistance"))
    (:file "_package_AngleDistance" :depends-on ("_package"))
  ))