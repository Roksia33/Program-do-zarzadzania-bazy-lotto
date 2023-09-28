-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 28, 2023 at 11:41 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lotto`
--

-- --------------------------------------------------------

--
-- Table structure for table `lotto_results`
--

CREATE TABLE `lotto_results` (
  `id` int(11) NOT NULL,
  `lotto_type` text NOT NULL,
  `number1` int(11) NOT NULL,
  `number2` int(11) NOT NULL,
  `number3` int(11) NOT NULL,
  `number4` int(11) DEFAULT NULL,
  `number5` int(11) DEFAULT NULL,
  `number6` int(11) DEFAULT NULL,
  `number7` int(11) DEFAULT NULL,
  `number8` int(11) DEFAULT NULL,
  `number9` int(11) DEFAULT NULL,
  `number10` int(11) DEFAULT NULL,
  `number11` int(11) DEFAULT NULL,
  `number12` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `lotto_results`
--

INSERT INTO `lotto_results` (`id`, `lotto_type`, `number1`, `number2`, `number3`, `number4`, `number5`, `number6`, `number7`, `number8`, `number9`, `number10`, `number11`, `number12`) VALUES
(1, 'Lotto', 34, 1, 44, 11, 2, 17, 23, 56, 45, 22, 21, 13),
(2, 'Lotto', 43, 1, 41, 45, 23, 8, 3, 67, 10, 24, 15, 19);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lotto_results`
--
ALTER TABLE `lotto_results`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lotto_results`
--
ALTER TABLE `lotto_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
