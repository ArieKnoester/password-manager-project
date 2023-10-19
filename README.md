# password-manager-project

### Disclaimer
This application was made for learning purposes only and **NOT** 
intended for use. Use at your own risk. Passwords are stored in 
data.json as _plain text_. I am not responsible for any issues, 
security or otherwise, from the use of this application.

### Description
A basic password management application created as part of a Python
course. The image, logo.png, was provided by the course. Credentials
added by the user are stored in a local json file. 

- A default Username/Email can be added by assigning it to the 
constant, DEFAULT_USERNAME, in app.py.
- Clicking the 'Generate Password' button will also copy the
password to your clipboard via the Pyperclip module 
(https://pypi.org/project/pyperclip/)
- Users can now search for stored website credentials via the 
'Search' button.

#### Possible short-term improvements
- Clean up App class methods. Break them up to be more discrete.
- When adding credentials, check if it already exists. Give the
user an option to overwrite.
- Add button to set the default 'Username/Email' entry and have
it persist upon next use.

#### Possible long-term improvements
- Implement some form of password encryption/decryption.
- Replace file storage with something else.



