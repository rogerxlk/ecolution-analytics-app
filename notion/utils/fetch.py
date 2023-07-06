#!/usr/bin/env python3

import os
import pandas as pd
import requests
import logging
from config import NOTION_API_KEY

"""Fetch Notion databases to a specified directory."""

headers = {
    "Authorization": "Bearer " + NOTION_API_KEY,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def fetch_single_notion_database(database_id, database_name, target_dir):
    """
    Fetches a Notion database with the specified database ID and name to a local directory.

    Args:
        database_id (str): The ID of the database to fetch.
        database_name (str): The name of the database to fetch.
        target_dir (str): The path to the directory where downloaded file should be stored.
    """

    global target_file_path
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    payload = {"page_size": 100}
    has_more = True

    logging.info("Start fetching Notion databases...")

    df = pd.DataFrame()

    while has_more:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            new_data = pd.json_normalize(data["results"])
            df = pd.concat([df, new_data], ignore_index=True)

            has_more = data.get("has_more", False)
            if has_more:
                payload["start_cursor"] = data["next_cursor"]
        else:
            logging.error(
                f"Request failed with status code {response.status_code}. You may not have set the Connection for the "
                f"database in Notion!"
            )
            has_more = False

    # Split the data into two dataframes
    df_not_null = df[df["properties.Canton.select.name"].notna()]
    df_null = df[df["properties.Canton.select.name"].isna()]

    # Save the two dataframes to two separate files
    file_name_not_null = f"{database_name}_services.csv"
    target_file_path_not_null = os.path.join(target_dir, file_name_not_null)
    logging.info(
        f"Downloaded {database_name} database with not null properties.Canton.select.name and saved to {target_file_path_not_null}"
    )
    df_not_null.to_csv(target_file_path_not_null, index=False)

    file_name_null = f"{database_name}_time_tracking.csv"
    target_file_path_null = os.path.join(target_dir, file_name_null)
    logging.info(
        f"Downloaded {database_name} database with null properties.Canton.select.name and saved to {target_file_path_null}"
    )
    df_null.to_csv(target_file_path_null, index=False)


def fetch_all_notion_databases(databases, os_dir):
    """
    Fetches all Notion databases in the specified list to a local directory.

    Args:
        databases (list): A list of dictionaries containing information about the databases to fetch.
            Each dictionary should have the keys 'database_id' and 'database_name'.
        os_dir (str): The path to the directory where the fetched databases should be stored.
    """

    for database in databases:
        database_id = database["database_id"]
        database_name = database["database_name"]
        fetch_single_notion_database(database_id, database_name, os_dir)

    logging.info("Fetched all databases successfully!")


if __name__ == "__main__":
    target_dir = "../data/raw"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    databases = [
        {
            "database_id": "bd59729a3af8461a84b61bf06094980c",
            "database_name": "energieberatungDb",
        },
    ]
    fetch_all_notion_databases(databases, target_dir)
