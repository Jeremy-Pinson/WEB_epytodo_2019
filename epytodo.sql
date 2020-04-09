CREATE DATABASE epytodo;
USE epytodo;
CREATE TABLE user ( user_id int NOT NULL AUTO_INCREMENT primary key, username VARCHAR(40) NOT NULL, password VARCHAR(100) NOT NULL );
CREATE TABLE task ( 
    task_id int NOT NULL AUTO_INCREMENT primary key,
    title VARCHAR(100) NOT NULL, 
    begin DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end DATE DEFAULT NULL,
    status ENUM ('not started','in progress','done') NOT NULL
);
CREATE TABLE user_has_task ( fk_user_id int, fk_task_id int, atribution_id int NOT NULL AUTO_INCREMENT primary key );