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

window = sg.Window("Zipper Magic",
                   layout=[[lable1, input1, choose_button1],
                           [lable2, input2, choose_button2],
                           [lable3, op_file_name,compress_button],
                           [output_lable]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(op_file_name)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder, values['op_fn'])

    window["output_lable"].update(value="Compression Completed!")

window.close()


