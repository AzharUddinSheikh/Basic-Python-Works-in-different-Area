import webbrowser

print("deployment completed")

# opening the default brower ie here microsoft internet
webbrowser.open("https://github.com/AzharUddinSheikh")


# it ll use current folder path to locate chrome application
# webbrowser.get(
# using='google-chrome').open("https://github.com/AzharUddinSheikh")

# opening the chrome browser
webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(
    "https://github.com/AzharUddinSheikh")
