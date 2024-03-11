import os

from data_ci.utils.db import DBConnection


def get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv("WAREHOUSE_USER", "tranthe"),
        password=os.getenv("WAREHOUSE_PASSWORD", "tranthe"),
        db=os.getenv("WAREHOUSE_DB", "finance"),
        host=os.getenv("WAREHOUSE_HOST", "localhost"),
        port=int(os.getenv("WAREHOUSE_PORT", 5432)),
    )
