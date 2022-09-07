
(cl:in-package :asdf)

(defsystem "bebob2_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Pos_XYZ_th" :depends-on ("_package_Pos_XYZ_th"))
    (:file "_package_Pos_XYZ_th" :depends-on ("_package"))
  ))