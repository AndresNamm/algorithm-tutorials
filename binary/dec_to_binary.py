from math import floor
def binary_converter(num_in_dec):
    res=[]
    quot=num_in_dec
    if quot==0:
        return [0]
    while quot != 0:
        remainder=quot%2
        quot=floor(quot/2)
        res.insert(0,(remainder))
    return res


def main():
    for i in range(10):
        print(binary_converter(i))


if __name__ == "__main__":
    # execute only if run as a script
    main()