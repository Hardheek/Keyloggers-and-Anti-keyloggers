print('hello')
import getpass

user = getpass.getuser()
# displays the login name of the user This function checks the environment variables LOGNAME, USER, LNAME and
# USERNAME, in order, and returns the value of the first non-empty string // of user/system
print(user)
try:
    x = getpass.getpass(prompt="Enter Password")
except Exception as E:
    print('There is an Error: ', E)
else:
    print(x)

z = getpass.getuser()
pass_word = getpass.getpass("User's password %s: " % z)
print(z, pass_word)