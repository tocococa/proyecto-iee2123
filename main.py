import os


def to_bits(path_in, path_out):
    path_in = os.path.join(os.getcwd(), path_in)
    path_out = os.path.join(os.getcwd(), path_out)
    with open(path_in, 'r') as file:
        line = file.readline()
        bytes_file = line
        files_out = {x: [] for x in range(8)}
        time = 0
        for i in range(0, len(bytes_file), 9):
            # leer en grupos de 9 caracetres (byte+space)
            byte = bytes_file[i:i+8]
            for k in range(len(byte)):
                # revisar cada bit del byte
                if byte[k] == '1':
                    out = str(time*100)+'us 5V\n'
                elif byte[k] == '0':
                    out = str(time*100)+'us 0V\n'
                files_out[k].append(out)
            time += 1
    for k in files_out.keys():
        path_file = path_out + f'{k+1}b.txt'
        with open(path_file, 'a') as file:
            for j in files_out[k]:
                file.write(j)


if __name__ == '__main__':
    try:
        to_bits('tripulantes/tripulante1.txt', 'tripulantes/out_t1/')
        to_bits('tripulantes/tripulante2.txt', 'tripulantes/out_t2/')
    except IOError as err:
        print(f"Error: {err}")
