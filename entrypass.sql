-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2024 at 03:53 AM
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
-- Table structure for table `guard`
--

CREATE TABLE `guard` (
  `guard_name` varchar(30) NOT NULL,
  `date_of_shift` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `guard`
--

INSERT INTO `guard` (`guard_name`, `date_of_shift`) VALUES
('guard1', '2024-04-22'),
('guard2', '2024-04-22'),
('guard3', '2024-04-22');

-- --------------------------------------------------------

--
-- Table structure for table `guard_log`
--

CREATE TABLE `guard_log` (
  `guard_name` varchar(30) NOT NULL,
  `transaction_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `firstname`, `lastname`, `role`) VALUES
('Person1@gmail.com', 'Person11111', 'Person11', 'Person11', 'visitor'),
('Person2@gmail.com', 'Person2', 'Person22', 'Person22', 'visitor'),
('Person3@gmail.com', 'Person3', 'Person33', 'Person33', 'visitor'),
('test', 'test', 'test', 'test', 'visitor');

-- --------------------------------------------------------

--
-- Table structure for table `visitor`
--

CREATE TABLE `visitor` (
  `visitor_id` int(11) NOT NULL,
  `visitor_fname` varchar(30) NOT NULL,
  `visitor_lname` varchar(30) NOT NULL,
  `purpose` varchar(200) NOT NULL,
  `date_of_visit` date NOT NULL,
  `time_of_visit` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visitor`
--

INSERT INTO `visitor` (`visitor_id`, `visitor_fname`, `visitor_lname`, `purpose`, `date_of_visit`, `time_of_visit`) VALUES
(1, 'Person1', 'Person1', 'Cashier', '2024-04-15', '10:00am'),
(2, 'Person2', 'Person2', 'Registrar', '2024-04-15', '11:00am'),
(3, 'Person3', 'Person3', 'Registrar', '2024-04-15', '1:00pm'),
(4, 'Person4', 'Person4', 'Cashier', '2024-04-15', '2:00:pm'),
(5, 'Person5', 'Person5', 'OSAD', '2024-04-15', '2:00pm');

-- --------------------------------------------------------

--
-- Table structure for table `visit_transaction`
--

CREATE TABLE `visit_transaction` (
  `transaction_number` int(11) NOT NULL,
  `visitor_id` int(11) NOT NULL,
  `visitor_fname` varchar(30) NOT NULL,
  `visitor_lname` varchar(30) NOT NULL,
  `purpose` varchar(200) NOT NULL,
  `guard_name` varchar(30) DEFAULT NULL,
  `office_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Stand-in structure for view `visit_transaction_info`
-- (See below for the actual view)
--
CREATE TABLE `visit_transaction_info` (
`transaction_number` int(11)
,`visitor_id` int(11)
,`visitor_fname` varchar(30)
,`visitor_lname` varchar(30)
,`purpose` varchar(200)
,`guard_name` varchar(30)
,`office_name` varchar(20)
);

-- --------------------------------------------------------

--
-- Structure for view `visit_transaction_info`
--
DROP TABLE IF EXISTS `visit_transaction_info`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `visit_transaction_info`  AS SELECT `vt`.`transaction_number` AS `transaction_number`, `v`.`visitor_id` AS `visitor_id`, `v`.`visitor_fname` AS `visitor_fname`, `v`.`visitor_lname` AS `visitor_lname`, `v`.`purpose` AS `purpose`, `g`.`guard_name` AS `guard_name`, `o`.`office_name` AS `office_name` FROM (((`visit_transaction` `vt` join `visitor` `v` on(`vt`.`visitor_id` = `v`.`visitor_id`)) join `guard` `g` on(`vt`.`guard_name` = `g`.`guard_name`)) join `office` `o` on(`vt`.`office_name` = `o`.`office_name`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `guard`
--
ALTER TABLE `guard`
  ADD PRIMARY KEY (`guard_name`);

--
-- Indexes for table `guard_log`
--
ALTER TABLE `guard_log`
  ADD KEY `fk_guard_log_guard_name` (`guard_name`),
  ADD KEY `fk_guard_log_transaction_number` (`transaction_number`);

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
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `visitor`
--
ALTER TABLE `visitor`
  ADD PRIMARY KEY (`visitor_id`);

--
-- Indexes for table `visit_transaction`
--
ALTER TABLE `visit_transaction`
  ADD PRIMARY KEY (`transaction_number`),
  ADD KEY `fk_visitor_id` (`visitor_id`),
  ADD KEY `fk_guard_name` (`guard_name`),
  ADD KEY `fk_office_name` (`office_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `visitor`
--
ALTER TABLE `visitor`
  MODIFY `visitor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `visit_transaction`
--
ALTER TABLE `visit_transaction`
  MODIFY `transaction_number` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `guard_log`
--
ALTER TABLE `guard_log`
  ADD CONSTRAINT `fk_guard_log_guard_name` FOREIGN KEY (`guard_name`) REFERENCES `guard` (`guard_name`),
  ADD CONSTRAINT `fk_guard_log_transaction_number` FOREIGN KEY (`transaction_number`) REFERENCES `visit_transaction` (`transaction_number`);

--
-- Constraints for table `specific_office`
--
ALTER TABLE `specific_office`
  ADD CONSTRAINT `fk_specific_office_office_name` FOREIGN KEY (`office_name`) REFERENCES `office` (`office_name`),
  ADD CONSTRAINT `fk_transaction_number` FOREIGN KEY (`transaction_number`) REFERENCES `visit_transaction` (`transaction_number`);

--
-- Constraints for table `visit_transaction`
--
ALTER TABLE `visit_transaction`
  ADD CONSTRAINT `fk_guard_name` FOREIGN KEY (`guard_name`) REFERENCES `guard` (`guard_name`),
  ADD CONSTRAINT `fk_office_name` FOREIGN KEY (`office_name`) REFERENCES `office` (`office_name`),
  ADD CONSTRAINT `fk_visitor_id` FOREIGN KEY (`visitor_id`) REFERENCES `visitor` (`visitor_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
