def a(st):
    if len(st) <= 1:
        return st
    
    f = st[0]
    l = st[1:]
    return a(l)+f
    
def main():
    print a("this is a test")
    
if __name__ == '__main__':
    main()