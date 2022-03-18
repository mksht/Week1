def test_solution(monkeypatch):
    x=['ByteAcademy']
    index=-1

    #def f(string): #f(string) is expecting input. if there is no input there'll be error.
    #def f(string) will work
    def f(string = None):
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input',f)

    from solution import string, strlen
    assert type(string) == str
    assert strlen == len(string)
  

    