-- Create database
CREATE DATABASE IF NOT EXISTS project_2;
USE project_2;

-- Table 1: bird_monitoring
CREATE TABLE IF NOT EXISTS bird_monitoring (
    id INT AUTO_INCREMENT PRIMARY KEY,
    site_name VARCHAR(255),
    sci_name VARCHAR(100),
    com_name VARCHAR(255),
    observer VARCHAR(100),
    temperature FLOAT,
    humidity FLOAT,
    date DATE,
    location_type VARCHAR(255)
);

-- Table 2: bird_monitoring_grassland
CREATE TABLE IF NOT EXISTS bird_monitoring_grassland (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plot_name VARCHAR(255),
    observer VARCHAR(100),
    id_method VARCHAR(100),
    wind VARCHAR(100),
    sci_name VARCHAR(100),
    com_name VARCHAR(255)
);

-- Table 3: grassland_year
CREATE TABLE IF NOT EXISTS grassland_year (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plot_name VARCHAR(255),
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    sci_name VARCHAR(100),
    com_name VARCHAR(255)
);

-- Table 4: forest_year
CREATE TABLE IF NOT EXISTS forest_year (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plot_name VARCHAR(255),
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    sci_name VARCHAR(100),
    com_name VARCHAR(255)
);
