// Generated by gencpp from file wasp_custom_msgs/image_point.msg
// DO NOT EDIT!


#ifndef WASP_CUSTOM_MSGS_MESSAGE_IMAGE_POINT_H
#define WASP_CUSTOM_MSGS_MESSAGE_IMAGE_POINT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Point.h>
#include <std_msgs/Int64.h>
#include <std_msgs/Int64.h>

namespace wasp_custom_msgs
{
template <class ContainerAllocator>
struct image_point_
{
  typedef image_point_<ContainerAllocator> Type;

  image_point_()
    : ID(0)
    , point()
    , width()
    , height()  {
    }
  image_point_(const ContainerAllocator& _alloc)
    : ID(0)
    , point(_alloc)
    , width(_alloc)
    , height(_alloc)  {
  (void)_alloc;
    }



   typedef int16_t _ID_type;
  _ID_type ID;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _point_type;
  _point_type point;

   typedef  ::std_msgs::Int64_<ContainerAllocator>  _width_type;
  _width_type width;

   typedef  ::std_msgs::Int64_<ContainerAllocator>  _height_type;
  _height_type height;




  typedef boost::shared_ptr< ::wasp_custom_msgs::image_point_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::wasp_custom_msgs::image_point_<ContainerAllocator> const> ConstPtr;

}; // struct image_point_

typedef ::wasp_custom_msgs::image_point_<std::allocator<void> > image_point;

typedef boost::shared_ptr< ::wasp_custom_msgs::image_point > image_pointPtr;
typedef boost::shared_ptr< ::wasp_custom_msgs::image_point const> image_pointConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::wasp_custom_msgs::image_point_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::wasp_custom_msgs::image_point_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace wasp_custom_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'wasp_custom_msgs': ['/home/wasp_vb/wasp_cht2_catkin/src/wasp_custom_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::wasp_custom_msgs::image_point_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::wasp_custom_msgs::image_point_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::wasp_custom_msgs::image_point_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8d6f24f08099975fe78b0257a398b6bb";
  }

  static const char* value(const ::wasp_custom_msgs::image_point_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8d6f24f08099975fULL;
  static const uint64_t static_value2 = 0xe78b0257a398b6bbULL;
};

template<class ContainerAllocator>
struct DataType< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
{
  static const char* value()
  {
    return "wasp_custom_msgs/image_point";
  }

  static const char* value(const ::wasp_custom_msgs::image_point_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#Custom message for publishing a point in an image and getting image data\n\
#image_point.msg\n\
int16 ID\n\
geometry_msgs/Point point\n\
std_msgs/Int64 width\n\
std_msgs/Int64 height\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: std_msgs/Int64\n\
int64 data\n\
";
  }

  static const char* value(const ::wasp_custom_msgs::image_point_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ID);
      stream.next(m.point);
      stream.next(m.width);
      stream.next(m.height);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct image_point_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::wasp_custom_msgs::image_point_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::wasp_custom_msgs::image_point_<ContainerAllocator>& v)
  {
    s << indent << "ID: ";
    Printer<int16_t>::stream(s, indent + "  ", v.ID);
    s << indent << "point: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.point);
    s << indent << "width: ";
    s << std::endl;
    Printer< ::std_msgs::Int64_<ContainerAllocator> >::stream(s, indent + "  ", v.width);
    s << indent << "height: ";
    s << std::endl;
    Printer< ::std_msgs::Int64_<ContainerAllocator> >::stream(s, indent + "  ", v.height);
  }
};

} // namespace message_operations
} // namespace ros

#endif // WASP_CUSTOM_MSGS_MESSAGE_IMAGE_POINT_H
