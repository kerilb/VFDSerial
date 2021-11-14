import vfd
from time import sleep, ctime

d = vfd.BA63("COM1")

d.reset()
d.write("Wincor Nixdorf" + "\r\n", 1, 4)

d.scroll("", line=2, step_delay=0.2)

while 1:
    sleep(0.1)
    # d.scroll_update(2, ctime()[0:-4])
    d.scroll_update(2, "Тест дисплея Wincor Nixdorf BA63-1 RS-232")


