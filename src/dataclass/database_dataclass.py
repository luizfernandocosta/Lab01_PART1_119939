from dataclasses import dataclass

@dataclass(frozen=True)
class DatabaseDataclass:
    db_user: str
    db_password: str
    db_host: str
    db_name: str