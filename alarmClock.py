# importing whole module
from tkinter import *
from tkinter.ttk import *
from threading import *
import datetime
import time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Alarm Clock')

# Set geometry
root.geometry("400x300")

# display time on the label
def Atime():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, Atime)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
			background = 'white',
			foreground = 'black',)

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
Atime()

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()
def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound
			#winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
Label(root,text="Set Time").pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm",command=Threading).pack(pady=20)
def Exit():
	exit(0)
Button(root, text="EXIT",command=Exit).pack(pady=10)




mainloop()