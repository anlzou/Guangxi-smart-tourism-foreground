/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50051
Source Host           : localhost:3306
Source Database       : sparks-of-fire

Target Server Type    : MYSQL
Target Server Version : 50051
File Encoding         : 65001

Date: 2020-06-27 10:11:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `buy_user_of_scenic_spots`
-- ----------------------------
DROP TABLE IF EXISTS `buy_user_of_scenic_spots`;
CREATE TABLE `buy_user_of_scenic_spots` (
  `scenic_spot_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `buy_date` datetime NOT NULL,
  `use_date` datetime NOT NULL,
  PRIMARY KEY  (`scenic_spot_name`),
  KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of buy_user_of_scenic_spots
-- ----------------------------

-- ----------------------------
-- Table structure for `login`
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `login_time` datetime default NULL,
  `logout_time` datetime default NULL,
  `login_ip` varchar(255) default NULL,
  PRIMARY KEY  (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of login
-- ----------------------------

-- ----------------------------
-- Table structure for `order_user_of_scenic_spots`
-- ----------------------------
DROP TABLE IF EXISTS `order_user_of_scenic_spots`;
CREATE TABLE `order_user_of_scenic_spots` (
  `scenic_spot_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `order_date` datetime NOT NULL,
  `use_date` datetime NOT NULL,
  PRIMARY KEY  (`scenic_spot_name`),
  KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_user_of_scenic_spots
-- ----------------------------

-- ----------------------------
-- Table structure for `scenic_spot`
-- ----------------------------
DROP TABLE IF EXISTS `scenic_spot`;
CREATE TABLE `scenic_spot` (
  `title` varchar(255) NOT NULL,
  `address` varchar(255) default NULL,
  `city` varchar(255) default NULL,
  `theme` varchar(255) default NULL,
  `introduce` text,
  `traffic_guide` text,
  `open_time` text,
  `ticket_information` text,
  `ticket_price` double default NULL,
  `ticket_total` int(11) default NULL,
  `ticket_surplus` int(11) default NULL,
  `stars` int(11) default NULL,
  PRIMARY KEY  (`title`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of scenic_spot
-- ----------------------------

-- ----------------------------
-- Table structure for `signup`
-- ----------------------------
DROP TABLE IF EXISTS `signup`;
CREATE TABLE `signup` (
  `username` varchar(255) NOT NULL,
  `pet_name` varchar(255) default NULL,
  `telephone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY  (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of signup
-- ----------------------------

-- ----------------------------
-- Table structure for `vip_users`
-- ----------------------------
DROP TABLE IF EXISTS `vip_users`;
CREATE TABLE `vip_users` (
  `username` varchar(255) NOT NULL,
  `buy_tickets` int(11) default NULL,
  `orders_tickets` int(11) default NULL,
  PRIMARY KEY  (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of vip_users
-- ----------------------------
