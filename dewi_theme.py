import PySimpleGUI as sg
sg.theme("DarkBlue10")
window = sg.Window(title="Profile Dewi Anida",
                   layout=[[sg.Text("Selamat Belajar PySimpleGUI Dewi")],
                            [sg.Text("NPM       : 2310010692 ")],
                            [sg.Text("Nama      : Dewi Anida ")],
                            [sg.Text("Kelas      : 5B Non Reguler Banjarmasin ")],
                            [sg.Text("Matkul     : Pemrograman Visual 3 ")]
                           ],
                   size=(400,200))
window()
window.close()