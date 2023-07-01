# pip install pyperclip in your cmd console 
# winreg and os used to open during startup

import pyperclip
import winreg
import os

# ---------------- #
# Startup fucntion #
# ---------------- #

# So that this script can run on startup

# Get the path of the current script
script_path = os.path.realpath(__file__)

# Add the script to the run key in the registry
key = winreg.HKEY_CURRENT_USER
key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

# Open the key to edit
open = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

# Set value
winreg.SetValueEx(open, "any_name", 0, winreg.REG_SZ, script_path)

# Close the key
winreg.CloseKey(open)

# -------------- #
# main functions #
# -------------- #

# check if it is twitter link then replace the content

def replace_twitter_link(text):

  if "twitter.com" in text:

    new_text = text.replace("/twitter.com", "/vxtwitter.com")
    return new_text

  else:
      
    return text

#if the link is from twitter

while True:

  clipboard_content = pyperclip.paste()
  modified_content = replace_twitter_link(clipboard_content)
  
  if modified_content != clipboard_content:
    pyperclip.copy(modified_content)
    
