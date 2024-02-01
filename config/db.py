from mongoengine import register_connection
from dotenv import load_dotenv
from config import load_config
from pymongo.errors import PyMongoError
import certifi


load_dotenv()


def connect_db(ssl_reqs: bool = False):
    config = load_config()
    main_db_name = (
        config.DB_NAME if config.ENV == "prod" else f"{config.DB_NAME}Testing"
    )
    main_db_host = f"{config.DB_URL}/{main_db_name}?retryWrites=true&w=majority"

    ssl_kwargs = {} if not ssl_reqs else {"ssl": True, "tlsCAFile": certifi.where()}

    try:
        # Register the main connection
        register_connection(
            alias="default",
            name=main_db_name,
            host=main_db_host,
            **ssl_kwargs,
        )
        print(
            f"Connected to {'production' if config.ENV == 'prod' else 'testing'} database at: {main_db_host}..."
        )
    except PyMongoError as e:
        print(f"Failed to connect to MongoDB: {e}")
