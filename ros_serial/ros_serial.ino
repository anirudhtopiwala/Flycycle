/* 
 * Button Example for Rosserial
 */

#include <ros.h>
#include <std_msgs/String.h>


ros::NodeHandle nh;

std_msgs::String pushed_msg;

ros::Publisher pub_button("button", &pushed_msg);

const int button45 = 7;
const int button40 = 9;
const int button90 = 11;

void setup()
{
  nh.initNode();
  nh.advertise(pub_button);
  
  pinMode(button45, INPUT);
  pinMode(button40, INPUT);
  pinMode(button90, INPUT);
  
  digitalWrite(button45, HIGH);
  digitalWrite(button40, HIGH);
  digitalWrite(button90, HIGH);
  
}

void loop()
{
 if (button45 == LOW){
    pushed_msg.data = "btn45";
 }
 else if (button40 == LOW){
   pushed_msg.data = "btn40";
 }
 else if (button90 == LOW){
   pushed_msg.data = "btn90";
 }
 else{
   pushed_msg.data = "nobtn";
 }
  pub_button.publish(&pushed_msg);
  nh.spinOnce();
}
