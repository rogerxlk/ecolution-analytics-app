# Ecolution Operational Analytics

## Table of Content
* [Description](#description)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
  * [1. Clone the repository](#1.-clone-the-repository)
  * [2. Install dependencies with Poetry](#2.-install-dependencies-with-poetry)
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
### 2. Install dependencies with Poetry
This project requires some dependencies to be installed. If you don't have Poetry installed, download the latest version from https://python-poetry.org/docs/#installation, and then run the following command:
```bash
  curl -sSL https://install.python-poetry.org | python3 -
```
  
After installing Poetry, use the following command to install the project's dependencies in your repo directory (cd REPO_DIRECTORY):
```bash
poetry install
 ```

### 3. Set up pre-commit hooks
To run pre-commit automatically before each commit, set up the pre-commit hooks by running the following command in your repo directory (cd REPO_DIRECTORY):
```bash
pre-commit install
   ```

## Poetry Commands
This project uses Poetry to manage its dependencies. If you have made changes to the pyproject.toml file, you can use the following commands to update the dependencies:

- `poetry add <package-name>` - Add a new dependency to the project
- `poetry remove <package-name>` - Remove a dependency from the project
- `poetry update <package-name>` - Update a dependency to the latest version
- `poetry install` - Install the dependencies for the project and update poetry.lock

## Support
If you encounter any issues or have any questions about this project, please feel free to open an issue in this repository. 

## License
This project is confidential and proprietary to Ecolution Engineering GmbH. This license is granted solely for internal use by authorized employees. Any external use, disclosure, distribution or reproduction of the project or any portion thereof is strictly prohibited.