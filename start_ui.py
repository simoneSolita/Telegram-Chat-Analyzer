import gradio as gr
from constants.constant import PROPERTIES_FILE_JSON_NAME
from manager.file_manager import scan_db, validate_input_file
from manager.properties_manager import write_property, open_properties_file
from manager.ui_manager import search_sentence_db, search_user_db, search_sentence_by_user_db


def ui_function_search_user(user_input):
    return search_user_db(user_input)


def ui_function_search_sentence(user_input):
    return search_sentence_db(user_input)


def ui_function_search_sentence_by_user(user_input):
    return search_sentence_by_user_db(user_input)


def refresh_db_list():
    return scan_db()


def create_new_db_dropdown():
    return gr.Dropdown(choices=refresh_db_list())


def set_db(db_name):
    write_property(PROPERTIES_FILE_JSON_NAME, db_name)


def validate_json(file):
    print(validate_input_file(file))


with gr.Blocks() as demo:
    gr.Markdown("Connect to a DB")
    with gr.Tab("DB List") as tab_scan_db:
        with gr.Row() as dbs_row:
            dropdown = gr.Dropdown([], label="Chats", info="Select a chat to Query")
            dropdown.change(
                fn=lambda _: gr.Dropdown.update(choices=refresh_db_list()),
                inputs=[dropdown],
                outputs=[dropdown],
            )
            scan_db_text_button = gr.Button("🔄 Scan For DB")
            scan_db_text_button.click(create_new_db_dropdown, [], [dropdown])
        with gr.Row() as btn_row:
            select_db_text_button = gr.Button("Select DB")
            select_db_text_button.click(set_db, [dropdown], [])
    with gr.Tab("Create a DB") as tab_create_db:
        area_json_upload = gr.File(label="Select a JSON", file_types=[".json"])
        json_uploaded_button = gr.Button("Upload JSON")
        json_uploaded_button.click(validate_json, [area_json_upload], [])

    with gr.Column() as query_col:
        gr.Markdown("Insert Info to search")
        with gr.Tab("Sentence By User") as sentence_by_user_tab:
            sentence_by_user_text_input = gr.Textbox(label="Filter (or nothing for every User)")
            sentence_by_user_df_output = gr.DataFrame()
            sentence_by_user_text_button = gr.Button("Search Sentence")
        with gr.Tab("Users") as user_tab:
            user_text_input = gr.Textbox(label="Filter (or nothing for every User)")
            user_df_output = gr.DataFrame()
            user_text_button = gr.Button("Search User")
        with gr.Tab("Sentence") as sentence_tab:
            sentence_text_input = gr.Textbox(label="Filter (or nothing for every Sentence)")
            sentence_df_output = gr.DataFrame()
            sentence_text_button = gr.Button("Search Sentence")

        user_text_button.click(
            ui_function_search_user,
            inputs=user_text_input,
            outputs=user_df_output
        )
        sentence_text_button.click(
            ui_function_search_sentence,
            inputs=sentence_text_input,
            outputs=sentence_df_output,
        )
        sentence_by_user_text_button.click(
            ui_function_search_sentence_by_user,
            inputs=sentence_by_user_text_input,
            outputs=sentence_by_user_df_output,
        )

demo.launch()
