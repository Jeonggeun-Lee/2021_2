// Generated by gencpp from file bebob2_pkg/Pos_XYZ_th.msg
// DO NOT EDIT!


#ifndef BEBOB2_PKG_MESSAGE_POS_XYZ_TH_H
#define BEBOB2_PKG_MESSAGE_POS_XYZ_TH_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace bebob2_pkg
{
template <class ContainerAllocator>
struct Pos_XYZ_th_
{
  typedef Pos_XYZ_th_<ContainerAllocator> Type;

  Pos_XYZ_th_()
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , th(0.0)  {
    }
  Pos_XYZ_th_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , th(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _th_type;
  _th_type th;





  typedef boost::shared_ptr< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> const> ConstPtr;

}; // struct Pos_XYZ_th_

typedef ::bebob2_pkg::Pos_XYZ_th_<std::allocator<void> > Pos_XYZ_th;

typedef boost::shared_ptr< ::bebob2_pkg::Pos_XYZ_th > Pos_XYZ_thPtr;
typedef boost::shared_ptr< ::bebob2_pkg::Pos_XYZ_th const> Pos_XYZ_thConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator1> & lhs, const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.th == rhs.th;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator1> & lhs, const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace bebob2_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
{
  static const char* value()
  {
    return "65f0f7e7047e6c995ec2215d89b172fa";
  }

  static const char* value(const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x65f0f7e7047e6c99ULL;
  static const uint64_t static_value2 = 0x5ec2215d89b172faULL;
};

template<class ContainerAllocator>
struct DataType< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bebob2_pkg/Pos_XYZ_th";
  }

  static const char* value(const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 z\n"
"float32 th\n"
"\n"
;
  }

  static const char* value(const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.th);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Pos_XYZ_th_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bebob2_pkg::Pos_XYZ_th_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "th: ";
    Printer<float>::stream(s, indent + "  ", v.th);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEBOB2_PKG_MESSAGE_POS_XYZ_TH_H
