import os
import sys
import subprocess
import sqlite3

# Version 1.0
# for Gajim 1.3.3

host_name = "jabber.example.org"
resource_name = "onTerminalServer"
user_name = os.environ['USERNAME']
app_data = os.environ['APPDATA']
conf_file = app_data+"\Gajim\Settings.sqlite"
gajim_exe = "C:\\Program Files\\Gajim\\bin\\Gajim.exe"
user_password = ""


def check_if_need_run():
    if os.path.isfile(conf_file):
        proc = subprocess.Popen([gajim_exe], shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
        exit(0)

# if Settings file exist
# skip, and just run Gajim
check_if_need_run()

connection = sqlite3.connect(conf_file)
cursor = connection.cursor()

# add table "account_settings"
cursor.execute('''
CREATE TABLE settings (
    name TEXT UNIQUE,
    settings TEXT
)
''')

# add table "settings"
cursor.execute('''
CREATE TABLE account_settings (
    account TEXT UNIQUE,
    settings TEXT
)
''')

# account settings
account_settings = (
    '{'+
    '"account": {'+
        '"active": true, '+
        '"name": "'+user_name+'", '+
        '"resource": "'+resource_name+'", '+
        '"account_label": "'+user_name+'@'+host_name+'", '+
        '"account_color": "rgb(182,0,115)", '+
        '"hostname": "'+host_name+'", '+
        '"savepass": true, '+
        '"anonymous_auth": false, '+
        '"autoconnect": true, '+
        '"sync_with_global_status": true, '+
        '"use_custom_host": false, '+
        '"password": "'+user_password+'", '+
        '"last_status": "online", '+
        '"last_status_msg": "", '+
        '"roster_version": "", '+
        '"opened_chat_controls": ""}, '+
    '"contact": {}, '+
    '"group_chat": {}'+
    '}'
)

sql_account_settings = '''INSERT INTO account_settings
    (account, settings)
    VALUES (?, ?)'''
cursor.execute(sql_account_settings, (host_name, account_settings))

# create app settings
json_app_settings = (
    '{'+
    '"emoticons_theme": "noto", '+
    '"one_message_window": "always_with_roster", '+
    '"positive_184_ack": true, '+
    '"show_send_message_button": true, '+
    '"print_status_in_chats": true, '+
    '"sort_by_show_in_muc": true, '+
    '"sounds_on": false, '+
    '"autopopup": true, '+
    '"check_for_update": false, '+
    '"last_update_check": "2025-04-19 22:56", '+
    '"roster_x-position": 0, '+
    '"roster_y-position": 0, '+
    '"roster_width": 700, '+
    '"roster_height": 440, '+
    '"last_roster_visible": true, '+
    '"collapsed_rows": "", '+
    '"roster_hpaned_position": 200, '+
    '"msgwin-max-state": false, '+
    '"msgwin-width": 500, '+
    '"msgwin-height": 440, '+
    '"msgwin-x-position": 0, '+
    '"msgwin-y-position": 0, '+
    '"use_keyring": false'+
    '}'
)

sql_insert_settings = '''INSERT INTO settings
    (name, settings)
    VALUES (?, ?)'''

cursor.execute(sql_insert_settings, ("app", json_app_settings))

# sound settings
cursor.execute("INSERT INTO settings(name, settings) VALUES ('soundevents', '{}')")

# status presets (RU)
status_preset = (
    '{'+
    '"\u0421\u043f\u043b\u044e": {'+
        '"message": "ZZZZzzzzzZZZZZ",'+
        '"activity": "inactive",'+
        '"subactivity": "sleeping",'+
        '"mood": "sleepy"'+
    '},'+
    '"\u0421\u043a\u043e\u0440\u043e \u0431\u0443\u0434\u0443": {'+
        '"message": "\u0412\u0435\u0440\u043d\u0443\u0441\u044c \u0447\u0435\u0440\u0435\u0437 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043c\u0438\u043d\u0443\u0442."'+
    '},'+
    '"\u0415\u043c": {'+
        '"message": "\u042f \u043a\u0443\u0448\u0430\u044e.",'+
        '"activity": "eating",'+
        '"subactivity": "other"'+
    '}, '+
    '"\u0412 \u043a\u0438\u043d\u043e": {'+
        '"message": "\u042f \u0441\u043c\u043e\u0442\u0440\u044e \u0444\u0438\u043b\u044c\u043c.", '+
        '"activity": "relaxing", '+
        '"subactivity": "watching_a_movie"'+
    '}, '+
    '"\u0420\u0430\u0431\u043e\u0442\u0430\u044e": {"'+
        'message": "\u042f \u0440\u0430\u0431\u043e\u0442\u0430\u044e.", '+
        '"activity": "working", '+
        '"subactivity": "other"'+
    '}, '+
    '"\u0412\u044b\u0448\u0435\u043b": {'+
        '"message": "\u042f \u043d\u0430\u0441\u043b\u0430\u0436\u0434\u0430\u044e\u0441\u044c \u0436\u0438\u0437\u043d\u044c\u044e.", '+
        '"activity": "relaxing", '+
        '"subactivity": "going_out"'+
    '}'+
    '}'
)

cursor.execute(sql_insert_settings, ("status_presets", status_preset))

# proxy settings
proxy_str = '{"Tor": {"type": "socks5", "host": "localhost", "port": 9050}}'
cursor.execute(sql_insert_settings, ("proxies", proxy_str))

# plugin settings
plugin_str = '{"omemo": {"active": true}, "plugin_installer": {"active": true}, "url_image_preview": {"active": true}}'
cursor.execute(sql_insert_settings, ("plugins", plugin_str))

connection.commit()
connection.close()

# after all, run Gajim
check_if_need_run()
