import matplotlib.pyplot as plt
import glob
import PySimpleGUI as sg
import matplotlib
import re
import pandas as pd

sg.theme("DarkTeal1")
layout = [[sg.T("")],
          #this part is if you want it to add a file option
          #[sg.Text("Choose a file :     "), sg.Input(), sg.FileBrowse(key="-IN1-")],
          [sg.Text("This software will go through every file in the folder and plot all the values on excel!")],
          [sg.Text("Choose a folder : "), sg.Input(key="-IN2-", change_submits=True), sg.FolderBrowse(key="-IN-")],
          [sg.Button("Submit")]]
###Building Window
window = sg.Window('My File Browser', layout, size=(600, 150))
import pandas as pd


def chooseFolder():
    while True:
        event, values = window.read()
        print(values["-IN2-"])
       # print(values["-IN1-"])
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Submit":
            readFiles(values["-IN-"])


def readFiles(folder):
    #opens folder and stores a list of every file in that folder in this files array
    files = glob.glob(folder+'\*')
    for file in files:
            #open every file and read it
            with open(file,'r') as fd:
                print("File being plotted: "+file)
                df = pd.read_table(file)
                df.to_excel('output.xlsx', 'Sheet1')
                #values stores every line in the file in an array
                everythingInFile=fd.read()
                everyLine=fd.read().splitlines()
                plotData(everyLine)



def plotData(data):
    #print(data)
    data=1


if __name__ == '__main__':
    chooseFolder()
