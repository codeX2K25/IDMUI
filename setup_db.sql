-- File: setup_db.sql (optional - you can run these commands directly)
CREATE DATABASE idmui_db;
CREATE USER 'idmui_user'@'localhost' IDENTIFIED BY 'SecurePass123!';
GRANT ALL PRIVILEGES ON idmui_db.* TO 'idmui_user'@'localhost';
FLUSH PRIVILEGES;