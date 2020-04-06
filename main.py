###########################################################################
#Created By Ahmed Benarab in 2020/03/30 Whene Corana are spreading out !!!#
#-------------------------------------------------------------------------#
#License : the MIT license                                                #
###########################################################################







from tkinter import Tk
import keyboard
import time

class proprint:
    def __init__(self ,sttings,hotkey):
        self.sttings = sttings
        self.hotkey = hotkey
    
    def printos(self):
        clp_data= Tk().clipboard_get()
        list1=clp_data.split('\n')

        for i in range(len(list1)-1) :
            if len(list1[i])==0:
                list1.pop(i)
            else:
                pass
        list1.insert(1, '')
        list1.insert(2, self.sttings)
        for i in list1 :        
            keyboard.write(i)
            keyboard.press_and_release('tab',do_press=True, do_release=True)

    def listner(self):
        keyboard.add_hotkey(self.hotkey, lambda: self.printos())
    

MCQ = proprint('1','ctrl+p')
MCQ.listner()

MonoCQ = proprint('2','ctrl+o')
MonoCQ.listner()

YN = proprint('0','ctrl+i')
YN.listner()
