-- script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL.
	FOREIGN KEY (state_id) REFERENCES id(states),
	name VARCHAR(256) NOT NULL
);
