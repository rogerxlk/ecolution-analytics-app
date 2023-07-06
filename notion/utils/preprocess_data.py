import os
import pandas as pd
import ast


def load_data_notion():
    df = process_df_service()
    df_track = process_df_time_tracking()

    df_Done = df[df["Done"] == True]
    df_Undone = df[df["Done"] == False]

    return df, df_track, df_Done, df_Undone


def process_df_time_tracking():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data",
        "raw",
        "energieberatungDb_time_tracking.csv",
    )
    df_track = pd.read_csv(file_path)
    columns_to_keep = [
        "properties.LastEditedTime.last_edited_time",
        "properties.Hours.number",
        "properties.Name.title",
        "properties.ParentTasks.relation",
    ]
    df_track = df_track.loc[:, columns_to_keep]
    rename_dict = {col: col.split(".")[1] for col in df_track.columns}
    df_track.rename(columns=rename_dict, inplace=True)
    df_track = df_track.dropna(subset=["Hours"])
    df_track["LastEditedTime"] = pd.to_datetime(df_track["LastEditedTime"])
    df_track["Year"] = df_track["LastEditedTime"].dt.year
    df_track["Month"] = df_track["LastEditedTime"].dt.month
    df_track = df_track.copy()
    df_track["ParentTasks"] = df_track["ParentTasks"].apply(extract_id)
    df_track.loc[:, "Name"] = df_track["Name"].apply(extract_name)
    return df_track


def process_df_service():
    file_path = os.path.join(
        os.path.dirname(__file__), "../data", "raw", "energieberatungDb_services.csv"
    )
    df = pd.read_csv(file_path)
    columns_to_keep = [
        "properties.InternalHourlyRate.number",
        "properties.NetMargin.formula.number",
        "properties.Progress.formula.number",
        "properties.NetBudget.number",
        "properties.Priority.formula.string",
        "properties.Usage.multi_select",
        "properties.ExpenseCHF.formula.number",
        "properties.Done.formula.boolean",
        "properties.DateOrder.created_time",
        "properties.Name.title",
        "properties.Service.select.name",
        "properties.Canton.select.name",
        "properties.📨 Fakturieren.checkbox",
        "properties.💸 RE(n) versendet.checkbox",
        "properties.BuildingRecording.date.start",
    ]
    df = df.loc[:, columns_to_keep]
    rename_dict = {col: col.split(".")[1] for col in df.columns}
    df.rename(columns=rename_dict, inplace=True)
    df = df.dropna(subset=["NetBudget", "InternalHourlyRate"])
    df["DateOrder"] = pd.to_datetime(df["DateOrder"])
    df["Year"] = df["DateOrder"].dt.year
    df["Month"] = df["DateOrder"].dt.month
    df = df.copy()
    df.loc[:, "Usage"] = df["Usage"].apply(extract_usages)
    df.loc[:, "Name"] = df["Name"].apply(extract_title)

    # drop rows with building record date in 2022
    df = df[~df["BuildingRecording"].astype(str).str.contains("2022")]
    return df


def extract_title(data_string):
    try:
        first_split = data_string.split("'content': '", 1)[1]
        content = first_split.split("', 'link':", 1)[0]
        return content
    except IndexError:
        return None


def extract_usages(data):
    try:
        if data is None or data == []:
            return None
        data_string = str(data)
        splits = data_string.split("'name': '")
        splits = splits[1:]
        usages = [split.split("'", 1)[0] for split in splits]
        return usages
    except Exception as e:
        print(f"Error: {e}")
        print(f"Data: {data}")
        return None


def extract_id(data_string):
    data_list = ast.literal_eval(data_string)

    for item in data_list:
        if "id" in item:
            return item["id"]

    return None


def extract_name(data_string):
    data_list = ast.literal_eval(data_string)

    for item in data_list:
        if "text" in item and "content" in item["text"]:
            return item["text"]["content"]

    return None
