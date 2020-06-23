/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50051
Source Host           : localhost:3306
Source Database       : sparks-of-fire

Target Server Type    : MYSQL
Target Server Version : 50051
File Encoding         : 65001

Date: 2020-06-20 10:23:08

Last Author: anlzou
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `buy_user_of_scenic_spots`
-- describe `用户购买某个景点的票，该表保存相关信息`

-- ----------------------------
DROP TABLE IF EXISTS `buy_user_of_scenic_spots`;
CREATE TABLE `buy_user_of_scenic_spots` (
  `scenic_spot_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `buy_date` datetime NOT NULL,
  `user_date` datetime NOT NULL,
  PRIMARY KEY  (`scenic_spot_name`),
  KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of buy_user_of_scenic_spots

-- ----------------------------
INSERT INTO `buy_user_of_scenic_spots` VALUES ('桂林', 'an', '2020-06-20 09:58:52', '2020-06-21 09:58:59');
INSERT INTO `buy_user_of_scenic_spots` VALUES ('通灵峡谷', 'an', '2020-06-20 09:59:43', '2020-06-22 09:59:46');

-- ----------------------------
-- Table structure for `login`
-- describe `用户登录表，该表保存相关信息`

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
INSERT INTO `login` VALUES ('anlzou', '599502931@qq.com', 'anlzou', null, null, null);
INSERT INTO `login` VALUES ('an', '123456@qq.com', 'an', null, null, null);

-- ----------------------------
-- Table structure for `order_user_of_scenic_spots`
-- describe `用户预定某个景点的票，该表保存相关信息`

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
INSERT INTO `order_user_of_scenic_spots` VALUES ('桂林', 'an', '2020-06-20 10:16:00', '2020-06-24 10:16:03');

-- ----------------------------
-- Table structure for `scenic_spot`
-- describe `景点表，该表保存相关信息`

-- ----------------------------
DROP TABLE IF EXISTS `scenic_spot`;
CREATE TABLE `scenic_spot` (
  `scenic_spot_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `total_tickets` int(11) default NULL,
  `surplus` int(11) default NULL,
  `price` double default NULL,
  `open_time` time default NULL,
  `close_time` time default NULL,
  `stars` int(11) default NULL,
  `introduce` text,
  PRIMARY KEY  (`scenic_spot_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of scenic_spot
-- ----------------------------
INSERT INTO `scenic_spot` VALUES ('通灵峡谷', '广西通灵峡谷', '400', '300', '100.5', '08:00:00', '18:00:00', '4', '通灵大峡谷国家AAAA级别风景区位于广西百色市靖西县境内，地处北回归线以南，云贵高原南缘，距广西首府南宁230公里，属那亚热带地区。\r\n通灵大峡谷全长3.8公里，由通灵峡、念八峡及地下暗河、隧道贯通连接，通天彻地，灵气飘逸。峡谷绝壁千仞，幽幽深邃，巨型钟乳石高崖倒悬，古树老藤遮天蔽日，神秘莫测的洞穴、深潭星罗棋布。水帘洞、地下河及气象万千的瀑布，河涧曲回，流水潺潺，满谷青翠欲滴。通灵大峡谷原来是一个盲谷，由于地壳运动的影响，天行地运，形成一个大天坑，四周悬崖峻峭，气势壮观。高深的峡谷，清澈的溪流，苍翠的植被和188.6米的通灵大瀑布交相辉映，使整个峡谷充满了活力和灵性。');
INSERT INTO `scenic_spot` VALUES ('桂林', '广西桂林', '600', '300', '200.5', '00:00:00', '00:00:00', '5', '桂林，简称桂，是世界著名风景游览城市、万年智慧圣地，是国务院批复确定的中国对外开放国际旅游城市、全国旅游创新发展先行区和国际旅游综合交通枢纽，截至2019年，全市下辖6区10县、代管1个县级市、总面积2.78万平方公里，建成区面积162平方千米，常住人口530余万，城镇人口247.34万人，城镇化率55%。');
INSERT INTO `scenic_spot` VALUES ('德天瀑布', '广西德天瀑布', '400', '299', '99.5', '08:00:00', '16:00:00', '4', 'xxxxx,2的16次方个字节');

-- ----------------------------
-- Table structure for `signup`
-- describe `用户注册表，该表保存相关信息`
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
INSERT INTO `signup` VALUES ('anlzou', 'an', '12345678901', '599502931@qq.com', 'anlzou');
INSERT INTO `signup` VALUES ('an', 'an', '123456', '123456@qq.com', 'an');

-- ----------------------------
-- Table structure for `vip_users`
-- describe `用户消费详情表，该表保存相关信息`

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
INSERT INTO `vip_users` VALUES ('an', '2', '1');