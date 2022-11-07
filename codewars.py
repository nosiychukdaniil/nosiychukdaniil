def remove_char(s):
    f = s.split()
    f = f.pop()
    f = f.pop(0)
    return f.join()
print(remove_char('ehelloe'))