from functions_ep.import_ import *


def main():
    vaccine = pd.read_csv("vaccinations_4.csv")
    vaccine.date = pd.to_datetime(vaccine.date)
    epidemic_file = pd.read_csv("./new_table_epidemic.csv")
    epidemic_file.date = pd.to_datetime(epidemic_file.date)
    set_with_countries = get_list_of_countries(epidemic_file)
    mpl.rcParams['font.size'] = 7
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.figsize'] = [8, 6]

    theme = "DarkTeal4"
    sg.theme(theme)

    print("Current theme is", theme)

    dict_with_functions = {"New infected": ps.plot_country_confirmed_stats,
                           "New deceased": ps.plot_country_deceased_stats,
                           "infected absolute growth": ps.absolute_growth,
                           "Infected rate growth": ps.rate_growth,
                           'Deceased absolute growth': ps.deceased_absolute_growth,
                           'Deceased rate growth': ps.deceased_rate_growth,
                           'Vaccinated stats': ps.plot_vaccine_stats,
                           'Wave length': ps.waves,
                           'Anxiety': ps.plot_anxiety,
                           'Depression': ps.plot_depression,
                           }
    layout = [[sg.Text('Choose a plot', size=(15, 1)),
         sg.InputCombo(list(dict_with_functions.keys()), key="plot"), sg.Button("Confirm", key="confirm", use_ttk_buttons=True)],
        [sg.Text('Please enter two dates in the format     dd.mm.yy')],
        [sg.Text('Date 1', size=(15, 1)), sg.InputText(key='date_1', default_text="01.01.20"),
         sg.CalendarButton('Choose Date', target="date_1", format="%d.%m.%y", key='--date1--')],
        [sg.Text('Date 2', size=(15, 1)), sg.InputText(key="date_2", default_text="30.08.22"),
         sg.CalendarButton('Choose Date', target="date_2", format="%d.%m.%y", key='--date2--')],
        [sg.Text('Country', size=(15, 1)), sg.InputCombo(set_with_countries, key="country")],

        [sg.Text('Plot folder', size=(15, 1)), sg.InputText("", key='-dest-'),
         sg.FolderBrowse(key="Browse", target='-dest-')],
        [sg.Button('Ok', use_ttk_buttons=True), sg.Button('Exit', use_ttk_buttons=True)],
        [sg.Button('Clear all cells', use_ttk_buttons=True)]]

    window = sg.Window('Epidemic', layout, font="Minecraft 15", resizable=True, finalize=True, icon="skull.png", ttk_theme="alt")
    while True:
        event, values = window.read()
        print(event)
        if event == "Clear all cells":
            window['date_1'].update("")
            window['date_2'].update("")
            window['country'].update("")
            window['plot'].update("")
            window['-dest-'].update("")
            for i in ['date_1', 'date_2', 'country', 'plot', '--date1--', '--date2--']:
                window[i].update(disabled=False)
        elif event == "confirm":
            if values['plot'] == "Depression" or values['plot'] == "Anxiety":
                for i in ['date_1', 'date_2', 'country', '--date1--', '--date2--']:
                    window[i].update(disabled=True)
                window['country'].update(value='USA')
            else:
                for i in ['date_1', 'date_2', 'country', 'plot', '--date1--', '--date2--']:
                    window[i].update(disabled=False)
        elif event in (None, 'Exit'):
            break
        elif event == 'Ok':
            if values["plot"] != 'Anxiety' and values['plot'] != 'Depression':
                    if values['country'] == "" or values['plot'] == "" or values['Browse'] == "" or values['date_1'] == "" or values['date_2'] == "":
                        sg.popup("Please fill all fields", title="Error", auto_close=True, auto_close_duration=10)
                        continue
            else:
                if values['Browse'] == "":
                    sg.popup("Please fill the destination field", title="Error", auto_close=True, auto_close_duration=10)
                    continue
            date_1 = values['date_1']
            date_2 = values['date_2']
            country = values['country']
            plot = values['plot']
            path_to_plot = values["-dest-"]
            try:
                date_1 = pd.to_datetime(date_1, format="%d.%m.%y")

            except ValueError:
                sg.popup("Wrong date format date1")
                continue
            try:
                date_2 = pd.to_datetime(date_2, format="%d.%m.%y")
            except ValueError:
                sg.popup("Wrong date format date2")
                continue
            if date_2 < date_1:
                date_1, date_2 = date_2, date_1

            if plot == "Vaccinated stats":
                path_to_plot += "/" + country
                if not os.path.exists(path_to_plot):
                    os.mkdir(path_to_plot, mode=0o777, dir_fd=None)
                dict_with_functions[plot](country, date_1, date_2, vaccine, path_to_plot)

            elif plot == "Anxiety" or plot == 'Depression':
                path_to_plot += "/" + "anxiety_depression_stats"
                if not os.path.exists(path_to_plot):
                    os.mkdir(path_to_plot, mode=0o777, dir_fd=None)
                dict_with_functions[plot](path_to_plot)

            else:
                path_to_plot += "/" + country
                if not os.path.exists(path_to_plot):
                    os.mkdir(path_to_plot, mode=0o777, dir_fd=None)
                dict_with_functions[plot](country, date_1, date_2, epidemic_file, path_to_plot)
            sg.popup("Plot saved")
            plt.close()
    window.close()
    print("Program finished")


if __name__ == "__main__":
    main()
