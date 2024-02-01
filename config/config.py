import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CORS_HEADERS = "Content-Type"
    API_PORT = os.getenv("API_PORT", 5000)
    DB_NAME = os.getenv("DB_NAME", "NeutrinoAppDB")  # Change this
    DB_URL = os.getenv("DB_URL")
    CORS_ORIGIN_WHITELIST = "*"  # any origin
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    REDIS_URL = os.getenv("REDIS_URL")

    if DB_URL is None:
        raise ValueError("No DB URL set in environment variables")
    elif REDIS_HOST is None:
        raise ValueError("No Redis host set in environment variables")


class ProductionConfig(Config):
    DEBUG = False
    ENV = "prod"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    if JWT_SECRET_KEY is None:
        raise ValueError("No JWT secret key set in environment variables")


class DevConfig(Config):
    DEBUG = True
    ENV = os.getenv("ENV", "dev")
    REDIS_PASSWORD = None
    REDIS_URL = None
    JWT_SECRET_KEY = "dev-secret-key"


class LocalConfig(Config):
    DEBUG = True
    ENV = os.getenv("ENV", "local")
    REDIS_PASSWORD = None
    REDIS_URL = None
    JWT_SECRET_KEY = "dev-secret-key"
    DB_URL = "mongodb://mongo:27017"
