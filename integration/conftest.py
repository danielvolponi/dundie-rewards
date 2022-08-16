from subprocess import check_output


def test_load():
    """test command load"""
    check_output(["dundie", "load", "tests/assets/people.csv"])