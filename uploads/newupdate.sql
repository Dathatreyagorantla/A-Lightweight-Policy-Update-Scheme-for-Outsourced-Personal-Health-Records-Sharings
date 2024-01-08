/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.4.28-MariaDB : Database - lightweightpolicy
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`lightweightpolicy` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `lightweightpolicy`;

/*Table structure for table `appointments` */

DROP TABLE IF EXISTS `appointments`;

CREATE TABLE `appointments` (
  `id` int(200) NOT NULL AUTO_INCREMENT,
  `serialnumber` varchar(100) DEFAULT NULL,
  `patientname` varchar(100) DEFAULT NULL,
  `aadhar` varchar(100) DEFAULT NULL,
  `bp` varchar(100) DEFAULT NULL,
  `sugar` varchar(100) DEFAULT NULL,
  `hypertention` varchar(100) DEFAULT NULL,
  `status1` varchar(100) DEFAULT 'pending',
  `status2` varchar(100) DEFAULT 'pending',
  `billnumber` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `appointments` */

/*Table structure for table `connectdata` */

DROP TABLE IF EXISTS `connectdata`;

CREATE TABLE `connectdata` (
  `Id` int(100) NOT NULL AUTO_INCREMENT,
  `PatientName` varchar(100) DEFAULT NULL,
  `PatientAge` varchar(100) DEFAULT NULL,
  `Type` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `connectdata` */

/*Table structure for table `docreg` */

DROP TABLE IF EXISTS `docreg`;

CREATE TABLE `docreg` (
  `slno` int(100) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `Department` varchar(100) DEFAULT NULL,
  `Age` varchar(100) DEFAULT NULL,
  `Number` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  UNIQUE KEY `slno` (`slno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `docreg` */

/*Table structure for table `patient_reg` */

DROP TABLE IF EXISTS `patient_reg`;

CREATE TABLE `patient_reg` (
  `ID` int(200) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `profile` varchar(100) DEFAULT NULL,
  `profilename` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `aadhar` varchar(100) DEFAULT NULL,
  `bp` varchar(100) DEFAULT NULL,
  `sugar` varchar(100) DEFAULT NULL,
  `hypertention` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `patient_reg` */

insert  into `patient_reg`(`ID`,`name`,`profile`,`profilename`,`address`,`aadhar`,`bp`,`sugar`,`hypertention`,`password`) values (1,'balaram','profiles/balaram.png','balaram.png','bangalore','985425365689','normal','45','yes','1234');

/*Table structure for table `patientreq` */

DROP TABLE IF EXISTS `patientreq`;

CREATE TABLE `patientreq` (
  `Id` int(200) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `Type` varchar(100) DEFAULT NULL,
  `Age` varchar(100) DEFAULT NULL,
  `symptoms` varchar(100) DEFAULT NULL,
  `AppointmentDate` varchar(100) DEFAULT NULL,
  `Time` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `patientreq` */

/*Table structure for table `reports` */

DROP TABLE IF EXISTS `reports`;

CREATE TABLE `reports` (
  `Id` int(200) NOT NULL AUTO_INCREMENT,
  `FileName` varchar(200) DEFAULT NULL,
  `FileData` longblob DEFAULT NULL,
  `aadhar` varchar(200) DEFAULT NULL,
  `Status` varchar(200) DEFAULT NULL,
  `Key1` varchar(100) DEFAULT NULL,
  `Patientid` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `reports` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
