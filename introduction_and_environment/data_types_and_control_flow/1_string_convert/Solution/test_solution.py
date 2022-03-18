def test_solution(monkeypatch):
    x=['hi']
    index=-1

    def f(string):
        nonlocal x
        nonlocal index
        index+=1 #this way f can be called again, meaning inputs can be multiple
        return x[index]

    monkeypatch.setattr('builtins.input',f) # overwriting interactive input and assuming f is input

    from solution import string, data
    if string.isupper():
        assert data == string.lower()
    else:
        assert data == string.upper()

