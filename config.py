import os

class Config:
    # Security & Database Configurations
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://user:password@localhost/idmui_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Keystone Authentication
    KEYSTONE_AUTH_URL = os.environ.get('KEYSTONE_AUTH_URL', 'http://keystone-server:5000/v3')
    KEYSTONE_ADMIN_USER = os.environ.get('KEYSTONE_ADMIN_USER', 'admin')
    KEYSTONE_ADMIN_PASSWORD = os.environ.get('KEYSTONE_ADMIN_PASSWORD', 'securepassword')
