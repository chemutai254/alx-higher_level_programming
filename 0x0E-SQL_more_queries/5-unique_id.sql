-- Script that creates the table unique id
CREATE TABLE IF NOT EXISTS unique_id(
id INT NOT NULL DEFAULT 1,
name VARCHAR(2560),
UNIQUE INDEX(id));

