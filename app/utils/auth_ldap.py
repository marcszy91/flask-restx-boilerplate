import ldap3

from app import logger

from flask import current_app
from ldap3.core.exceptions import LDAPException


class LDAPHelper:
    @staticmethod
    def ldap_auth(username: str, password: str) -> bool:
        """Check ldap login

        Args:
            user_id (str): the user id
            password (str): the user password

        Returns:
            bool: True if connection successfully otherwise wrong
        """
        try:
            server = current_app.config["LDAP_HOST"]
            ldap_user_prefix = current_app.config["LDAP_USER_PREFIX"]
            user = username
            if ldap_user_prefix:
                user = ldap_user_prefix + username
            with ldap3.Connection(server=server, user=user, password=password) as conn:
                if conn.result["description"] == "success":
                    return True
                else:
                    return False
        except LDAPException as e:
            logger.error("LDAP-Login failed for user %s", username)
            logger.debug(e.with_traceback)
            return False

    @staticmethod
    def ldap_get_email_by_username(username: str, password: str) -> str:
        try:
            server = current_app.config["LDAP_HOST"]
            ldap_user_prefix = current_app.config["LDAP_USER_PREFIX"]
            search_base = current_app.config["LDAP_SEARCH_BASE"]
            search_filter = current_app.config["LDAP_SEARCH_FILTER"]
            search_filter = search_filter.format(username)
            user = username
            if ldap_user_prefix:
                user = ldap_user_prefix + username
            with ldap3.Connection(server=server, user=user, password=password) as conn:
                if conn.result["description"] == "success":
                    email_exist = conn.search(
                        search_base=search_base,
                        search_filter=search_filter,
                        attributes=["mail"],
                    )
                    if email_exist:
                        return conn.entries[0]["mail"].value
                else:
                    return None
        except LDAPException as e:
            logger.error("LDAP cant read email for user %s", username)
            logger.debug(e.with_traceback)
            return None
