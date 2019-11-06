import check50


@check50.check()
def exists():
    """factorial.py exists"""
    check50.exists("factorial.py")

@check50.check(exists)
def rejectneg():
    """rejects negative numbers"""
    check50.run("python3 factorial.py").stdin("-5").reject()

    
@check50.check(exists)
def factorial0():
    """factorial for 0"""
    check50.run("python3 factorial.py").stdin("0").stdout("1").exit(0)

    
@check50.check(exists)
def factorial1():
    """factorial for 1"""
    check50.run("python3 factorial.py").stdin("1").stdout("1").exit(0)

@check50.check(exists)
def factoroal5():
     """factorial for 5"""
    check50.run("python3 factorial.py").stdin("5").stdout("120").exit(0)

@check50.check(exists)
def factorial15():
     """factorial for 15"""
    check50.run("python3 factorial.py").stdin("15").stdout("1307674368000").exit(0)
