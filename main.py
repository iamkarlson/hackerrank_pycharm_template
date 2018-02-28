f = open("input.txt", mode='r')
o = open("output.txt")

def finput():
    return f.readline()
def oread():
    return o.readline()
def output(out_text):
    assert out_text == oread()
    print(out_text)


def op1(data):
    pass
def op2(data):
    pass


input_data_rows = int(finput().strip())

for row_0 in range(input_data_rows):
    in_data = finput().strip().split(' ')
    command = in_data[0]
    if command == "1":
        op1(in_data)
    elif command == "2":
        op2()
    output("")
