### 🔐 Account Keeper

Command-line application (CLI) designed for efficient and organized management of digital accounts. The database is fully portable, allowing access to data from anywhere without the need for an internet connection.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Typer](https://img.shields.io/badge/Typer-000000?style=for-the-badge)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🛠️ Installation

The system was developed using **Python 3.12**, and it is recommended to use this version for compatibility.

To obtain a local copy of the source code, run the following command:

```bash
git clone https://github.com/davidsantana06/account-keeper
```

Next, install the application dependencies with:

```bash
pip install -r requirements.txt
```

### 🤖 Commands

#### ![Create Account](https://img.shields.io/badge/C-Create_Account-28a745?style=for-the-badge)

```bash
python -m app account create <name> <username> <email> <phone>
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| Name      | `name`        | `string` | 👍           |
| Username  | `username`    | `string` | 👎           |
| E-mail    | `email`       | `string` | 👎           |
| Phone     | `phone`       | `string` | 👎           |

#

#### ![Retrieve All Accounts](https://img.shields.io/badge/R-Retrieve_All_Accounts-007bff?style=for-the-badge)

```bash
python -m app account all
```

#

#### ![Retrieve All Accounts By Name](https://img.shields.io/badge/R-Retrieve_All_Accounts_By_Name-007bff?style=for-the-badge)

```bash
python -m app account all --name <name>
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| Name      | `name`        | `string` | 👍           |

#

#### ![Retrieve One Account By ID](https://img.shields.io/badge/R-Retrieve_One_Account_By_ID-007bff?style=for-the-badge)

```bash
python -m app account one --id <id>
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| ID        | `id`          | `string` | 👍           |

#

#### ![Retrieve One Account By ID](https://img.shields.io/badge/R-Retrieve_One_Account_By_Name-007bff?style=for-the-badge)

```bash
python -m app account one --name <name>
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| Name      | `name`        | `string` | 👍           |

#

#### ![Update Account Name](https://img.shields.io/badge/U-Update_Account_Name-ffc107?style=for-the-badge)

```bash
python -m app account update <id> --name <name>
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| ID        | `id`          | `string` | 👍           |
| Name      | `name`        | `string` | 👍           |

#

#### ![Update Account Password](https://img.shields.io/badge/U-Update_Account_Password-ffc107?style=for-the-badge)

```bash
python -m app account update <id> --password
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| ID        | `id`          | `string` | 👍           |
| Password  | `password`    | `string` | 👍           |

#

#### ![Delete Account](https://img.shields.io/badge/D-Delete_Account-dc3545?style=for-the-badge)

```bash
python -m app account delete <id>
```

| **Field** | **Parameter** | **Type** | **Required** |
| --------- | ------------- | -------- | ------------ |
| ID        | `id`          | `string` | 👍           |

### ⚖️ License

This project adopts the **MIT License**, which allows you to use and make modifications to the code as you wish. The only thing I ask is that proper credit is given, acknowledging the effort and time I invested in building it.
