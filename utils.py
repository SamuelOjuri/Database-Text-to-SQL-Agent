from dotenv import load_dotenv
import mysql.connector
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits.sql.base import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from sqlalchemy import create_engine
from urllib.parse import quote_plus

import os

# Load .env file for database credentials
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# Create a connection to the MySQL database
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return True, conn
    except mysql.connector.Error:
        return False, "Could not establish a database connection"

# Print table names from database
def show_tables(cursor):
    table_list = []
    try:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        if tables:
            for table in tables:
                table_list.append(table[0])
        else:
            print("No tables found in the database.")
    except mysql.connector.Error:
        return False, "Error fetching tables"
    return True, table_list

# Create a new SQLAlchemy engine
def create_engine_connection():
    DB_PASS_QUOTED = quote_plus(DB_PASS)
    connection_string = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS_QUOTED}@{DB_HOST}/{DB_NAME}'
    engine = create_engine(connection_string)
    return engine

# Setup Langchain Agent Executor
def setup_agent_executor(engine):
    db = SQLDatabase(engine=engine)
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        handle_parsing_errors=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        output_parser=CommaSeparatedListOutputParser(),
        verbose=True
    )
    return agent_executor



#