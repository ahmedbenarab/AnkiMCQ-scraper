from tkinter import Tk
import keyboard
import time
def printos():
    #time.sleep(0.25)
    clp_data= Tk().clipboard_get()
    list1=clp_data.split('\n')

    for i in range(len(list1)-1) :
        if len(list1[i])==0:
            list1.pop(i)
        else:
            pass
    list1.insert(1, '')
    list1.insert(2, '2')
    for i in list1 :        
        keyboard.write(i)
        keyboard.press_and_release('tab',do_press=True, do_release=True)
    end()
keyboard.add_hotkey('ctrl+p', lambda: printos())