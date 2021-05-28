def run():
    my_list = [1,"Hello",True, 4.5]
    my_dict = {"firstName": "Osnayder","lastName":"Severiche"}

    super_list = [
        {"firstName": "Osnayder","lastName":"Severiche"},
        {"firstName": "Osnayder2","lastName":"Severiche2"},
        {"firstName": "Osnayder3","lastName":"Severiche3"},
        {"firstName": "Osnayder4","lastName":"Severiche4"},
        {"firstName": "Osnayder5","lastName":"Severiche5"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-2-1,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key," - ", value)

if __name__ == '__main__':
    run()
