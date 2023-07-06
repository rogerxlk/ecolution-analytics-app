# Ecolution Operational Analytics

## Table of Content

* [Description](#description)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
    * [1. Clone the repository](#1.-clone-the-repository)
    * [2. Install dependencies with pip](#2.-install-dependencies-with-pip)
    * [3. Set up pre-commit hooks](#3.-set-up-pre-commit-hooks)
* [Poetry Commands](#poetry-commands)
* [Support](#support)
* [License](#license)

## Used APIs

- [Notion API](https://developers.notion.com/)
- [Bexio API](https://docs.bexio.com)

## Used Visualization Libraries

- [Plotly](https://plotly.com/python/)
- [Dash](https://dash.plotly.com/)
- [Streamlit](https://streamlit.io/gallery)

## Prerequisites

Python 3.9 or higher is installed on your machine.

Check the Python version

```bash
python3 --version
```

You can download it from the official website: https://www.python.org/downloads/.

```bash
sudo apt-get install python3
python3 --version
```

## Installation

### 1. Clone the repository

To get started, clone the project repository to your local machine:

```bash
  git https://github.com/rogerxlk/ecolution-analytics.git
   ```

### 2. Install dependencies with pip

This project requires some dependencies to be installed. If you don't have pip installed, download the latest version,
and then run the following command:

```bash
  curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
python3 get-pip.py
```

After installing pip, use the following command to install the project's dependencies in your repo directory (cd
REPO_DIRECTORY):

- macOs/Linus:
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
   ```
- windows:
  ```bash
    python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
   ```

### 3. Set up pre-commit hooks

To run pre-commit automatically before each commit, set up the pre-commit hooks by running the following command in your
repo directory (cd REPO_DIRECTORY):

```bash
pre-commit install
   ```

## pip Commands

This project uses pip to manage its dependencies. Use the following command to add new libraries to requirements.txt:

```bash
pip freeze > requirements.txt
```

## Support

If you encounter any issues or have any questions about this project, please feel free to open an issue in this
repository.

## License

This project is confidential and proprietary to Ecolution Engineering GmbH. This license is granted solely for internal
use by authorized employees. Any external use, disclosure, distribution or reproduction of the project or any portion
thereof is strictly prohibited.