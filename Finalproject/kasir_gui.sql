-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Nov 2020 pada 17.38
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kasir_gui`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `meja`
--

CREATE TABLE `meja` (
  `id` int(100) NOT NULL,
  `nama` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `meja`
--

INSERT INTO `meja` (`id`, `nama`) VALUES
(1, 'MEJA 1'),
(2, 'MEJA 2'),
(3, 'MEJA 3'),
(4, 'MEJA 4'),
(5, 'MEJA 5'),
(6, 'MEJA 6'),
(7, 'MEJA 7'),
(8, 'MEJA 8'),
(9, 'MEJA 9'),
(10, 'MEJA 10'),
(11, 'MEJA 11'),
(12, 'MEJA 12'),
(18, 'MEJA 13'),
(19, 'MEJA 14');

-- --------------------------------------------------------

--
-- Struktur dari tabel `menu`
--

CREATE TABLE `menu` (
  `id` int(100) NOT NULL,
  `nama_menu` varchar(128) NOT NULL,
  `harga_menu` varchar(128) NOT NULL,
  `jenis_menu` enum('Minuman','Makanan') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `menu`
--

INSERT INTO `menu` (`id`, `nama_menu`, `harga_menu`, `jenis_menu`) VALUES
(2, 'Nasi Goreng', '15000', 'Makanan'),
(3, 'Kopi Hitam', '4000', 'Minuman'),
(4, 'Mie Goreng/Rebus', '8000', 'Makanan'),
(10, 'Kopi Susu', '3000', 'Minuman'),
(12, 'Ayam Goreng', '70000', 'Makanan'),
(13, 'Jus Jeruk', '7000', 'Minuman'),
(14, 'Jus Mangga', '4000', 'Minuman'),
(15, 'Jus Alpukat', '7000', 'Minuman'),
(16, 'Ayam Bakar', '7000', 'Makanan'),
(17, 'Gorengan', '1000', 'Makanan'),
(18, 'Nasi Bungkus', '4000', 'Makanan'),
(19, 'Ikan Bakar', '7000', 'Makanan'),
(20, 'Ikan Goreng', '40000', 'Makanan'),
(21, 'Gurame Goreng', '40000', 'Makanan'),
(22, 'Es Teh Manis', '4000', 'Minuman'),
(23, 'Es Cendol', '4000', 'Minuman'),
(27, 'ES Cingcau', '5000', 'Minuman'),
(29, 'Kopi Susu2', '4000', 'Minuman'),
(30, 'Nasi Goreng Spesial', '15000', 'Makanan'),
(31, 'Kentang', '13000', 'Makanan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `riwayat`
--

CREATE TABLE `riwayat` (
  `id` int(100) NOT NULL,
  `nama_menu` varchar(128) NOT NULL,
  `harga_menu` varchar(128) NOT NULL,
  `jenis_menu` varchar(128) NOT NULL,
  `by_user` varchar(128) NOT NULL,
  `waktu_input` date NOT NULL,
  `nama_meja` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `riwayat`
--

INSERT INTO `riwayat` (`id`, `nama_menu`, `harga_menu`, `jenis_menu`, `by_user`, `waktu_input`, `nama_meja`) VALUES
(1, 'Kopi Hitam', '4000', 'Minuman', 'admin', '2020-06-28', 'MEJA 1');

-- --------------------------------------------------------

--
-- Struktur dari tabel `riwayat_hapus`
--

CREATE TABLE `riwayat_hapus` (
  `id` int(100) NOT NULL,
  `nama_menu` varchar(128) NOT NULL,
  `harga_menu` varchar(128) NOT NULL,
  `jenis_menu` varchar(128) NOT NULL,
  `user_input` varchar(128) NOT NULL,
  `user_hapus` varchar(128) NOT NULL,
  `waktu_input` date NOT NULL,
  `waktu_hapus` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `riwayat_hapus`
--

INSERT INTO `riwayat_hapus` (`id`, `nama_menu`, `harga_menu`, `jenis_menu`, `user_input`, `user_hapus`, `waktu_input`, `waktu_hapus`) VALUES
(7, 'Mie Goreng/Rebus', '8000', 'Makanan', 'Admin', 'Admin', '2020-06-25', '2020-06-25'),
(8, 'Mie Goreng/Rebus', '8000', 'Makanan', 'ardi', 'ardi', '2020-06-25', '2020-06-25'),
(9, 'Kopi Hitam', '4000', 'Minuman', 'admin', 'admin', '2020-06-26', '2020-06-26'),
(10, 'Mie Goreng/Rebus', '8000', 'Makanan', 'admin', 'admin', '2020-06-26', '2020-06-26'),
(11, 'Mie Goreng/Rebus', '8000', 'Makanan', 'admin', 'admin', '2020-06-26', '2020-06-26');

-- --------------------------------------------------------

--
-- Struktur dari tabel `riwayat_selesai`
--

CREATE TABLE `riwayat_selesai` (
  `id` int(100) NOT NULL,
  `nama_menu` varchar(128) NOT NULL,
  `harga_menu` varchar(128) NOT NULL,
  `jenis_menu` varchar(128) NOT NULL,
  `user_input` varchar(128) NOT NULL,
  `user_selesai` varchar(128) NOT NULL,
  `waktu_input` date NOT NULL,
  `waktu_selesai` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `riwayat_selesai`
--

INSERT INTO `riwayat_selesai` (`id`, `nama_menu`, `harga_menu`, `jenis_menu`, `user_input`, `user_selesai`, `waktu_input`, `waktu_selesai`) VALUES
(148, 'Kopi Hitam', '4000', 'Minuman', 'Admin', 'Admin', '2020-06-25', '2020-06-25'),
(149, 'Mie Goreng/Rebus', '8000', 'Makanan', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(150, 'Ayam Goreng', '70000', 'Makanan', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(151, 'Jus Alpukat', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(152, 'Ayam Bakar', '7000', 'Makanan', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(153, 'Ayam Goreng', '70000', 'Makanan', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(154, 'Gorengan', '1000', 'Makanan', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(155, 'Jus Jeruk', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(156, 'Kopi Hitam', '4000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(157, 'Jus Jeruk', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(158, 'Jus Alpukat', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(159, 'Jus Mangga', '4000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(160, 'Ikan Bakar', '7000', 'Makanan', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(161, 'Jus Jeruk', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(162, 'Jus Mangga', '4000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(163, 'Jus Jeruk', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(164, 'Jus Jeruk', '7000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(165, 'Kopi Hitam', '4000', 'Minuman', 'ardi', 'ardi', '2020-06-26', '2020-06-26'),
(166, 'Jus Jeruk', '7000', 'Minuman', 'admin', 'admin', '2020-06-26', '2020-06-26'),
(167, 'Ayam Goreng', '70000', 'Makanan', 'admin', 'admin', '2020-06-27', '2020-06-27'),
(168, 'Mie Goreng/Rebus', '8000', 'Makanan', 'admin', 'admin', '2020-06-27', '2020-06-27'),
(169, 'Kopi Susu', '3000', 'Minuman', 'admin', 'admin', '2020-06-28', '2020-06-28');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `nama` varchar(128) NOT NULL,
  `role` enum('Admin','Kasir') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `nama`, `role`) VALUES
(1, 'admin', '459d9e004d552fb5d160dc216ac31d81', 'Hanung', 'Admin'),
(2, 'ardi', 'b623a7cebe5be1abc1409e528f6b4451', 'Ardi', 'Kasir'),
(3, 'gilang', '6d8f8a1a4837f099459ec46a72660f30', 'Gilang', 'Kasir'),
(4, 'gilang2', '88e7309f61a969337f5cbdfe04ecc78d', 'Gilang2', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `meja`
--
ALTER TABLE `meja`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `riwayat`
--
ALTER TABLE `riwayat`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `riwayat_hapus`
--
ALTER TABLE `riwayat_hapus`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `riwayat_selesai`
--
ALTER TABLE `riwayat_selesai`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `meja`
--
ALTER TABLE `meja`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT untuk tabel `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT untuk tabel `riwayat`
--
ALTER TABLE `riwayat`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `riwayat_hapus`
--
ALTER TABLE `riwayat_hapus`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT untuk tabel `riwayat_selesai`
--
ALTER TABLE `riwayat_selesai`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=170;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
