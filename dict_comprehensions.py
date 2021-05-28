def run():
    # my_dyct = {}

    
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dyct[i] = i**3
    
    my_dyct = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dyct)

if __name__ == '__main__':
    run()
