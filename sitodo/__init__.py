from typing import Optional


def getenv_bool(key: str) -> Optional[bool]:
    """Get an environment variable as boolean value."""
    from os import getenv

    VALID_TRUE_VALUES: tuple[str] = ("true", "True", "TRUE")
    VALID_FALSE_VALUES: tuple[str] = ("false", "False", "FALSE")

    value: Optional[str] = getenv(key)

    if value is None:
        return None

    if value in VALID_TRUE_VALUES:
        return True

    if value in VALID_FALSE_VALUES:
        return False

    return False
