import os
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# os.system("taskkill /im Spotify.exe")

# # timer = threading.Timer(5.0, print("Hello World!"))
# # timer.start()

# time.sleep(1)
# os.startfile("C:/Users/Vlad/AppData/Roaming/Spotify/Spotify.exe")
# os.system("tasklist")


if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_modified(event):
	print(f"hey buddy, {'C:/Users/Vlad/AppData/Local/Spotify/Browser/Network Persistent State'} has been modified")

my_event_handler.on_modified = on_modified

path = "C:/Users/Vlad/AppData/Local/Spotify/Browser/Network Persistent State"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()