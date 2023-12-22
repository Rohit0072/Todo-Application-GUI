import PySimpleGUI as sg
from zip_creator import make_archive

lable1 = sg.Text('Select files to compress:')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

lable2 = sg.Text('Select destination compress:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

lable3 = sg.Text('Zip File Name:')
op_file_name = sg.Input(key='op_fn')
compress_button = sg.Button("Compress")

output_lable = sg.Text(key="output_lable", text_color="green")

col1 = sg.Column([[lable1], [lable2], [lable3]])
col2 = sg.Column([[input1], [input2], [op_file_name]])
col3 = sg.Column([[choose_button1], [choose_button2], [compress_button]])

window = sg.Window("Zipper Magic",
                   layout=[[col1, col2, col3],
                           [output_lable]])
while True:
    try:
        event, values = window.read()
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder, values['op_fn'])

        window["output_lable"].update(value="Compression Completed!")
    except AttributeError:
        break
    except TypeError:
        break

window.close()


