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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `appointments` */

insert  into `appointments`(`id`,`serialnumber`,`patientname`,`aadhar`,`bp`,`sugar`,`hypertention`,`status1`,`status2`,`billnumber`) values (1,'PID01','balaram','985425365689','normal','45','yes','pending','pending',NULL),(8,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(9,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(10,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(11,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(12,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(13,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(14,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(15,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(16,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01'),(17,'PID01','balaram','985425365689','normal','45','yes','pending','pending','PB01');

/*Table structure for table `connectdata` */

DROP TABLE IF EXISTS `connectdata`;

CREATE TABLE `connectdata` (
  `Id` int(100) NOT NULL AUTO_INCREMENT,
  `PatientName` varchar(100) DEFAULT NULL,
  `PatientAge` varchar(100) DEFAULT NULL,
  `Type` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `connectdata` */

insert  into `connectdata`(`Id`,`PatientName`,`PatientAge`,`Type`,`status`) values (1,'mouli','45','Pulmonary','accept'),(2,'mouli','45','Pulmonary','accept'),(3,'kumar','58','Pulmonary','accept'),(4,'narayana','59','Pulmonary','pending');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `docreg` */

insert  into `docreg`(`slno`,`Name`,`Department`,`Age`,`Number`,`Email`,`Password`,`status`) values (1,'Balaram','Pulmonary','28','4587256987','balarampanigrahy42@gmail.com','1234','accepted');

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

insert  into `patient_reg`(`ID`,`name`,`profile`,`profilename`,`address`,`aadhar`,`bp`,`sugar`,`hypertention`,`password`) values (1,'balaram','uploadfiles/balaram.png','balaram.png','Nellore','985425365689','normal','45','yes','1234');

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `patientreq` */

insert  into `patientreq`(`Id`,`Name`,`Type`,`Age`,`symptoms`,`AppointmentDate`,`Time`,`Status`) values (1,'mouli','Pulmonary','45','Brain hemorrhage  ','03/23/2022','16:38','accepted'),(2,'kumar','Pulmonary','58','Brain tumor ','03/28/2022','18:20','accepted'),(3,'narayana','Pulmonary','59','hemorrhage  ','03/29/2022','06:30','accepted');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `reports` */

insert  into `reports`(`Id`,`FileName`,`FileData`,`aadhar`,`Status`,`Key1`,`Patientid`) values (1,'File1.txt','ësµ‚30È3G\'¦˜Åœ>PI’åL9š\Zú­UÖRmÈ','985425365689','accepted',NULL,'PID5336');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
