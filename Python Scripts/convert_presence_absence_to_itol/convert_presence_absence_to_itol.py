import pandas as pd

df = pd.read_excel('Input_Folder/Input_Presence_Absence.xlsx', sheet_name='Sheet1', index_col=0)

df_t = df.T

shapes = ['circle', 'square', 'triangle', 'star', 'diamond']

shape_list = [shapes[i % len(shapes)] for i in range(df_t.shape[1])]

colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a']
color_list = [colors[i % len(colors)] for i in range(df_t.shape[1])]

with open('itol_dataset_binary.txt', 'w') as f:
    f.write("DATASET_BINARY\n")
    f.write("SEPARATOR TAB\n")
    f.write("DATASET_LABEL\tCyanorak Clusters\n")
    f.write("FIELD_LABELS\t" + "\t".join(df_t.columns) + "\n")
    f.write("FIELD_COLORS\t" + "\t".join(color_list) + "\n")
    f.write("FIELD_SHAPES\t" + "\t".join(shape_list) + "\n")
    f.write("DATA\n")
    for strain, row in df_t.iterrows():
        f.write(str(strain) + "\t" + "\t".join(map(str, row)) + "\n")
