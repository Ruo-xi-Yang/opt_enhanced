import os
import csv

def data_extract(wdr):
    idv_files = [filename for filename in os.listdir(wdr) if filename.startswith('idv')]
    x = []
    y = []
    cl = []
    CD = []

    for idv_file in idv_files:
        idv_path = os.path.join(wdr, idv_file)
        # Assuming importDVs and importclcd functions read data from CSV files
        dv_x, dv_y, clcd = read_data_from_csv_files(idv_path)
        cl.append(clcd[0][0])
        CD.append(clcd[0][1])
        x.append(dv_x[0])
        y.append(dv_y[0])

    return x, y, cl, CD

# Implement the read_data_from_csv_files function to read data from CSV files
def read_data_from_csv_files(idv_path):
    dv_x = []
    dv_y = []
    clcd = []
    # Read data from 'DVs.csv' and 'cl_cd_idv.csv' files
    with open(os.path.join(idv_path, 'DVs.csv'), 'r') as dv_file:
        dv_reader = csv.reader(dv_file)
        dv_data = list(dv_reader)
        dv_x.append(float(dv_data[0][0]))
        dv_y.append(float(dv_data[0][1]))

    with open(os.path.join(idv_path, 'cl_cd_idv.csv'), 'r') as clcd_file:
        clcd_reader = csv.reader(clcd_file)
        clcd_data = list(clcd_reader)
        clcd.append((float(clcd_data[0][0]), float(clcd_data[0][1])))

    return dv_x, dv_y, clcd

x = [None] * 10
y = [None] * 10
cl = [None] * 10
cd = [None] * 10
pf = [None] * 10
ngen = 2
neval = 30 + 15 * (ngen - 1)

# read the folders and extract x y cl cd
for i in range(1, ngen + 1):
    gen = 'gen_{}'.format(i)
    wdr = os.path.join('C:\\Users\\bzdell\\Desktop\\FYP3004', gen)
    x[i - 1], y[i - 1], cl[i - 1], cd[i - 1] = data_extract(wdr)
