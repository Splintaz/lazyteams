# Lazy Teams
Automatically join a Teams-meeting with a muted microphone and camera. Supports organization login. 

# What is Lazy Teams?
It uses Selenium and Chrome to open up a web browser and automatically login for you where it will then wait for a call prompt. Upon the call prompt being shown, it will be accepted and the saved profile will avoid any browser notifications from showing up by blocking the microphone and camera. 

# Instructions
1. First, you will have to install dependencies. 
  - Terminal: pip install selenium
  - Python: https://www.python.org/
  - Chrome: https://www.google.com/chrome/
  - Chromedriver: https://chromedriver.chromium.org/downloads
2. Change the hardcoded username and password in the file.
3. Release the Python!

For normal teams users, use "teams.py". 
For organization users, use "org.py".
