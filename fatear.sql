-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 01, 2023 at 01:22 AM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fatear`
--

-- --------------------------------------------------------

--
-- Table structure for table `album`
--

CREATE TABLE `album` (
  `albumID` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `album`
--

INSERT INTO `album` (`albumID`) VALUES
('1'),
('2'),
('3'),
('4'),
('5');

-- --------------------------------------------------------

--
-- Table structure for table `artist`
--

CREATE TABLE `artist` (
  `artistID` varchar(5) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `artistBio` varchar(300) DEFAULT NULL,
  `artistURL` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `artist`
--

INSERT INTO `artist` (`artistID`, `fname`, `lname`, `artistBio`, `artistURL`) VALUES
('1', 'Bill', 'Withers', 'William Harrison Withers Jr. was an American singer and songwriter. He had several hits over a career spanning 18 years, including \"Ain\'t No Sunshine\", \"Grandma\'s Hands\", \"Use Me\", \"Lean on Me\", \"Lovely Day\" and \"Just the Two of Us\".', 'https://music.youtube.com/channel/UCDjpW6k2Sfg_FTr1toLvffQ'),
('10', 'Frank', 'Sinatra', 'Francis Albert Sinatra was an American singer and actor. Nicknamed the \"Chairman of the Board\" and later called \"Ol\' Blue Eyes\", Sinatra was one of the most popular entertainers of the 1940s, 1950s, and 1960s.', 'https://music.youtube.com/channel/UC1zsfp3OD8qWQ0HfLbz2TXg'),
('11', 'Bruno', 'Mars', 'Peter Gene Hernandez, known professionally as Bruno Mars, is an American singer, songwriter, and record producer.', 'https://music.youtube.com/channel/UCZn4r7heNOPY-C43YIywnVA'),
('2', 'Norah', 'Jones', 'Norah Jones first emerged on the world stage with the February 2002 release of Come Away With Me, her self-described “moody little record” that introduced a singular new voice and grew into a global phenomenon, sweeping the 2003 GRAMMY Awards.', 'https://music.youtube.com/channel/UCxRuL2yOu2ydTJNZuYdU0qg'),
('3', 'Ed', 'Sheeran', 'Edward Christopher Sheeran MBE is an English singer-songwriter. Born in Halifax, West Yorkshire, and raised in Framlingham, Suffolk, he began writing songs around the age of eleven. In early 2011, Sheeran independently released the extended play No. 5 Collaborations Project. ', 'https://music.youtube.com/channel/UClmXPfaYhXOYsNn_QUyheWQ'),
('4', 'Michael', 'Jackson', 'Michael Joseph Jackson was an American singer, songwriter, dancer, and philanthropist. Dubbed the \"King of Pop\", he is regarded as one of the most significant cultural figures of the 20th century.', 'https://music.youtube.com/channel/UCoIOOL7QKuBhQHVKL8y7BEQ'),
('5', 'The', 'Weeknd', ' The Weeknd is a talented and popular Ethiopian Hipster R&B artist who hails from the beautiful country of Canada--Ontario in particular. Born on February 16, 1990 under the name of Abel Tesfaye, he felt the pains of a less than ideal child\'s life while growing up.', 'https://music.youtube.com/channel/UClYV6hHlupm_S_ObS1W-DYw'),
('6', 'Mark', 'Ronson', 'Mark Ronson didn’t mean to make a debut album that reinvented party-friendly hip hop. Nor a follow-up that became one of the defining albums of the second half of the Noughties.', 'https://music.youtube.com/channel/UCm9XijVCOsRrxdx0giD_1fQ'),
('7', 'Chris', 'Brown', 'Christopher Maurice Brown is an American singer, songwriter, dancer, and actor. According to Billboard, Brown is one of the most successful R&B singers of his generation, having often been referred to by many contemporaries as the \"King of R&B\".', 'https://music.youtube.com/channel/UCMXDyVR2tclKWhbqNforSyA'),
('8', 'H.E.R.', '', 'Gabriella Sarmiento Wilson, known professionally as H.E.R., is an American R&B singer.', 'https://music.youtube.com/channel/UCeOvrkZes_-LywIjFvbaxug'),
('9', 'Grover', 'Washington, Jr.', 'Grover Washington Jr. was an American jazz-funk and soul-jazz saxophonist and Grammy Award Winner. Along with Wes Montgomery and George Benson, he is considered by many to be one of the founders of the smooth jazz genre.', 'https://music.youtube.com/channel/UCsN1HTruhFfXcSMGMsBmX_w');

-- --------------------------------------------------------

--
-- Table structure for table `artistperformssong`
--

CREATE TABLE `artistperformssong` (
  `artistID` varchar(5) NOT NULL,
  `songID` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `artistperformssong`
--

INSERT INTO `artistperformssong` (`artistID`, `songID`) VALUES
('3', '1'),
('11', '2'),
('6', '2'),
('4', '3'),
('5', '5'),
('2', '8');

-- --------------------------------------------------------

--
-- Table structure for table `follows`
--

CREATE TABLE `follows` (
  `follower` varchar(10) NOT NULL,
  `follows` varchar(10) NOT NULL,
  `createdAt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `follows`
