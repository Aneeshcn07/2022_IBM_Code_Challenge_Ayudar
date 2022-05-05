-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2022 at 11:30 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY '';

CREATE DATABASE IF NOT EXISTS mydatabase;

GRANT ALL PRIVILEGES ON taluk_test . * TO 'root'@'localhost';

USE mydatabase;
--
-- Database: `mydatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `tax_details`
--

CREATE TABLE `tax_details` (
  `id` int(5) NOT NULL,
  `aadhaar_no` varchar(12) NOT NULL,
  `date` datetime NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tax_details`
--

INSERT INTO `tax_details` (`id`, `aadhaar_no`, `date`, `status`) VALUES
(1, '201236547896', '2022-05-06 23:06:43', 'Not paid'),
(2, '201236547896', '2022-05-05 23:08:42', 'Paid');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tax_details`
--
ALTER TABLE `tax_details`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tax_details`
--
ALTER TABLE `tax_details`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
