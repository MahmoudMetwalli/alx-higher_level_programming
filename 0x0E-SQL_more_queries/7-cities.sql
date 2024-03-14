-- Creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL FOREIGN KEY(cities.id), name VARCHAR(256) NOT NULL);
