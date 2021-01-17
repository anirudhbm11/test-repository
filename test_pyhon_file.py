def multiply(x,y):
    return x*y

def subtract(x,y):
    return x-y

def divide(x,y):
    if y == 0:
        print("Cannot divide")
        print("\n use another number")
        return
    else:
        return x/y

def modulo(x,y):
    return x%y

if __name__ == "__main__":
    ans = multiply(2,3)
    print(ans)