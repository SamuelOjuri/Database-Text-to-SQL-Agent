# Database-Text-to-SQL-Agent
Database Analyst with OpenAI Assistant API

## Deriving Business Insights from Relational Database Management Systems with Natural Language

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Structure](#code-structure)

---

## Introduction

As recent advancements make it easier to leverage the use of Large Language Models in business solutions, the potential for widespread adoption of this approach is increasingly promising. Most organizations across several industries store their data about business processes and transactions in Relational Database Management Systems. Retrieving business-critical insights from these data stores has the limitation of technical expertise in Structured Query Language (SQL). The project aims to provide a solution that enables non-technical stakeholders to easily query databases using natural language and retrieve insights about the business's key performance indicators and opportunities in real-time. It aims to allow appropriate non-technical stakeholders to use natural language for retrieving desired information from their RDBMS and also access advanced data analytics reports and dashboards derived from their queries using an intelligent agent and a competent large language model within an integrated framework. 

This application provides an intuitive interface for users to derive business insights directly from their databases by using natural language queries. Leveraging OpenAI Assistant's API as an intelligent agent and the OpenAI's GPT-4 model as a reasoning engine, the application executes SQL queries behind the scenes to generate informative responses.

### Notebook
[Google Colab Notebook] (https://colab.research.google.com/drive/1x0s4xxrwGjzSC3Fz2uhMwsp-TNvD5L1Q?usp=sharing)

### Architecture
![image](https://github.com/SamuelOjuri/Business_Insights_from_RDBMS_with_Natural_Language/blob/main/SQL_database_agent_workflow.png)

---

## Requirements
- The project uses MySQL Demo Database for Analysis: [MySQL classicmodels dataset] (https://www.mysqltutorial.org/mysql-sample-database.aspx) . A sample database was set up in Google Cloud using the example credentials provided.
- OpenAI API Key is required for the use of the LLM in this prototype: [How to get OpenAI API Key] (https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

### System Requirements
- Python 3.8+
- MySQL database

### Environment Variables
Create a `.env` file at the root directory with the following variables:
- `OPENAI_API_KEY` : OpenAI API Key
- `DB_HOST` : Database host address
- `DB_USER` : Database user
- `DB_PASS` : Database password
- `DB_NAME` : Database name

Example:
```env
OPENAI_API_KEY=set-openai-api-key
DB_HOST=35.197.251.91
DB_USER=root
DB_PASS=P@ssw0rd
DB_NAME=classicmodels
```

---

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/your_repository.git
    ```
    
2. Navigate to the project directory:

    ```
    cd your_repository
    ```

3. Create a Python virtual environment: 

`python3 -m venv venv`

Activate your environment (change 'bin' to 'Scripts' or 'Source' directory depending on which OS you are using): 

`. venv/bin/activate`

Add the base directory path (current working directory) to a `basepath.pth` file in `Database-Text-to-SQL-Agent/venv/lib/python3.10/site-packages/`

```
import os

path = os.getcwd()

print(path)
```

4. Install required packages:

    ```
    pip install -r requirements.txt
    ```

---

## Usage

1. Open your terminal and run the following command:

    - streamlit run main.py   

    This will launch a Streamlit interface.

2. Access the Streamlit interface by visiting the URL provided in the terminal.

3. Type your question into the textbox and click "Chat with Assistant" button to get your insights.

---

## Code Structure

- **utils.py**: Contains utility functions such as:

    - `get_db_connection()`: Establishes a MySQL database connection.
    - `show_tables(cursor)`: Prints table names from the database.
    - `create_engine_connection()`: Creates a SQLAlchemy engine.

- **main.py**: Entry point of the application. Initializes Streamlit UI and manages the execution of the OpenAI Assistant (Agent).

- **.env**: Stores environment variables required for the application.

- **requirements.txt**: List of Python packages required for the application.

---


