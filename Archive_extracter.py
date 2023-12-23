import PySimpleGUI as sg
from arc_ext_function import extract_archive

sg.theme("LightTeal")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select Destination:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_lable = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_lable]])

while True:
    try:
        event, value = window.read()
        archivepath = value['archive']
        dest_dir = value['folder']
        extract_archive(archivepath, dest_dir)
        window['output'].update(value="Extraction Completed")
    except AttributeError:
        break
    except TypeError:
        break

window.close()
