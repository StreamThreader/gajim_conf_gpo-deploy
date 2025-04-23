import os
import subprocess

# Version 1.0

generator_script = "gajim-settings-generator.py"
usr_pwd_file_path = "user_password_list.txt"
settings_file = "Settings.sqlite"

# Opening file
usr_pwd_file = open(usr_pwd_file_path, 'r')

# Using for loop
for line in usr_pwd_file:
    line = line.replace("\n", "")
    user_data = line.split(":")
    user_name = user_data[0]
    user_password = user_data[1]

    subprocess.run(["python", generator_script, user_name, user_password])

    user_appdata_path = "gajim-configs\\"+user_name+"\\AppData\\Roaming\\Gajim"

    if not os.path.exists(user_appdata_path):
        os.makedirs(user_appdata_path)
        os.rename(settings_file, user_appdata_path+"\\"+settings_file)

# Closing files
usr_pwd_file.close()
