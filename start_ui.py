import gradio as gr

from manager.file_manager import scan_db
from manager.ui_manager import search_sentence_db, search_user_db


def ui_function_search_user(user_input):
    return search_user_db(user_input)


def ui_function_search_sentence(user_input):
    return search_sentence_db(user_input)


def refresh_dbs():
    return gr.Dropdown(choices=scan_db(), value=scan_db()[0])


with gr.Blocks() as demo:
    gr.Markdown("Connect to a DB")
    with gr.Tab("DB List") as tab_scan_db:
        with gr.Row() as dbs_row:
            dropdown = gr.Dropdown([], label="Chats", info="Select a chat to Query")
            dropdown.change(
                fn=lambda s: gr.Dropdown.update(choices=scan_db()),
                inputs=[dropdown],
                outputs=[dropdown],
            )
            scan_db_text_button = gr.Button("🔄 Scan For DB")
            # scan_db_text_button.click(
            #     write_property(
            #         property_key=PROPERTIES_FILE_JSON_NAME, property_value=dropdown
            #     ),
            #     [],
            #     [],
            # )
            scan_db_text_button.click(refresh_dbs, [], [dropdown])

        with gr.Row() as btn_row:
            create_db_text_button = gr.Button("Create a DB")
            select_db_text_button = gr.Button("Select DB")

            select_db_text_button.click(None, _js="window.location.reload()")

    with gr.Column() as query_col:
        gr.Markdown("Insert Info to search")
        with gr.Tab("User") as user_tab:
            user_text_input = gr.Textbox()
            user_text_output = gr.TextArea()
            user_text_button = gr.Button("Search User")
        with gr.Tab("Sentence") as sentence_tab:
            sentence_text_input = gr.Textbox()
            sentence_text_output = gr.TextArea()
            sentence_text_button = gr.Button("Search Sentence")

        user_text_button.click(
            ui_function_search_user, inputs=user_text_input, outputs=user_text_output
        )
        sentence_text_button.click(
            ui_function_search_sentence,
            inputs=sentence_text_input,
            outputs=sentence_text_output,
        )


demo.launch()
