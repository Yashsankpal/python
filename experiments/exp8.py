#try catch problem

try:
    #print(x)
    #print(1/0)
    #print('2'+2)
    #x=[]
    #print(x[0])
    #f = open ( "foo.txt", 'r' )
    #a = 0
    #assert a!=0
except NameError:
    print('NameError')
except TypeError:
    print('TypeError')
except AssertionError:
    print('AssertionError')
except IndexError:
    print('IndexError')
except ZeroDivisionError:
    print('ZeroDivisionError')
except IOError:
    print('IOError')