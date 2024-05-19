-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2024 at 06:39 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `entrypass`
--

-- --------------------------------------------------------

--
-- Table structure for table `office`
--

CREATE TABLE `office` (
  `office_name` varchar(20) NOT NULL,
  `office_in_charge` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `office`
--

INSERT INTO `office` (`office_name`, `office_in_charge`) VALUES
('Bookstore', 'George'),
('Cashier', 'Blair'),
('OSAD', 'Clara'),
('Registrar', 'Abby');

-- --------------------------------------------------------

--
-- Table structure for table `specific_office`
--

CREATE TABLE `specific_office` (
  `office_name` varchar(20) NOT NULL,
  `transaction_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `role` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `firstname`, `lastname`, `role`) VALUES
('admin1', 'admin1', 'Sylvesqual', 'Korathos', 'admin'),
('test1', 'test1', 'Reag', 'Paddle', 'visitor'),
('test2', 'test2', 'Stardew', 'Ravago', 'visitor');

-- --------------------------------------------------------

--
-- Table structure for table `visitor`
--

CREATE TABLE `visitor` (
  `transaction_id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `date_of_visit` varchar(10) NOT NULL,
  `time_of_visit` varchar(10) NOT NULL,
  `office_name` varchar(20) NOT NULL,
  `purpose` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visitor`
--

INSERT INTO `visitor` (`transaction_id`, `email`, `date_of_visit`, `time_of_visit`, `office_name`, `purpose`) VALUES
(1, 'test1', '2024-05-15', '02:14', 'Cashier', 'Im going to cashier'),
(3, 'test1', '2024-05-15', '02:14', 'OSAD', 'Im going to OSAD'),
(4, 'test2', '2024-05-15', '02:14', 'Registrar', 'Im going to register'),
(5, 'test2', '2024-05-15', '02:14', 'Bookstore', 'Im going to bookstore'),
(8, 'test2', '2024-05-14', '05:39', 'Bookstore', 'book'),
(74, 'test2', '2024-04-30', '02:59', 'Cashier', 'Im going to pay for my SOUL'),
(75, 'test1', '2024-05-18', '16:00', 'Registrar', 'Im going to registrar');

-- --------------------------------------------------------

--
-- Table structure for table `visit_transaction`
--

CREATE TABLE `visit_transaction` (
  `transaction_number` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `guard_name` varchar(30) DEFAULT NULL,
  `office_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `office`
--
ALTER TABLE `office`
  ADD PRIMARY KEY (`office_name`);

--
-- Indexes for table `specific_office`
--
ALTER TABLE `specific_office`
  ADD KEY `fk_transaction_number` (`transaction_number`),
  ADD KEY `fk_specific_office_office_name` (`office_name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `idx_email` (`email`),
  ADD KEY `idx_firstname` (`firstname`),
  ADD KEY `idx_lastname` (`lastname`);

--
-- Indexes for table `visitor`
--
ALTER TABLE `visitor`
  ADD PRIMARY KEY (`transaction_id`),
  ADD KEY `fk_user_email` (`email`),
  ADD KEY `fk_office_office_name` (`office_name`);

--
-- Indexes for table `visit_transaction`
--
ALTER TABLE `visit_transaction`
  ADD PRIMARY KEY (`transaction_number`),
  ADD KEY `fk_guard_name` (`guard_name`),
  ADD KEY `fk_office_name` (`office_name`),
  ADD KEY `fk_user_email1` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `visitor`
--
ALTER TABLE `visitor`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `visit_transaction`
--
ALTER TABLE `visit_transaction`
  MODIFY `transaction_number` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `specific_office`
--
ALTER TABLE `specific_office`
  ADD CONSTRAINT `fk_specific_office_office_name` FOREIGN KEY (`office_name`) REFERENCES `office` (`office_name`),
  ADD CONSTRAINT `fk_transaction_number` FOREIGN KEY (`transaction_number`) REFERENCES `visit_transaction` (`transaction_number`);

--
-- Constraints for table `visitor`
--
ALTER TABLE `visitor`
  ADD CONSTRAINT `fk_office_office_name` FOREIGN KEY (`office_name`) REFERENCES `office` (`office_name`),
  ADD CONSTRAINT `fk_user_email` FOREIGN KEY (`email`) REFERENCES `users` (`email`);

--
-- Constraints for table `visit_transaction`
--
ALTER TABLE `visit_transaction`
  ADD CONSTRAINT `fk_guard_name` FOREIGN KEY (`guard_name`) REFERENCES `guard` (`guard_name`),
  ADD CONSTRAINT `fk_office_name` FOREIGN KEY (`office_name`) REFERENCES `office` (`office_name`),
  ADD CONSTRAINT `fk_user_email1` FOREIGN KEY (`email`) REFERENCES `users` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
