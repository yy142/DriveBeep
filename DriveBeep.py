from microbit import *

while True:
	accele_x = accelermeter.get_x()
	accele_y = accelermeter.get_y()
	accele_z = accelermeter.get_z()
	touch_0 = pin0.is_touched()
	touch_1 = pin1.is_touched()
	touch_2 = pin2.is_touched()
	if touch_0:
		display.show(Image.HAPPY)
	else:
		display.show(Image.SAD)
	sleep(100)