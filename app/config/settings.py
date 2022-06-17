import os

class Settings:
    
    databases: dict ={
        "ENGINE": os.getenv("DB_ENGINE"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "DATABASE": os.getenv("DB_DATABASE")
    }
