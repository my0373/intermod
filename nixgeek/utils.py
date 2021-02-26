import sys


def exit_success():
    """
    Exit the program with an exit status of 0.
    This denotes success for most shell applications.
    :return:
    """
    sys.exit(0)


def exit_failure(exit_status=1):
    """
    Exit the program with a non zero exit status.
    :param exit_status:
    :return:
    """
    sys.exit(exit_status)
