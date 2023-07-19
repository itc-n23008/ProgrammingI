str_num_list = map(lambda x: "{:04}".format(x), range(1, 8))

print(["{:0=4}".format(x) for x in range(1, 8)])

print(("{:0=4}".format(x) for x in range(1, 8)))

print(list("{:0=4}".format(x) for x in range(1, 8)))
