from backend.function import Function, Property
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from backend.utils import create_engine_connection  

load_dotenv()


class GetDBSchema(Function):
    def __init__(self):
        super().__init__(
            name="get_db_schema",
            description="Get the schema of the database",
        )

    def function(self):
        engine = create_engine_connection()  
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        schema_data_statements = []

        for table_name in table_names:
            # Schema retrieval
            table = inspector.get_columns(table_name)
            create_statement = f"CREATE TABLE {table_name} (\n"
            create_statement += ",\n".join(
                f"{col['name']} {col['type']}" for col in table
            )
            create_statement += "\n);\n"

            # Sample data retrieval
            sample_data_query = f"SELECT * FROM {table_name} LIMIT 3;"
            with engine.connect() as connection:
                results = connection.execute(text(sample_data_query)).fetchall()

            sample_data_result = '\n'.join([str(result) for result in results])

            combined_statement = create_statement + "\n" + sample_data_query + "\n" + sample_data_result
            schema_data_statements.append(combined_statement)

        return "\n\n".join(schema_data_statements)
    
class RunSQLQuery(Function):
    def __init__(self):
        super().__init__(
            name="run_sql_query",
            description="Run a SQL query on the database",
            parameters=[
                Property(
                    name="query",
                    description="The SQL query to run",
                    type="string",
                    required=True,
                ),
            ],
        )

    def function(self, query):
        engine = create_engine_connection()  # Use the function from utils.py
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            with engine.connect() as connection:
                results = connection.execute(text(query)).fetchall()

            return '\n'.join([str(result) for result in results])
        except Exception as e:
            return str(e)
        finally:
            session.close()

