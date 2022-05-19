from enum import Enum


class AuthType(Enum):
    """The auth type

    Args:
        Enum (AuthType): the auth type
    """

    BASIC = "BASIC"
    LDAP = "LDAP"
