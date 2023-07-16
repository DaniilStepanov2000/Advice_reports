class UserExists(Exception):
    """
    Entered credentials already exists
    """
    pass


class IncorrectCredentialsError(Exception):
    """
    Entered credentials are not correct
    """
    pass
