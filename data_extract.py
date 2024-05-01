import os
import csv
import pandas as pd

def data_extract(wdr):
    idv_files = [filename for filename in os.listdir(wdr) if filename.startswith('idv')]
    data = []

    for idv_file in idv_files:
        idv_path = os.path.join(wdr, idv_file)
        clcd, dv = read_data_from_csv_files(idv_path)
        data.append([dv[0], dv[1], clcd[0], clcd[1]])

    return pd.DataFrame(data, columns=['x', 'y', 'cl', 'CD'])

# Implement the read_data_from_csv_files function to read data from CSV files
def read_data_from_csv_files(idv_path):
    dv = []
    clcd = []
    # Read data from 'DVs.csv' file
    with open(os.path.join(idv_path, 'DVs.csv'), 'r') as dv_file:
        dv_reader = csv.reader(dv_file)
        dv_data = list(dv_reader)
        dv.append(float(dv_data[0][0]))  # Assuming the first column contains x values
        dv.append(float(dv_data[0][1]))  # Assuming the second column contains y values

    # Read data from 'cl_cd_idv.csv' file
    with open(os.path.join(idv_path, 'cl_cd_idv.csv'), 'r') as clcd_file:
        clcd_reader = csv.reader(clcd_file)
        clcd_data = list(clcd_reader)
        clcd.append(float(clcd_data[0][0]))  # Assuming the first cell contains cl value
        clcd.append(float(clcd_data[0][1]))  # Assuming the second cell contains CD value

    return clcd, dv

# Main code
ngen = 2
neval = 30 + 15 * (ngen - 1)
output_directory = 'C:\\Users\\bzdell\\Desktop\\FYP3004'

gen_data = {}
for i in range(1, ngen + 1):
    gen = 'gen_{}'.format(i)
    wdr = os.path.join(output_directory, gen)
    gen_data[gen] = data_extract(wdr)
    
    # Output x, y, cl, CD of each generation to CSV
    gen_csv_filename = os.path.join(output_directory, 'generation_{}.csv'.format(i))
    gen_data[gen].to_csv(gen_csv_filename, index=False)
    print("CSV file for {} generation saved as '{}'.".format(gen, gen_csv_filename))

# Combine all x, y, cl, and CD values into arrays
combined_cl = []
combined_x = []
combined_y = []
combined_CD = []

for gen, df in gen_data.items():
    combined_x.extend(df['x'].tolist())
    combined_y.extend(df['y'].tolist())
    combined_cl.extend(df['cl'].tolist())
    combined_CD.extend(df['CD'].tolist())

# Create a DataFrame from the combined data
combined_df = pd.DataFrame({
    'x': combined_x,
    'y': combined_y,
    'cl': combined_cl,
    'CD': combined_CD
})

# Output the combined DataFrame to CSV
combined_csv_filename = os.path.join(output_directory, 'combined_data.csv')
combined_df.to_csv(combined_csv_filename, index=False)
print("Combined DataFrame saved as '{}'.".format(combined_csv_filename))
