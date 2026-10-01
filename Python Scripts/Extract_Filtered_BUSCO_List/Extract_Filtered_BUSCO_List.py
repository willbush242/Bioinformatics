import pandas as pd

file_path = r"BUSCO_summary.xlsx"

df = pd.read_excel(file_path)

filtered_df = df[
    (df['C'] >= 95) &
    (df['S'] >= 95) &
    (df['D'] <= 2.5) &
    (df['F'] <= 2.5) &
    (df['M'] <= 2.5)
]

gca_names = filtered_df['GCA'].tolist()

output_file = r"GCA_names_filtered.txt"

with open(output_file, 'w') as f:
    for name in gca_names:
        f.write(name + '\n')

print(f"GCA names saved to {output_file}")
print(f"Total number meeting the criteria: {len(gca_names)}")
