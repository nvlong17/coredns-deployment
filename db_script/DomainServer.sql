-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 30, 2020 at 03:58 PM
-- Server version: 8.0.17
-- PHP Version: 7.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `DomainServer`
--
CREATE DATABASE `DomainServer`;
USE `DomainServer`;

-- --------------------------------------------------------

--
-- Create dnssinkhole and grant privileges
--


CREATE USER 'dnssinkhole'@'%' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON `DomainServer`.`coreDNS` TO `dnssinkhole`@`%`;


-- --------------------------------------------------------

--
-- Create addomain and grant privileges
--


CREATE USER 'addomain'@'%' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON `DomainServer`.`domains` TO `addomain`@`%`;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON `DomainServer`.`whitelistDomains` TO `addomain`@`%`;


-- --------------------------------------------------------

--
-- Table structure for table `coreDNS`
--

CREATE TABLE `coreDNS` (
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `domains`
--

CREATE TABLE `domains` (
  `domain` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `whitelistDomains`
--

CREATE TABLE `whitelistDomains` (
  `domain` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `whitelistDomains`
--

INSERT INTO `whitelistDomains` (`domain`) VALUES
('azure.com'),
('blogdns.com'),
('cloudapp.net'),
('dantri.com.vn'),
('gartner.com'),
('github.blog'),
('github.community'),
('github.io'),
('githubassets.com'),
('githubstatus.com'),
('githubusercontent.com'),
('gitlab-static.net'),
('gitlab.com'),
('google.com'),
('msb.com.vn'),
('outlook.com.br'),
('readme.io'),
('sharepoint.com'),
('support-cloudapp.net'),
('uw.edu'),
('vnexpress.net'),
('vtc.vn');

--
-- Indexes for table `coreDNS`
--
ALTER TABLE `coreDNS`
  ADD KEY `id` (`id`);

--
-- Indexes for table `domains`
--
ALTER TABLE `domains`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `whitelistDomains`
--
ALTER TABLE `whitelistDomains`
  ADD PRIMARY KEY (`domain`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `domains`
--
ALTER TABLE `domains`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `coreDNS`
--
ALTER TABLE `coreDNS`
  ADD CONSTRAINT `coreDNS_ibfk_1` FOREIGN KEY (`id`) REFERENCES `domains` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
