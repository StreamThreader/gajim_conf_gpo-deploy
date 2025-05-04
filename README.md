# gajim_conf_gpo-deploy

Scripts for generate Gajim 1.3.3 user profile settings.

1) gajim-loop-gen.py - for mass generate, read txt file "user_password_list.txt" with user_name:password line by line, then run "gajim-settings-generator.py user password" for generate Settings.sqlite (move to subfolder "gajim-configs\\"+user_name+"\\AppData\\Roaming\\Gajim")

2) gajim-settings-generator.py - generate Settings.sqlite for single user (supply username and password as arguments)

3) gajim-settings-gen_autologon.py - used for run Gajim with user logon (or auto-create config, and then run Gajim)

Requirements:
1) Python 3.8.10 (https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)
2) Nircmd 2.87 (https://www.nirsoft.net/utils/nircmd-x64.zip)

For Windows 2008 R2:
1) install Python 3.8.10 to "c:\Program Files\Python38\"
2) copy nircmd to "C:\Program Files\nircmd\"
3) place script "gajim-settings-gen_autologon.py" to Gajim dir "c:\Program Files\Gajim\"

You can use Microsoft Group Policy to organise autostart
1) Win+R -> gpedit.msc (or use Domain Group Policy Editor)
2) Group Policy Management Editor window, navigate to User Configuration > Policies > Windows Settings > Scripts (Logon/Logoff)
3) Script Name: "c:\Program Files\Python38\python.exe"
4) Script Parameters: "c:\Program Files\Gajim\gajim-settings-gen_autologon.py"
