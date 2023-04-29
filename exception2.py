try:
    num=int(input("Enter any number"))
    if num<=0:
        raise ValueError("This is not a positive number")
    else:
        raise ValueError("This is a positive number")
except ValueError as error:
    print(error)
    