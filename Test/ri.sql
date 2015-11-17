-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: Ago 23, 2015 as 02:39 AM
-- Versão do Servidor: 5.5.8
-- Versão do PHP: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de Dados: `ri`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tweet`
--

CREATE TABLE IF NOT EXISTS `tweet` (
  `id` bigint(20) unsigned NOT NULL,
  `id_str` varchar(20) NOT NULL,
  `text` varchar(140) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_str` (`id_str`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
