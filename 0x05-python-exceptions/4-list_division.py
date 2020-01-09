#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    div = 0

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("{}".format("wrong type"))
            div = 0
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            div = 0
        except IndexError:
            print("{}".format("out of range"))
            div = 0
        finally:
            length.append(div)
    return length
