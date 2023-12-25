from dotenv import load_dotenv
import streamlit as st
import os
from io import BytesIO
from backend.assistant import AIAssistant
from backend.sql_assistant import GetDBSchema, RunSQLQuery


load_dotenv()



st.markdown("<h2 style='text-align: left; color: black;'>🔍 Database Query Assistant</h2>", unsafe_allow_html=True)
st.write("Interact with the Database Query Assistant using natural language queries.")
st.write("The Assistant can provide information about the database schema and execute SQL queries.")
st.write(
    "- Enter your questions about the MySQL classicmodels database and click the 'Chat with Assistant' button to get answers."
)
st.write("- You can type in 'bye' or 'exit' to quit when you are done.")

# Display example input questions
st.write("Example questions about classicmodels database:")
st.markdown("""
- List the top 10 customers by total payments.
- Create a data visualisation for the number of orders by product line.
- List the top 10 products by payments.
- Create a word cloud for the sales employees by performance.
- What is the total quantity of products sold for each product line.
- Create a line graph for the sum of quantity ordered by month for the year 2003.
""")

user_input = st.text_input("Enter your question:")

if st.button("Chat with Assistant"):
    assistant = AIAssistant(
        instruction="""
        You are a SQL expert. User asks you questions about the MySQL classicmodels database.
        First obtain the schema of the database to check the tables and columns, then generate SQL queries to answer the questions.
        """,
        #model="gpt-3.5-turbo-1106",
        model="gpt-4-1106-preview",
        functions=[GetDBSchema(), RunSQLQuery()],
        use_code_interpreter=True,
    )

    response_content = assistant.streamlit_chat(user_input)

    # Check if the response content is a byte stream indicating an image
    if isinstance(response_content, BytesIO):
        # Display the image from the byte stream
        st.image(response_content, use_column_width=True)
    else:
        # Display text output.
        st.text(response_content)
 
