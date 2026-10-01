number = 10

print (number)

def test_global():
    #si elimino linea 7, la variable no se modifica por ser global.
    global number
    number = 20

def test_local():
    local_number = 30
    print (local_number)


test_global()
print (number)

test_local()
print (local_number)
