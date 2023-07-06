#!/usr/bin/env python3
import requests
import pandas as pd
import logging
from config import BEXIO_API_KEY

"""Fetch Bexio databases to a specified directory."""

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

headers = {"Accept": "application/json", "Authorization": f"Bearer {BEXIO_API_KEY}"}

base_url = "https://api.bexio.com/"

endpoints = {
    "journal": {"endpoint": "3.0/accounting/journal", "limit": 2000},
    "orders": {"endpoint": "2.0/kb_order", "limit": 2000},
    "offers": {"endpoint": "2.0/kb_offer", "limit": 2000},
    "invoices": {"endpoint": "2.0/kb_invoice", "limit": 2000},
    "account_groups": {"endpoint": "2.0/account_groups", "limit": 2000},
    "accounts": {"endpoint": "2.0/accounts", "limit": 2000},
}


def fetch_bexio_data():
    """
    Fetches data from Bexio API and saves it to CSV files.

    The data is fetched for the specified endpoints and saved to separate CSV files in the '../data/raw/' directory.

    Returns:
        None
    """

    logging.info("Start fetching Bexio databases...")

    for name, config in endpoints.items():
        offset = 0
        all_data = []
        endpoint = config["endpoint"]
        pagination_limit = config["limit"]

        while True:
            params = {"limit": pagination_limit, "offset": offset}
            response = requests.get(
                f"{base_url}{endpoint}", headers=headers, params=params
            )
            data = response.json()

            if not data:
                break

            if "data" in data:
                all_data.extend(data["data"])
            else:
                all_data.extend(data)

            if len(data) < pagination_limit:
                break

            offset += pagination_limit

        if all_data:
            if isinstance(all_data[0], dict):
                df = pd.DataFrame(all_data)
                df.to_csv(f"../data/raw/{name}.csv", index=False)
                logging.info(
                    f"Downloaded data for {name} and saved to ../data/raw/{name}.csv"
                )
            elif isinstance(all_data[0], list):
                for item in all_data:
                    df = pd.DataFrame(item)
                    df.to_csv(f"../data/raw/{name}.csv", index=False)
                logging.info(
                    f"Downloaded data for {name} and saved to ../data/raw/{name}.csv"
                )
            else:
                logging.warning(f"Unexpected data format for {name}: {data}")
        else:
            logging.warning(f"No data found for {name}")

    logging.info("Fetched all databases successfully!")


if __name__ == "__main__":
    fetch_bexio_data()
