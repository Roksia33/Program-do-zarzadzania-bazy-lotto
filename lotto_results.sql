-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Paź 10, 2023 at 06:22 PM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

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
-- Struktura tabeli dla tabeli `lotto_results`
--

CREATE TABLE `lotto_results` (
  `id` int(11) NOT NULL,
  `lotto_type` text CHARACTER SET utf16 COLLATE utf16_polish_ci NOT NULL,
  `number1` int(11) NOT NULL,
  `number2` int(11) DEFAULT NULL,
  `number3` int(11) DEFAULT NULL,
  `number4` int(11) DEFAULT NULL,
  `number5` int(11) DEFAULT NULL,
  `number6` int(11) DEFAULT NULL,
  `number7` int(11) DEFAULT NULL,
  `number8` int(11) DEFAULT NULL,
  `number9` int(11) DEFAULT NULL,
  `number10` int(11) DEFAULT NULL,
  `number11` int(11) DEFAULT NULL,
  `number12` int(11) DEFAULT NULL,
  `number13` int(11) DEFAULT NULL,
  `number14` int(11) DEFAULT NULL,
  `number15` int(11) DEFAULT NULL,
  `number16` int(11) DEFAULT NULL,
  `number17` int(11) DEFAULT NULL,
  `number18` int(11) DEFAULT NULL,
  `number19` int(11) DEFAULT NULL,
  `number20` int(11) DEFAULT NULL,
  `e_number1` int(11) DEFAULT NULL,
  `e_number2` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `lotto_results`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
