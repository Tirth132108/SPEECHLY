-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2021 at 01:02 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `speechly`
--

-- --------------------------------------------------------

--
-- Table structure for table `translator`
--

CREATE TABLE `translator` (
  `sourceMessage` varchar(1000) NOT NULL,
  `translatedTo` varchar(100) NOT NULL,
  `translatedMessage` varchar(1000) CHARACTER SET utf8 NOT NULL,
  `timeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `translator`
--

INSERT INTO `translator` (`sourceMessage`, `translatedTo`, `translatedMessage`, `timeStamp`) VALUES
('????? ??? ????? ???? ??', 'hi', 'मैरुइंग नाउट ट्रैथ पॅट ', '2021-03-10 06:34:10'),
('I have to take IELTS on Saturday', 'gu', 'મારે શનિવારે આઇઇએલટીએસ લેવું પડશે ', '2021-03-10 06:36:51'),
('you are such a fool', 'hi', 'तुम ऐसे मूर्ख हो ', '2021-03-10 06:38:20'),
('you are such a fool', 'hi', 'यो रे का फूल ', '2021-03-10 06:40:45'),
('????? ??? ????? ???? ??', 'en', 'My name is Tirtha Patel ', '2021-03-10 06:41:59'),
('???? ??????? ????????? ????? ????\r\n', 'en', 'I have to take IELTS on Saturday ', '2021-03-10 08:05:30'),
('???? ??????? ????????? ????? ????\r\n', 'en', 'I have to take IELTS on Saturday ', '2021-03-10 08:18:59'),
('i have done speaking  test', 'gu', 'ઇ હવે ડોને સ્પેઅકિંગ  ટેસ્ટ ', '2021-03-14 10:00:01'),
('\r\n\r\n? ??? ???? ????????? ?????', 'hi', 'ई। अब डॉन का स्पोकिंग टेस्ट ', '2021-03-14 10:00:23'),
('\r\n\r\n? ??? ???? ????????? ?????', 'hi', 'ई। अब डॉन का स्पोकिंग टेस्ट ', '2021-03-14 10:00:31'),
('user', 'gujarati', '', '2021-03-17 12:21:42'),
('user', 'gujarati', '', '2021-03-17 12:22:28'),
('user', 'gujarati', '', '2021-03-17 12:22:46'),
('user', 'gujarati', '', '2021-03-17 12:24:39'),
('user', 'gujarati', '', '2021-03-17 12:25:41'),
('user', 'gujarati', '', '2021-03-17 13:04:42'),
('user', 'gujarati', '', '2021-03-17 13:05:05'),
('user', 'gujarati', '', '2021-03-17 13:06:34'),
('user', 'gujarati', '', '2021-03-17 13:16:42'),
('user', 'gujarati', '', '2021-03-17 13:19:46'),
('user', 'gujarati', '', '2021-03-17 13:22:30'),
('user', 'gujarati', '', '2021-03-17 13:26:48'),
('user', 'gujarati', '', '2021-03-17 13:38:20'),
('user', 'gujarati', '', '2021-03-17 13:40:09'),
('user', 'gujarati', '', '2021-03-17 13:41:44'),
('user', 'gujarati', '', '2021-03-17 13:44:06'),
('user', 'gujarati', '', '2021-03-18 05:31:10'),
('user', 'gujarati', '', '2021-03-18 05:34:03'),
('user', 'gujarati', '', '2021-03-18 05:35:26'),
('user', 'gujarati', '', '2021-03-18 05:56:23'),
('user', 'gujarati', '', '2021-03-18 06:01:21'),
('user', 'gujarati', '', '2021-03-18 07:28:09'),
('user', 'gujarati', '', '2021-03-18 07:28:21'),
('user', 'gujarati', '', '2021-03-18 07:28:40'),
('user', 'gujarati', '', '2021-03-18 07:59:17');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_password` varchar(30) NOT NULL,
  `user_email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `user_password`, `user_email`) VALUES
(1, 'admin', 'admin', 'admin@gmail.com'),
(2, 'niyati', 'niyu@1321', 'niyatisalot1999@gmail.com'),
(3, 'detuu', 'rana@1234', 'niyatisheth@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
