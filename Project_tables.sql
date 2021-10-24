-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET @@time_zone = 'SYSTEM';


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--
DROP TABLE IF EXISTS `Student`;

# Create TABLE 'Student'
CREATE TABLE Student (
  Student_ID BIGINT(10) NOT NULL,
  Name VARCHAR(50) NOT NULL,
  Email VARCHAR(30) NOT NULL,
  `login_time` time NOT NULL,
  `login_date` date NOT NULL,
  `duration (h:min:s)` time NOT NULL,
  PRIMARY KEY(Student_ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'Course'
# Create TABLE 'Classroom'
# Create other TABLE...

CREATE TABLE Classroom
(
	Classroom_ID INT(10) NOT NULL,
	Address VARCHAR (30) NOT NULL,
	PRIMARY KEY(Classroom_ID)
);

CREATE TABLE Teacher
(
	Teacher_ID INT NOT NULL,
	Name VARCHAR(30) NOT NULL,
	PRIMARY KEY(Teacher_ID)
);

SET @@time_zone = 'SYSTEM';

CREATE TABLE Course
(
	Course_code VARCHAR(30) NOT NULL,
	Course_name VARCHAR(100) NOT NULL,
	Description TEXT NOT NULL,
	Zoom_link VARCHAR(200) NOT NULL,
	Message TEXT NOT NULL,
	Classroom_ID INT(10) NOT NULL,
	PRIMARY KEY(Course_code),
	FOREIGN KEY(Classroom_ID) REFERENCES Classroom(Classroom_ID)
);

CREATE TABLE `Course_materials`
(
	Course_code VARCHAR(30) NOT NULL,
	Course_material VARCHAR(200) NOT NULL,
	PRIMARY KEY(Course_code, Course_material),
	FOREIGN KEY(Course_code) REFERENCES Course(Course_code)
);

CREATE TABLE `Course_timeslots`
(
	Course_code VARCHAR(30) NOT NULL,
	Time_slot VARCHAR(30) NOT NULL,
	PRIMARY KEY(Course_code, Time_slot),
	FOREIGN KEY(Course_code) REFERENCES Course(Course_code)
);

CREATE TABLE takes
(
	Student_ID BIGINT(10) NOT NULL,
	Course_code VARCHAR(30) NOT NULL,
	PRIMARY KEY(Student_ID, Course_code),
	FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID),
	FOREIGN KEY(Course_code) REFERENCES Course(Course_code)
);

CREATE TABLE teaches
(
	Course_code VARCHAR(30) NOT NULL,
	Teacher_ID INT NOT NULL,
	PRIMARY KEY(Course_code, Teacher_ID),
	FOREIGN KEY(Course_code) REFERENCES Course(Course_code),
	FOREIGN KEY(Teacher_ID) REFERENCES Teacher(Teacher_ID)
);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
