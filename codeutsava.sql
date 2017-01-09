-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: codeutsava
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `linuxworkshop`
--

DROP TABLE IF EXISTS `linuxworkshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linuxworkshop` (
  `email` varchar(100) DEFAULT NULL,
  `yop` varchar(60) DEFAULT NULL,
  `experience` varchar(100) DEFAULT NULL,
  `degree` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `stream` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `institute` varchar(100) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linuxworkshop`
--

LOCK TABLES `linuxworkshop` WRITE;
/*!40000 ALTER TABLE `linuxworkshop` DISABLE KEYS */;
INSERT INTO `linuxworkshop` VALUES ('urjapawar@gmail.com','2018','yes','B.Tech','7746039992','Information Technology','Urja Pawar','',1),('lalitc375@gmail.com','2017','yes','B.Tech','7772823928','Information Technology','Lalit Chauhan','',2),('sahu_e@yahoo.com','2016','yes','Others','7509059076','Others','Ekta sahu','',3),('kajalrai835@gmail.com','2016','yes','Others','8871440193','Others','Kajal rai','',4),('tusharjani@live.com','2019','yes','B.Tech','9644577861','Information Technology','TUSHAR JANI','',5),('anubhavjain434@Gmail.com','2018','yes','B.Tech','8224985434','Computer Science','Anubhav Jain ','',6),('vikram00770@gmail.com','2018','no','B.Tech','8349474529','Information Technology','Vikram sukhsagar tiwari','',7),('huzaifwasim.nitrr@gmail.com','2018','no','B.Tech','7587348141','Information Technology','Muhammad Huzaif Wasim Qureshi','',8),('jhalani.anshul8025@gmail.com','2018','no','B.Tech','9770838126','Information Technology','Anshul jhalani','',9),('verma.smarika19@gmail.com','2019','yes','B.Tech','9451197324 ','Information Technology','Smarika Verma','',10),('agrawalprashant1995@gmail.com','2018','no','B.Tech','7583090979','Information Technology','prashant agrawal','',11),('ektaagrawal.agrawal09@gmail.com','2018','yes','B.Tech','7879082308','Computer Science','Ekta Agrawal ','',12),('sushiljain.267@gmail.com','2018','yes','B.Tech','9713379935','Information Technology','Sushil jain','NIT RAIPUR ',13),('iamyashwi@gmail.com','2019','no','B.Tech','7898556656','Information Technology','YASHWI SHAH','NIT Raipur',14),('grabamitesh@gmail.com','2017','no','M.Tech','8287898697','Information Technology','AMITESH KUMAR','NITRR',15),('sourabh.modi14@gmail.com','2019','yes','B.Tech','9039189251','Computer Science','Sourabh Modi ','NIT Raipur',16),('bipulpandey.100@gmail.com','2019','no','B.Tech','9563882153','Computer Science','BIPUL KUMAR PANDEY','JALAPAIGURI GOVERNMENT ENGINEERING COLLEGE',17),('sohit.gore21@outlook.com','2019','no','B.Tech','7767037922','Information Technology','Sohit Suresh Gore','National Institute of Technology, Raipur',18),('samantar216@gmail.com','2018','yes','B.Tech','8982404267','Electrical','rashmiranjan samanta','nit raipur',19),('apoorv.bansalite@gmail.com','2017','no','B.Tech','8109331863','Computer Science','Apoorv Singhal','NIT Raipur',20),('aditya999123@gmail.com','2019','yes','B.Tech','7587485272','Computer Science','Aditya','NIT RAIPUR',21),('sameertiwari98@gmail.com','2018','no','B.Tech','7089806780','Information Technology','SAMEER TIWARI ','NIT RAIPUR ',22),('mayanksharma.nitrr@gmail.com','2018','yes','B.Tech','7587045022','Information Technology','MAYANK SHARMA','NIT RAIPUR',23),('prashant.dhiru@gamil.com','2018','yes','Others','8889045277','Computer Science','prashant Dhirendra ','Disha college ',24),('rajatsurana12@gmail.com','2018','no','B.Tech','7987259362','Information Technology','Rajat Surana','National institute of technology, Raipur ',25),('shilpibiswas18@gmail.com','2019','yes','B.Tech','9479264954','Computer Science','suparna biswas','nit raipur',26),('padheeashutosh96@gmail.com','2018','no','B.Tech','8821047922','Electronics and Telecommunication','Ashutosh Padhee','NIT Raipur',27),('educate1996@gmail.com','2018','yes','B.Tech','9630800669','Information Technology','V Ramya','NIT Raipur',28),('meghal.nit@gmail.com','2018','yes','B.Tech','8109109457','Computer Science','Meghal Agrawal','NIT Raipur',29),('shreyanshss7@gmail.com','2019','yes','B.Tech','8871915764','Computer Science','Shreyansh Sahare','NIT Raipur',30),('yash199649@gmail.com','2018','yes','B.Tech','8085029528','Information Technology','Yash Sharma','NIT RAIPUR',31),('khedwaljahanvi@gmail.com','2018','no','B.Tech','8962011281','Information Technology','JAHANVI KHEDWAL','National Institute of Technology,raipur',32),('pratyushjanghel.exams@gmail.com','2019','yes','B.Tech','9617952219','Mechanical','Pratyush Janghel','SSIPMT, Raipur',33),('95akankshaverma@gmail.com','2017','yes','B.Tech','9753083338','Computer Science','Akanksha Verma','NIT Raipur',34),('kumar.kodwani007@gmail.com','2016','no','B.Tech','7987604376','Computer Science','Kumar Kodwani','Bit Raipur',35),('pihupatel817@gmail.com','2019','yes','B.Tech','9329613309','Computer Science','Asmita patidar','Columbia Institute of engineering and technology ',36),('vipulbjj@gmail.com','2018','yes','B.Tech','9407622939','Computer Science','Vipul Bajaj','NIT Raipur',37),('agarwal.rohit0597@gmail.com','2019','no','B.Tech','9039921002','Information Technology','Rohit Agarwal ','NIT raipur ',38),('jagritibajpai2606@gmail.com','2018','no','B.Tech','9893876413','Information Technology','Jagriti Bajpai','NIT Raipur',39),('pushpamandal1598pm@gmail.com','2019','no','B.Tech','9754362810','Computer Science','Pushpa Mandal','Shri Shankaracharya Institute of Technology &Management ',40),('divya.tiwari703@gmail.com','2018','no','B.Tech','8817678003','Information Technology','Divya Tiwari','NIT Raipur',41),('yashbafna05@gmail.com','2018','yes','B.Tech','9630580898','Information Technology','YASH BAFNA','NIT Raipur',42),('dollydivya1996@gmail.com','2018','yes','B.Tech','9893261194','Information Technology','Divya Sharma','NIT Raipur',43),('namsgh1012@gmail.com','2018','no','B.Tech','9993027747','Information Technology','Namrata Singh','NIT Raipur',44),('anoushka.20jul@gmail.com','2019','no','B.Tech','7024093123','Information Technology','anoushka dayal','national institute of technology Raipur ',45),('yalpalaneeraja422@gmail.com','2019','yes','B.Tech','9704963155','Information Technology','YALPALA NEERAJA','NIT Raipur',46);
/*!40000 ALTER TABLE `linuxworkshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `list`
--

DROP TABLE IF EXISTS `list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `list` (
  `email` varchar(100) DEFAULT NULL,
  `teamname` varchar(100) DEFAULT NULL,
  `resume` varchar(500) DEFAULT NULL,
  `github` varchar(500) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `yop` varchar(60) DEFAULT NULL,
  `experience` varchar(500) DEFAULT NULL,
  `address` varchar(500) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `degree` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `stream` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `twitter` varchar(500) DEFAULT NULL,
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `list`
--

LOCK TABLES `list` WRITE;
/*!40000 ALTER TABLE `list` DISABLE KEYS */;
INSERT INTO `list` VALUES ('ritesh.prasad289@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('78salmankashif6@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('kashyapshbhm@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('khedwaljahanvi@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('jagritibajpai2606@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('divya.tiwari703@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('urjapawar@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('urjapawar.nitrr@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('urja.pawar@rediffmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('yalpalaneeraja422@gmail.com',NULL,'https://drive.google.com/open?id=0B86xLpcoMU9QX01IQ3h3ckJhMEk','https://github.com/Neeraja422','1998-04-15','2019','not yet','Room no.29, Hostel E, NIT Raipur','Female','B.Tech','9704963155','Chattisgarh','Raipur','Information Technology','Neeraja Yalpala',NULL,'https://mobile.twitter.com/neeraja_yalpala'),('kodavatianusha.19@gmail.com',NULL,'https://drive.google.com/open?id=0B8LHKZ-1pE6OLTJjb0ljenBzeE0','https://github.com/Anusha1907','1999-07-19','2019','not yet','Room no.30, Hostel E, NIT Raipur','Female','B.Tech','9492073723','Chattisgarh','Raipur','Information Technology','Kodavati Anusha',NULL,'https://twitter.com/kodavati_anusha'),('nsupriya2013@gmail.com',NULL,'https://drive.google.com/open?id=0BxibIEE7DUdYYTFoMjVWcUFURmM','https://github.com/supriyaNIT','1999-03-28','2019','not yet ','Room no.34, Hostel E, NIT Raipur','Female','B.Tech','7587132524','Chattisgarh','Raipur','Information Technology','Nittravati Supriya',NULL,'https://mobile.twitter.com/NittravatiS'),('prashant.dhiru@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('mittal01091997@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('ashish03091996@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('b@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('c@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('a@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('deepanshusharma1802@gmail.com',NULL,'https://drive.google.com/open?id=0BzFQW4OZED8WTjNWeXN3RnBEQkk','https://github.com/sdeepanshu02','1997-02-18','2019','Android Development\r\nWeb Development\r\n\r\nI have successfully completed 3 projects of Android app.\r\n1. Medi World\r\n2. Time Table\r\n3. Where r u ??\r\n\r\nEach of above app can be found on my Github repo.','B-114, Bhabha Bhavan, SVNIT','Male','B.Tech','7600828330','Gujarat','Surat','Computer Science','Deepanshu sharma',NULL,'https://twitter.com/sdeepanshu02'),('tanishqq.khatri@gmail.com',NULL,'https://drive.google.com/open?id=0B5DZN1UQXQdQdHRzb1BkdlpETTA','https://github.com/Tanishka1997','1997-11-28','2019','Previously worked with android and done projects on android.Some involved web scripting as the app needed online connection.\r\nCurrently learning Flask(python) and web backend.\r\n','B-110 Bhabha Bhavan SVNIT campus,Surat','Male','B.Tech','9824259166','Gujarat','Surat','Computer Science','Tanishka Khatri',NULL,'https://twitter.com/KhatriTanishka'),('karan.juneja1106@gmail.com',NULL,'https://drive.google.com/open?id=0B0f8SxUZ_rL-dXliVm9LUWFzaWs','https://github.com/karanjuneja1106/','1997-06-11','2019','Android app development in Summer Mentor-ship Program By SVNIT \r\nParticipated in Hacktoberfest 2016 ','B 108 Bhabha Bhavan, SVNIT Campus','Male','B.Tech','9408748648','Gujarat','Surat','Computer Science','Karan Juneja',NULL,''),('suyashbajpai86@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('yash199649@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('garg.swapnil26@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('kanha95@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('catchdevabi@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('kanha1995@rediffmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Kaviyapriyas01@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('gnanamdurai96@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('priya.banu1497@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('anandvijsy094@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('ssshekhu53@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('abhinavanand7812@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('scmbs.verma@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('ravisingh9835201134@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('vikram00770@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('pa19972014@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('chetanasahu1997@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('rashiguptady@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('x@y.xom',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('a@b.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('c@d.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('ayushbsp98@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('dkg1915@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('bbhardwaj102@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('sourabh.modi14@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('awani.mishra216@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('arpitj938@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('amanjain.1596@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('amanagrawal513@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('iket.ag24@gmail.com',NULL,'https://drive.google.com/open?id=0BzG6CtqkERK8YlU1YjNHazQ2cEk','https://github.com/iket0512','1995-12-05','2019','Developed E-Cell App.\r\nDeveloped app for vigyaan and secured 2 nd position in my department.\r\nCurrently developing apps and learning server end(django and python) at codenicely.','','Male','B.Tech','9174908579','chhattisgarh','raigarh','Computer Science','Iket Agrawal',NULL,''),('ujjwalkumarsingh61@gmail.com',NULL,'https://github.com/ujjwakumarsingh','https://github.com/ujjwakumarsingh','1997-09-20','2019','NOT ANY','HALL 9 ENERGY CENTRE MANIT BHOPAL','Male','B.Tech','7549474776','MADHYA PRADESH','BHOPAL','Others','UJJWAL KUMAR SINGH',NULL,''),('bhagwatidholpuria@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('arpitsahu3108@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('prpt30@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('samridhigupta.100@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('naushe27enkhan@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('srivastava.aishwarya177@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('ektaagrawal.agrawal09@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('vipulbjj@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `active` int(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `teamname` varchar(100) DEFAULT NULL,
  `resume` varchar(500) DEFAULT NULL,
  `github` varchar(500) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `yop` varchar(60) DEFAULT NULL,
  `experience` varchar(500) DEFAULT NULL,
  `address` varchar(500) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `degree` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `stream` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `twitter` varchar(500) DEFAULT NULL,
  `tshirt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,1,'1995rishi@gmail.com','ghanta','https://www.github.com/rishi1995','https://www.github.com/rishi1995','1995-12-14','2018','nope','Plot Nos. 14/15, Street 19E, Priyanka Nagar, Risali, Bhilai','Male','B.Tech','7587351731','Chhattisgarh','Bhilai Nagar','Information Technology','Rishi',1,'',NULL),(2,1,'gaurav.alliswell@gmail.com','ghanta','http://codeutsava.in/activate?email=katiyar.bhaumik@gmail.com&hash=356475bb7164ba49cdaa60c383581bf6','http://n.com','2017-01-13','2017','YOYO','j','Male','B.Tech','860229193','CG','Bhilai','Mechanical','Rishi',1,NULL,NULL),(3,NULL,'aashray18521@gmail.com','ghanta',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,1,'ritesh.prasad289@gmail.com','dotSlash',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,NULL,'78salmankashif6@gmail.com','dotSlash',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,NULL,'kashyapshbhm@gmail.com','dotSlash',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,1,'khedwaljahanvi@gmail.com','Bits please',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,1,'jagritibajpai2606@gmail.com','Bits please',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,1,'divya.tiwari703@gmail.com','Bits please',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(16,1,'yalpalaneeraja422@gmail.com','ANS@NITRR','https://drive.google.com/open?id=0B86xLpcoMU9QX01IQ3h3ckJhMEk','https://github.com/Neeraja422','1998-04-15','2019','not yet','Room no.29, Hostel E, NIT Raipur','Female','B.Tech','9704963155','Chattisgarh','Raipur','Information Technology','Neeraja Yalpala',1,'https://mobile.twitter.com/neeraja_yalpala',NULL),(17,1,'kodavatianusha.19@gmail.com','ANS@NITRR','https://drive.google.com/open?id=0B8LHKZ-1pE6OLTJjb0ljenBzeE0','https://github.com/Anusha1907','1999-07-19','2019','not yet','Room no.30, Hostel E, NIT Raipur','Female','B.Tech','9492073723','Chattisgarh','Raipur','Information Technology','Kodavati Anusha',1,'https://twitter.com/kodavati_anusha',NULL),(18,1,'nsupriya2013@gmail.com','ANS@NITRR','https://drive.google.com/open?id=0BxibIEE7DUdYYTFoMjVWcUFURmM','https://github.com/supriyaNIT','1999-03-28','2019','not yet ','Room no.34, Hostel E, NIT Raipur','Female','B.Tech','7587132524','Chattisgarh','Raipur','Information Technology','Nittravati Supriya',1,'https://mobile.twitter.com/NittravatiS',NULL),(19,1,'prashant.dhiru@gmail.com','ImperfectCoder',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(20,NULL,'mittal01091997@gmail.com','ImperfectCoder',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(21,NULL,'ashish03091996@gmail.com','ImperfectCoder',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(25,1,'deepanshusharma1802@gmail.com','Null Pointer','https://drive.google.com/open?id=0BzFQW4OZED8WTjNWeXN3RnBEQkk','https://github.com/sdeepanshu02','1997-02-18','2019','Android Development\r\nWeb Development\r\n\r\nI have successfully completed 3 projects of Android app.\r\n1. Medi World\r\n2. Time Table\r\n3. Where r u ??\r\n\r\nEach of above app can be found on my Github repo.','B-114, Bhabha Bhavan, SVNIT','Male','B.Tech','7600828330','Gujarat','Surat','Computer Science','Deepanshu sharma',1,'https://twitter.com/sdeepanshu02',NULL),(26,1,'tanishqq.khatri@gmail.com','Null Pointer','https://drive.google.com/open?id=0B5DZN1UQXQdQdHRzb1BkdlpETTA','https://github.com/Tanishka1997','1997-11-28','2019','Previously worked with android and done projects on android.Some involved web scripting as the app needed online connection.\r\nCurrently learning Flask(python) and web backend.\r\n','B-110 Bhabha Bhavan SVNIT campus,Surat','Male','B.Tech','9824259166','Gujarat','Surat','Computer Science','Tanishka Khatri',1,'https://twitter.com/KhatriTanishka',NULL),(27,1,'karan.juneja1106@gmail.com','Null Pointer','https://drive.google.com/open?id=0B0f8SxUZ_rL-dXliVm9LUWFzaWs','https://github.com/karanjuneja1106/','1997-06-11','2019','Android app development in Summer Mentor-ship Program By SVNIT \r\nParticipated in Hacktoberfest 2016 ','B 108 Bhabha Bhavan, SVNIT Campus','Male','B.Tech','9408748648','Gujarat','Surat','Computer Science','Karan Juneja',1,'',NULL),(28,1,'suyashbajpai86@gmail.com','Sys',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(29,NULL,'yash199649@gmail.com','Sys',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(30,1,'garg.swapnil26@gmail.com','Sys',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(31,1,'kanha95@gmail.com','whizz-kids',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(32,NULL,'catchdevabi@gmail.com','whizz-kids',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(33,1,'kanha1995@rediffmail.com','whizz-kids',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(34,NULL,'Kaviyapriyas01@gmail.com','Kaviya priya',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(35,NULL,'gnanamdurai96@gmail.com','Kaviya priya',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(36,NULL,'priya.banu1497@gmail.com','Kaviya priya',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(37,NULL,'anandvijsy094@gmail.com','psccoders094',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(38,1,'ssshekhu53@gmail.com','psccoders094',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(39,1,'abhinavanand7812@gmail.com','psccoders094',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(40,NULL,'scmbs.verma@gmail.com','teamvrb',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(41,1,'ravisingh9835201134@gmail.com','teamvrb',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(42,1,'vikram00770@gmail.com','teamvrb',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(43,1,'pa19972014@gmail.com','cpr',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(44,1,'chetanasahu1997@gmail.com','cpr',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(45,1,'rashiguptady@gmail.com','cpr',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(46,NULL,'x@y.xom','xyz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(47,NULL,'a@b.com','xyz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(48,NULL,'c@d.com','xyz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49,1,'ayushbsp98@gmail.com','ABD',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50,1,'dkg1915@gmail.com','ABD',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(51,NULL,'bbhardwaj102@gmail.com','ABD',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(52,1,'sourabh.modi14@gmail.com','Dementors',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(53,NULL,'awani.mishra216@gmail.com','Dementors',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(54,1,'arpitj938@gmail.com','Dementors',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(55,1,'amanjain.1596@gmail.com','Phoenix',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(56,1,'amanagrawal513@gmail.com','Phoenix',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(57,1,'iket.ag24@gmail.com','Phoenix','https://drive.google.com/open?id=0BzG6CtqkERK8YlU1YjNHazQ2cEk','https://github.com/iket0512','1995-12-05','2019','Developed E-Cell App.\r\nDeveloped app for vigyaan and secured 2 nd position in my department.\r\nCurrently developing apps and learning server end(django and python) at codenicely.','','Male','B.Tech','9174908579','chhattisgarh','raigarh','Computer Science','Iket Agrawal',1,'','XL'),(58,1,'ujjwalkumarsingh61@gmail.com','whitewolf','https://github.com/ujjwakumarsingh','https://github.com/ujjwakumarsingh','1997-09-20','2019','NOT ANY','HALL 9 ENERGY CENTRE MANIT BHOPAL','Male','B.Tech','7549474776','MADHYA PRADESH','BHOPAL','Others','UJJWAL KUMAR SINGH',1,'','M'),(59,1,'bhagwatidholpuria@gmail.com','whitewolf',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(60,NULL,'arpitsahu3108@gmail.com','whitewolf',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(61,1,'prpt30@gmail.com','Sneakgeekz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(62,1,'samridhigupta.100@gmail.com','Sneakgeekz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(63,1,'naushe27enkhan@gmail.com','Sneakgeekz',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(64,NULL,'srivastava.aishwarya177@gmail.com','E.V.A',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(65,1,'ektaagrawal.agrawal09@gmail.com','E.V.A',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(66,1,'vipulbjj@gmail.com','E.V.A',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pythonworkshop`
--

DROP TABLE IF EXISTS `pythonworkshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pythonworkshop` (
  `email` varchar(100) DEFAULT NULL,
  `yop` varchar(60) DEFAULT NULL,
  `experience` varchar(100) DEFAULT NULL,
  `degree` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `stream` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pythonworkshop`
--

LOCK TABLES `pythonworkshop` WRITE;
/*!40000 ALTER TABLE `pythonworkshop` DISABLE KEYS */;
INSERT INTO `pythonworkshop` VALUES ('1995rishi@gmail.com','2018',NULL,'B.Tech','7587351731','Information Technology','Rishi',1),('tusharjani@live.com','2019',NULL,'B.Tech','9644577861','Information Technology','TUSHAR JANI',2),('sourabh.modi14@gmail.com','2019',NULL,'B.Tech','9039189251','Computer Science','Sourabh Modi ',3),('rajatsurana12@gmail.com','2018',NULL,'B.Tech','7987259362','Information Technology','Rajat Surana',4),('educate1996@gmail.com','2018',NULL,'B.Tech','9630800669','Information Technology','V Ramya',5),('yash199649@gmail.com','2018',NULL,'B.Tech','8085029528','Information Technology','Yash Sharma',6),('prlt30@gmail.com','2018',NULL,'B.Tech','7089060776','Information Technology','Preeti Patel',7),('dollydivya1996@gmail.com','2018',NULL,'B.Tech','8619449262','Information Technology','Divya Sharma',8),('yalpalaneeraja422@gmail.com','2019',NULL,'B.Tech','9704963155','Information Technology','YALPALA NEERAJA',9);
/*!40000 ALTER TABLE `pythonworkshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(100) DEFAULT NULL,
  `active` int(11) DEFAULT NULL,
  `teamname` varchar(100) DEFAULT NULL,
  `institute` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (1,'yoyoyo',NULL,'ghanta','NIT Raipur'),(2,'pythonhunters',NULL,'dotSlash','NIT Jamshedpur'),(3,'Bits please',NULL,'Bits please','National Institute of Technology Raipur'),(6,'ANS@NITRR',1,'ANS@NITRR','NIT Raipur'),(7,'prashant',NULL,'ImperfectCoder','Disha college '),(9,'12345678',1,'Null Pointer','Sardar Vallabhbhai National Institute of Technology, Surat,Gujarat'),(10,'password',NULL,'Sys','NIT,Raipur'),(11,'kanha123',NULL,'whizz-kids','College Of Engineering And Technology Bhubaneswar'),(12,'Subru21@22',NULL,'Kaviya priya','Government college of technology, Coimbatore'),(13,'shashankanand',NULL,'psccoders094','Patna Science College'),(14,'faaducoder',NULL,'teamvrb','NIT Raipur'),(15,'chetanapoojarashi',NULL,'cpr','NIT, Raipur'),(16,'qwertyuiop',NULL,'xyz','iiit'),(17,'password123',NULL,'ABD','NATIONAL INSTITUTE OF TECHNOLOGY RAIPUR'),(18,'killpotter',NULL,'Dementors','NIT Raipur'),(19,'aman1596',NULL,'Phoenix','National Institute of Technology, Raipur'),(20,'215d02$QfPDG',NULL,'whitewolf','maulana azad national institute of technology'),(21,'SneakGeekz',NULL,'Sneakgeekz','NIT Raipur'),(22,'ekta@vipul@aish',NULL,'E.V.A','NIT Raipur');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-09 18:01:20
