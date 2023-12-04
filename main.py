import gradio as gr
from utils import setup_agent_executor, create_engine_connection, get_db_connection, show_tables
import os

# Retrieve the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create a reusable database connection
success, connection_or_msg = get_db_connection()
if not success:
    print("Application terminated: ", connection_or_msg)
    exit()

engine = create_engine_connection()

# Create a reusable Langchain Agent Executor
agent_executor = setup_agent_executor(engine)

def run_agent(query):
    response = agent_executor.run(query)
    return response

def populate_query(example_value, _):
    return example_value

# Define the Gradio interface
blocks = gr.Blocks()

with blocks:
    gr.Markdown("""<h1><center>Derive Business Insights from Database</center></h1>""")
    with gr.Row():
        with gr.Column():
            gr.Markdown("""<h2 style="text-align:left;">Sample Questions:</h2>""")
            with gr.Row():
                example1 = gr.Button(value="List the top 10 highest paying customers and the total payments for each customer")
                example2 = gr.Button(value="List the top 10 most frequent customers")
            with gr.Row():
                example3 = gr.Button(value="List the number of orders by productline")
                example4 = gr.Button(value="List the sum of quantity ordered by year")
            query = gr.Textbox(lines=5, label="Enter question")
            with gr.Row():
                gr.ClearButton(query)
                input_btn = gr.Button(value="Submit")
        with gr.Column():
            gr.Markdown("""<h2 style="text-align:left;">Derived Response:</h2>""")
            agent_output = gr.Textbox(label="Output", lines=15)

    example1.click(populate_query, inputs=[example1, query], outputs=[query])
    example2.click(populate_query, inputs=[example2, query], outputs=[query])
    example3.click(populate_query, inputs=[example3, query], outputs=[query])
    example4.click(populate_query, inputs=[example4, query], outputs=[query])

    input_btn.click(run_agent, inputs=[query], outputs=[agent_output], api_name="derive-insights")

blocks.launch(share=True, server_port=5004)