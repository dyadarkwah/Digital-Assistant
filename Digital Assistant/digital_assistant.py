import wolframalpha
app_id = '536544-TKAA45UJ6R'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)
#res = client.query('temperature in Washington, DC on October 3, 2012')
#print(next(res.results).text)

import wikipedia

import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("Hi I'm Jarvis, ask me anything?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')],]

# Create the window
window = sg.Window('Jarvis', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
try:
    wiki_res = wikipedia.summary(values[0], sentences=2, auto_suggest=False, redirect=True)
    sg.PopupNonBlocking(wiki_res, title="From Wikipedia:")
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(wiki_res)
    engine.runAndWait()
except wikipedia.exceptions.PageError:
    try:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        sg.PopupNonBlocking(wolfram_res, title="From Wolframalpha:")
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(wolfram_res)
        engine.runAndWait()
    except:
        sg.popup("Sorry I don't understand")
except:
    sg.popup("Sorry I don't understand")


#


# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window