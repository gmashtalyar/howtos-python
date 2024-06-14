

def myfunction(parameter: int) -> str:
    return f"{parameter + 10}"


def otherfunction(otherparameter: str):
    print(otherparameter)


otherfunction(myfunction(20))


def dosmth(param: list[int]):
    pass


