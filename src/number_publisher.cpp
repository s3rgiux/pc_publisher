#include "ros/ros.h"
#include "std_msgs/Int64.h"



int main(int argc, char **argv)
{
  ros::init(argc, argv, "number_publisher");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<std_msgs::Int64>("number", 1);
  ros::Rate loop_rate(2);

  int count = 0;
  while (ros::ok())
  {
    std_msgs::Int64 msg;
    msg.data= count;
    ROS_INFO("Enviado %i", msg.data);
    pub.publish(msg);
    loop_rate.sleep();
    ++count;
  }

  return 0;
}
