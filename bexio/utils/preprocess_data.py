import pandas as pd


def load_data_bexio():
    df = pd.read_csv("data/raw/journal.csv")
    return df


# # pasiven_range = range(2000, 3000) #todo: doesnt work as it should
# # aktiven_range = range(1000, 2000) #todo: doesnt work as it should
# aufwand_range = range(4000, 6941)
# ertrag_range = list(range(3000, 4000)) + [6950, 8100, 8710]
# grouped_data_frames = {}
#
# directory = "../../src/bexio/data/processed"
# os.makedirs(directory, exist_ok=True)
#
# for index, row in df.iterrows():
#     haben_entry = int(row['Haben'].split(" - ")[0])
#     if haben_entry in aufwand_range:
#         category = 'aufwand'
#     elif haben_entry in ertrag_range:
#         category = 'ertrag'
#     # elif haben_entry in pasiven_range:
#     #     category = 'passiven'
#     # elif haben_entry in aktiven_range:
#     #     category = 'aktiven'
#     else:
#         continue
#
#     if category not in grouped_data_frames:
#         grouped_data_frames[category] = pd.DataFrame(columns=df.columns)
#
#     grouped_data_frames[category] = pd.concat([grouped_data_frames[category], row.to_frame().T])
#
# for category, data_frame in grouped_data_frames.items():
#     filename = f"{directory}/{category}.csv"
#     data_frame.to_csv(filename, index=False)
