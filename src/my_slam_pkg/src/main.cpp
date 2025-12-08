#define _USE_MATH_DEFINES
#include <Eigen/Dense>
#include <functional>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <cmath>

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"

using std::placeholders::_1;

class Slam : public rclcpp::Node {
public:
  Slam() : Node("ScanSubscriber") {
    subscription_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
        "/scan", 10, std::bind(&Slam::ScanCallback, this, _1));
  }

private:
  sensor_msgs::msg::LaserScan current_scan;
  sensor_msgs::msg::LaserScan last_scan;
  std::vector<Eigen::Vector2d> current_xy;
  std::vector<Eigen::Vector2d> last_xy;
  std::vector<Eigen::Vector2d> calc_coords(sensor_msgs::msg::LaserScan scan){
    std::vector<Eigen::Vector2d> xy;
    xy.reserve(scan.ranges.size()); // ensure memory

    for(size_t i = 0; i < scan.ranges.size(); i++){
      float angle = scan.angle_min + i * scan.angle_increment;
      float r = scan.ranges[i];

      // distance check
      if(!std::isfinite(r)) continue;
      if(r < scan.range_min || r > scan.range_max) continue;
      
      Eigen::Vector2d pos(r * std::cos(angle), r * std::sin(angle));
      xy.push_back(pos);
    }
    return xy;
  }

  /*Eigen::Vector3d scan_matching(vector<Eigen::Vector2d> last_xy, vector<Eigen::Vector2d> current_xy){


    Eigen::Vector3d delta;
    delta << ;
    return 
  }*/

  void ScanCallback(const sensor_msgs::msg::LaserScan::SharedPtr msg) const {
    RCLCPP_INFO(this->get_logger(), "I heard:'%f", msg->ranges[0]);
  }
  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Slam>());
  rclcpp::shutdown();
  return 0;
}
