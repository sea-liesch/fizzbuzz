def fizz_bizz():
    """
    docstring
    """
    pass
    for i in range (1-101):
        if i % 3 == 0 |  i % 5 == 0:
            print("Fizzbizz")
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Bizz")
        else:
            print(i)
fizz_bizz()