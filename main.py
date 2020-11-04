import os


def to_bits(path_in, path_out):
    path_in = os.path.join(os.getcwd(), path_in)
    path_out = os.path.join(os.getcwd(), path_out)
    with open(path_in, 'rb') as file:
        line = file.readline()
        files_out = {x: [] for x in range(8)}
        for i in range(0, len(bytes_file), 9):
            chunk = bytes_file[i:i+8]
            for k in range(len(chunk)):
                files_out[k].append(chunk[k])
    for k in files_out.keys():
        path_file = path_out + f'{k}b.txt'
        with open(path_file + f'{k}b.txt', 'wb') as file:
            file.write(*files_out[k])
