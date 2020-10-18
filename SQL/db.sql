/*
 Navicat Premium Data Transfer

 Source Server         : MySql
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : db

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 18/10/2020 16:59:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stu_clazz
-- ----------------------------
DROP TABLE IF EXISTS `stu_clazz`;
CREATE TABLE `stu_clazz`  (
  `cno` int NOT NULL AUTO_INCREMENT,
  `cname` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`cno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu_clazz
-- ----------------------------
INSERT INTO `stu_clazz` VALUES (1, 'B201python');
INSERT INTO `stu_clazz` VALUES (2, 'B203HTML5');
INSERT INTO `stu_clazz` VALUES (3, 'B202JAVA');

-- ----------------------------
-- Table structure for stu_course
-- ----------------------------
DROP TABLE IF EXISTS `stu_course`;
CREATE TABLE `stu_course`  (
  `course_no` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`course_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu_course
-- ----------------------------
INSERT INTO `stu_course` VALUES (1, 'JAVA');
INSERT INTO `stu_course` VALUES (2, 'Python');
INSERT INTO `stu_course` VALUES (3, 'HTML5');

-- ----------------------------
-- Table structure for stu_student
-- ----------------------------
DROP TABLE IF EXISTS `stu_student`;
CREATE TABLE `stu_student`  (
  `sno` int NOT NULL AUTO_INCREMENT,
  `sname` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cls_id` int NOT NULL,
  PRIMARY KEY (`sno`) USING BTREE,
  INDEX `stu_student_cls_id_bfc5344f_fk_stu_clazz_cno`(`cls_id`) USING BTREE,
  CONSTRAINT `stu_student_cls_id_bfc5344f_fk_stu_clazz_cno` FOREIGN KEY (`cls_id`) REFERENCES `stu_clazz` (`cno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu_student
-- ----------------------------
INSERT INTO `stu_student` VALUES (1, 'zhangsan', 1);
INSERT INTO `stu_student` VALUES (2, 'lisi', 2);
INSERT INTO `stu_student` VALUES (3, 'wangwu', 3);

-- ----------------------------
-- Table structure for stu_student_cour
-- ----------------------------
DROP TABLE IF EXISTS `stu_student_cour`;
CREATE TABLE `stu_student_cour`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `stu_student_cour_student_id_course_id_39c56cc2_uniq`(`student_id`, `course_id`) USING BTREE,
  INDEX `stu_student_cour_course_id_07159f09_fk_stu_course_course_no`(`course_id`) USING BTREE,
  CONSTRAINT `stu_student_cour_course_id_07159f09_fk_stu_course_course_no` FOREIGN KEY (`course_id`) REFERENCES `stu_course` (`course_no`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `stu_student_cour_student_id_8669b064_fk_stu_student_sno` FOREIGN KEY (`student_id`) REFERENCES `stu_student` (`sno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu_student_cour
-- ----------------------------
INSERT INTO `stu_student_cour` VALUES (1, 1, 1);
INSERT INTO `stu_student_cour` VALUES (2, 2, 1);
INSERT INTO `stu_student_cour` VALUES (3, 2, 2);
INSERT INTO `stu_student_cour` VALUES (4, 2, 3);
INSERT INTO `stu_student_cour` VALUES (5, 3, 1);
INSERT INTO `stu_student_cour` VALUES (6, 3, 2);
INSERT INTO `stu_student_cour` VALUES (7, 3, 3);

SET FOREIGN_KEY_CHECKS = 1;
