import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#F0FFFF")
window = sg.Window(title="Profile Dewi Anida",
                   layout=[[sg.Text("Selamat Belajar PySimpleGUI Dewi")],
                            [sg.Text("NPM       : 2310010692 ")],
                            [sg.Text("Nama      : Dewi Anida ")],
                            [sg.Text("Kelas      : 5B Non Reguler Banjarmasin ")],
                            [sg.Text("Matkul    : Pemrograman Visual 3 ")]
                           ],
                   size=(400,200),
                   font=("Times", 18))
window()
window.close()