--

INSERT INTO `follows` (`follower`, `follows`, `createdAt`) VALUES
('ab123', 'kp2690', '2023-03-01 21:01:55'),
('ab123', 'mm13034', NULL),
('ab123', 'wc1609', NULL),
('admin1', 'ab123', '2023-04-23 17:34:20'),
('admin1', 'kp2690', '2023-04-30 14:12:44'),
('kp2690', 'ab123', '2023-03-17 21:33:15'),
('zs1282', 'ab123', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `friend`
--

CREATE TABLE `friend` (
  `user1` varchar(10) NOT NULL,
  `user2` varchar(10) NOT NULL,
  `acceptStatus` varchar(15) DEFAULT NULL,
  `requestSentBy` varchar(10) DEFAULT NULL,
  `createdAt` datetime DEFAULT NULL,
  `updatedAt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `friend`
--

INSERT INTO `friend` (`user1`, `user2`, `acceptStatus`, `requestSentBy`, `createdAt`, `updatedAt`) VALUES
('ab123', 'kp2690', 'Accepted', 'ab123', '2023-03-01 21:07:41', '2023-04-23 17:39:16'),
('ab123', 'mm13034', 'Accepted', 'ab123', '2023-03-01 21:07:41', '2023-04-23 17:39:16'),
('ab123', 'wc1609', 'Pending', 'wc1609', '2023-03-22 21:10:27', '2023-04-23 17:39:16'),
('admin1', 'ab123', 'Accepted', 'admin1', '2023-04-23 17:11:53', '2023-04-23 17:39:16'),
('admin1', 'admin', 'Pending', 'admin1', '2023-04-23 18:28:56', '2023-04-23 18:28:56'),
('admin1', 'kp2690', 'Pending', 'admin1', '2023-04-30 14:18:29', '2023-04-30 14:18:29'),
('kp2690', 'admin1', 'Not accepted', 'kp2690', '2023-04-01 18:31:53', '2023-04-30 13:42:56'),
('zs1282', 'ab123', 'Pending', 'zs1282', '2023-03-09 21:23:40', '2023-04-23 17:39:16');

-- --------------------------------------------------------

--
-- Table structure for table `ratealbum`
--

CREATE TABLE `ratealbum` (
  `username` varchar(10) NOT NULL,
  `albumID` varchar(5) NOT NULL,
  `stars` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `ratesong`
--

CREATE TABLE `ratesong` (
  `username` varchar(10) NOT NULL,
  `songID` varchar(5) NOT NULL,
  `stars` int(11) DEFAULT NULL,
  `ratingDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ratesong`
--

INSERT INTO `ratesong` (`username`, `songID`, `stars`, `ratingDate`) VALUES
('ab123', '7', 5, '2023-03-22'),
('ab123', '8', 4, '2023-03-28'),
('ab123', '9', 3, '2023-03-20'),
('admin1', '1', 3, '2023-04-20'),
('admin1', '2', 2, '2023-04-30'),
('kp2690', '1', 5, '2023-03-29'),
('kp2690', '2', 4, '2023-03-15'),
('kp2690', '7', 5, '2023-03-29'),
('kp2690', '8', 5, '2023-03-30'),
('kp2690', '9', 5, '2023-03-28'),
('mm13034', '4', 3, '2023-03-29'),
('mm13034', '5', 4, '2023-03-31'),
('mm13034', '7', 5, '2023-03-14'),
('mm13034', '8', 2, '2023-03-21'),
('mm13034', '9', 4, '2023-03-21'),
('wc1609', '2', 4, '2023-03-20');

-- --------------------------------------------------------

--
-- Table structure for table `reviewalbum`
--

CREATE TABLE `reviewalbum` (
  `username` varchar(10) NOT NULL,
  `albumID` varchar(5) NOT NULL,
  `reviewText` varchar(100) DEFAULT NULL,
  `reviewDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `reviewsong`
--

CREATE TABLE `reviewsong` (
  `username` varchar(10) NOT NULL,
  `songID` varchar(5) NOT NULL,
  `reviewText` varchar(100) DEFAULT NULL,
  `reviewDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `reviewsong`
--

INSERT INTO `reviewsong` (`username`, `songID`, `reviewText`, `reviewDate`) VALUES
('admin1', '1', 'sdfsdfsdf', '2023-04-23'),
('admin1', '2', 'review for Uptown Funk', '2023-04-30'),
('kp2690', '1', 'gdfgdfgfr', '2023-03-22'),
('mm13034', '2', 'sfsdwerwe', '2023-02-08');

-- --------------------------------------------------------

--
-- Table structure for table `song`
--

CREATE TABLE `song` (
  `songID` varchar(5) NOT NULL,
  `title` varchar(20) NOT NULL,
  `releaseDate` date DEFAULT NULL,
  `songURL` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `song`
--

INSERT INTO `song` (`songID`, `title`, `releaseDate`, `songURL`) VALUES
('1', 'Perfect', '2019-02-01', 'https://music.youtube.com/watch?v=ORrFJ63nlcA'),
('2', 'Uptown Funk', '2016-03-02', 'https://music.youtube.com/watch?v=OPf0YbXqDm0'),
('3', 'Billie Jean', '1991-01-23', 'https://music.youtube.com/watch?v=Zi_XLOBDo_Y'),
('4', 'Under The Influence', '2016-03-17', 'https://music.youtube.com/watch?v=pfxyk1glEq4'),
('5', 'Die for You', '2018-03-09', 'https://music.youtube.com/watch?v=mTLQhPFx2nM&list=RDAMVMmTLQhPFx2nM'),
('6', 'Damage', '2023-03-08', 'https://music.youtube.com/watch?v=PAFAfhod9TU'),
('7', 'Just the Two of Us', '2016-03-09', 'https://music.youtube.com/watch?v=6POZlJAZsok'),
('8', 'Don\'t Know Why', '2014-03-12', 'https://music.youtube.com/watch?v=tO4dxvguQDk'),
('9', 'My Way', '2018-03-14', 'https://music.youtube.com/watch?v=qQzdAsjWGPg');

-- --------------------------------------------------------

--
-- Table structure for table `songgenre`
--

CREATE TABLE `songgenre` (
  `songID` varchar(5) NOT NULL,
  `genre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `songgenre`
--

INSERT INTO `songgenre` (`songID`, `genre`) VALUES
('1', 'Pop'),
('2', 'Pop'),
('3', 'Pop'),
('4', 'R&B'),
('5', 'R&B'),
('6', 'R&B'),
('7', 'Jazz'),
('8', 'Jazz'),
('9', 'Jazz');

-- --------------------------------------------------------

--
-- Table structure for table `songinalbum`
--

CREATE TABLE `songinalbum` (
  `albumID` varchar(5) NOT NULL,
  `songID` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `songinalbum`
--

INSERT INTO `songinalbum` (`albumID`, `songID`) VALUES
('1', '1'),
('5', '1'),
('2', '2'),
('3', '3'),
('4', '5');

-- --------------------------------------------------------

--
-- Stand-in structure for view `song_avg_rating`
-- (See below for the actual view)
--
CREATE TABLE `song_avg_rating` (
`songID` varchar(5)
,`avg_rating` decimal(14,4)
);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(10) NOT NULL,
  `pwd` varchar(65) DEFAULT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `lastlogin` date DEFAULT NULL,
  `nickname` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `pwd`, `fname`, `lname`, `lastlogin`, `nickname`) VALUES
('ab123', '123456', 'Roy', 'Zhang', '2014-03-01', 'zh'),
('admin', '123456', 'Aliza', 'Levy', '2023-04-19', NULL),
('admin1', '$2b$12$nJIqzaxGB.ztUfF8mXiZmuaGF67GDtCAIbXoEe5ZJ08uVNiCW3.8a', 'Kaiyu', 'Pei', '2014-04-01', 'KZKZ'),
('admin111', '$2b$12$pH0ZLGiJ89F9.sTAn7zRF.U5oMvCF17Ha9LtogBIlpAcWT3EszEeS', '11', '22', NULL, 'cc'),
('kp2690', '123456', 'Mike', 'Peters', '2023-03-16', 'kp'),
('mm13034', '456456', 'Tommy', 'Brandt', '2023-03-08', 'tb'),
('wc1609', '657612', 'Raphael', 'Peltier', '2023-03-17', 'Ra'),
('zf2155', '435345', 'Siobhan', 'Shankar', '2023-03-02', NULL),
('zs1282', '234234', 'Kobe', 'Chavez', '2023-03-16', 'abc');

-- --------------------------------------------------------

--
-- Table structure for table `userfanofartist`
--

CREATE TABLE `userfanofartist` (
  `username` varchar(10) NOT NULL,
  `artistID` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userfanofartist`
--

INSERT INTO `userfanofartist` (`username`, `artistID`) VALUES
('ab123', '3'),
('admin1', '3');

-- --------------------------------------------------------

--
-- Structure for view `song_avg_rating`
--
DROP TABLE IF EXISTS `song_avg_rating`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `song_avg_rating`  AS   (select `ratesong`.`songID` AS `songID`,avg(`ratesong`.`stars`) AS `avg_rating` from (`ratesong` join `songgenre` on((`ratesong`.`songID` = `songgenre`.`songID`))) group by `ratesong`.`songID` order by `avg_rating` desc)  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`albumID`);

--
-- Indexes for table `artist`
--
ALTER TABLE `artist`
  ADD PRIMARY KEY (`artistID`);

--
-- Indexes for table `artistperformssong`
--
ALTER TABLE `artistperformssong`
  ADD PRIMARY KEY (`artistID`,`songID`),
  ADD KEY `songID` (`songID`);

--
-- Indexes for table `follows`
--
ALTER TABLE `follows`
  ADD PRIMARY KEY (`follower`,`follows`),
  ADD KEY `follows` (`follows`);

--
-- Indexes for table `friend`
--
ALTER TABLE `friend`
  ADD PRIMARY KEY (`user1`,`user2`),
  ADD KEY `user2` (`user2`);

--
-- Indexes for table `ratealbum`
--
ALTER TABLE `ratealbum`
  ADD PRIMARY KEY (`username`,`albumID`),
  ADD KEY `albumID` (`albumID`);

--
-- Indexes for table `ratesong`
--
ALTER TABLE `ratesong`
  ADD PRIMARY KEY (`username`,`songID`),
  ADD KEY `songID` (`songID`);

--
-- Indexes for table `reviewalbum`
--
ALTER TABLE `reviewalbum`
  ADD PRIMARY KEY (`username`,`albumID`),
  ADD KEY `albumID` (`albumID`);

--
-- Indexes for table `reviewsong`
--
ALTER TABLE `reviewsong`
  ADD PRIMARY KEY (`username`,`songID`),
  ADD KEY `songID` (`songID`);

--
-- Indexes for table `song`
--
ALTER TABLE `song`
  ADD PRIMARY KEY (`songID`);

--
-- Indexes for table `songgenre`
--
ALTER TABLE `songgenre`
  ADD PRIMARY KEY (`songID`,`genre`);

--
-- Indexes for table `songinalbum`
--
ALTER TABLE `songinalbum`
  ADD PRIMARY KEY (`albumID`,`songID`),
  ADD KEY `songID` (`songID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `userfanofartist`
--
ALTER TABLE `userfanofartist`
  ADD PRIMARY KEY (`username`,`artistID`),
  ADD KEY `artistID` (`artistID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `artistperformssong`
--
ALTER TABLE `artistperformssong`
  ADD CONSTRAINT `artistperformssong_ibfk_1` FOREIGN KEY (`artistID`) REFERENCES `artist` (`artistID`) ON DELETE CASCADE,
  ADD CONSTRAINT `artistperformssong_ibfk_2` FOREIGN KEY (`songID`) REFERENCES `song` (`songID`) ON DELETE CASCADE;

--
-- Constraints for table `follows`
--
ALTER TABLE `follows`
  ADD CONSTRAINT `follows_ibfk_1` FOREIGN KEY (`follower`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `follows_ibfk_2` FOREIGN KEY (`follows`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `friend`
--
ALTER TABLE `friend`
  ADD CONSTRAINT `friend_ibfk_1` FOREIGN KEY (`user1`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `friend_ibfk_2` FOREIGN KEY (`user2`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `ratealbum`
--
ALTER TABLE `ratealbum`
  ADD CONSTRAINT `ratealbum_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `ratealbum_ibfk_2` FOREIGN KEY (`albumID`) REFERENCES `album` (`albumID`) ON DELETE CASCADE;

--
-- Constraints for table `ratesong`
--
ALTER TABLE `ratesong`
  ADD CONSTRAINT `ratesong_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `ratesong_ibfk_2` FOREIGN KEY (`songID`) REFERENCES `song` (`songID`) ON DELETE CASCADE;

--
-- Constraints for table `reviewalbum`
--
ALTER TABLE `reviewalbum`
  ADD CONSTRAINT `reviewalbum_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `reviewalbum_ibfk_2` FOREIGN KEY (`albumID`) REFERENCES `album` (`albumID`) ON DELETE CASCADE;

--
-- Constraints for table `reviewsong`
--
ALTER TABLE `reviewsong`
  ADD CONSTRAINT `reviewsong_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `reviewsong_ibfk_2` FOREIGN KEY (`songID`) REFERENCES `song` (`songID`) ON DELETE CASCADE;

--
-- Constraints for table `songgenre`
--
ALTER TABLE `songgenre`
  ADD CONSTRAINT `songgenre_ibfk_1` FOREIGN KEY (`songID`) REFERENCES `song` (`songID`) ON DELETE CASCADE;

--
-- Constraints for table `songinalbum`
--
ALTER TABLE `songinalbum`
  ADD CONSTRAINT `songinalbum_ibfk_1` FOREIGN KEY (`albumID`) REFERENCES `album` (`albumID`) ON DELETE CASCADE,
  ADD CONSTRAINT `songinalbum_ibfk_2` FOREIGN KEY (`songID`) REFERENCES `song` (`songID`) ON DELETE CASCADE;

--
-- Constraints for table `userfanofartist`
--
ALTER TABLE `userfanofartist`
  ADD CONSTRAINT `userfanofartist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `userfanofartist_ibfk_2` FOREIGN KEY (`artistID`) REFERENCES `artist` (`artistID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
