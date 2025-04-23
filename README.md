# gajim_conf_gpo-deploy

Scripts for generate Gajim 1.3.3 user profile settings.

1) gajim-loop-gen.py - read txt file "user_password_list.txt" with user_name:password line by line, then run "gajim-settings-generator.py user password" for generate Settings.sqlite (move to subfolder "gajim-configs\\"+user_name+"\\AppData\\Roaming\\Gajim")

2) gajim-settings-generator.py - generate Settings.sqlite for single user (supply username and password as arguments)

3) gajim-settings-gen_autologon.py - used for run Gajim with user logon (or auto-create config, and then run Gajim)

You can use Microsoft Group Policy to organise autostart:
For Windows 2008 R2, install Python 3.8.10 (path c:\Program Files\Python38\)
Place script "gajim-settings-gen_autologon.py" to Gajim dir "c:\Program Files\Gajim\"

1) Win+R -> gpedit.msc (or use Domain Group Policy Editor)
2) Group Policy Management Editor window, navigate to Computer Configuration > Policies > Windows Settings > Scripts -> Startup
3) Script Name: "c:\Program Files\Python38\python.exe"
4) Script Parameters: "c:\Program Files\Gajim\gajim-settings-gen_autologon.py"
