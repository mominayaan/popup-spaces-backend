import os
from dotenv import load_dotenv

from .config import Config, ProductionConfig, DevConfig, LocalConfig

load_dotenv()


def load_config(
    mode=os.getenv("ENV", "prod")
) -> ProductionConfig | DevConfig | LocalConfig:
    """Load config.py."""
    if mode == "prod":
        print("Loading production config.py")
        return ProductionConfig()
    elif mode == "dev":
        print("Loading dev config.py")
        return DevConfig()
    else:
        print("Loading dev local config.py")
        return LocalConfig()


config = load_config()
