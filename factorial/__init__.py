import check50

@check50.check()
def exists():
    """factorial.py exists"""
    check50.exists("factorial.py")

@check50.check(exists)

def rejectneg():
    """rejects negative numbers"""
    from re import match
    expected = "Please enter a non-negative number: "
    actual = check50.run("python3 factorial.py").stdin("-5", prompt=False).stdout()
    if not match(expected, actual):
        help = None
        raise check50.Mispatch("factorial\n", actual)
def factorial():
    """factorial"""
    check50.run("python3 factorial.py").stdin("0", prompt=False).stdout("1", regex=False).exit(0)
    check50.run("python3 factorial.py").stdin("1", prompt=False).stdout("1", regex=False).exit(0)
    check50.run("python3 factorial.py").stdin("5", prompt=False).stdout("120", regex=False).exit()
    check50.run("python3 factorial.py").stdin("15", prompt=False).stdout("1307674368000", regex=False).exit()
