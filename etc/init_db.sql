DROP DATABASE IF EXISTS ask_db;
CREATE DATABASE  if not exists ask_db;
CREATE USER 'django' IDENTIFIED BY 'secret';
GRANT ALL ON ask_db.* TO 'django';
