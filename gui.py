import tkinter 

window_main = tkinter.Tk(className='Bluetooth light', )
window_main.geometry("400x200")
 
def submitFunction() :
    print('Submit button is clicked.')
 
button_submit = tkinter.Button(window_main, text ="Toggle", command=submitFunction)
button_submit.config(width=20, height=2)
 
button_submit.grid() 

window_main.mainloop()