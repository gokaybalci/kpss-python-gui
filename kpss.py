import PySimpleGUI
import tkinter as tk
import PySimpleGUI as sg

fnt = 'Arial 13'

sg.theme('DarkAmber')

layout = [  [sg.Text('Genel Yetenek D-Y'), sg.Push(), sg.InputText(size=(5, 30)), sg.InputText(size=(5, 30))],
            [sg.Text('Genel Kültür D-Y'), sg.Push(), sg.InputText(size=(5, 30)), sg.InputText(size=(5, 30))],
            [sg.Text('Eğitim Bilimleri D-Y'), sg.Push(), sg.InputText(size=(5, 30)),  sg.InputText(size=(5, 30))],
            [sg.Text('KPSS: ', key='kpss')],
            [sg.Button('Hesapla'), sg.Button('Kapat')]]

# Create the Window
window = sg.Window('KPSS Puan Hesaplama', layout, font=fnt)
event, values = window.read()


# Genel Yetenek
ssapma_gy = 11.13
hamort_gy = 20.5
# Genel Kültür
ssapma_gk = 8
hamort_gk = 22.01
# Eğitim Bilimleri
ssapma_eg = 14.46
hamort_eg = 37.15

ssapma_ort = 50 # ÖSYM tarafından açıklanmayan ağırlıklı puanların standart sapması


# Genel Yetenek Puan Hesaplama
gy_dogru = values[0]
gy_yanlis = values[1]
gy_ham = float(float(gy_dogru) - (float(gy_yanlis) / 4))
standart_gy = ((gy_ham - hamort_gy) / ssapma_gy) * 10 + 50

# Genel Kültür Puan Hesaplama
gk_dogru = values[2]
gk_yanlis = values[3]
gk_ham = float(float(gk_dogru) - (float(gk_yanlis) / 4))
standart_gk = ((gk_ham - hamort_gk) // ssapma_gk) * 10 + 50

# Eğitim Bilimleri
eg_dogru = values[4]
eg_yanlis = values[5]
eg_ham = float(float(eg_dogru) - (float(eg_yanlis) / 4))
standart_eg = ((eg_ham - hamort_eg) // ssapma_eg) * 10 + 50


# Ağırlıklı Standart Puan (Eğitim)
asp_eg = (standart_gy * .3) + (standart_gk * .3) + (standart_eg * .4)


kpss_total = 70 + ((30 * (2 * (asp_eg - ssapma_ort) - 9.525) // (2 * 86.15 - ssapma_ort) - 9.525))



while True:
    event, values = window.read()
    if event == 'Hesapla':
        window['kpss'].update('KPSS: ' + str(kpss_total))
    elif event == sg.WIN_CLOSED or event == 'Kapat':
        break
window.close()