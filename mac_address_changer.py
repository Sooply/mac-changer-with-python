import subprocess
import optparse
import re

def Arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface where you want to change your mac address")
    parser.add_option("-m", "--mac", dest="mac_address", help="The mac address you want to change")

    (options, args) = parser.parse_args()

    if not options.interface:
        print("(!) Please enter an interface, for more information: --help")
    elif not options.mac_address:
        print("(!) Please enter an mac address, for more information: --help")
    return options

def macChanger(interface, mac_address):
    print("(!) Changing mac address for", interface, "to", mac_address)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def currentMac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
    if search_result:
        return search_result.group(0)
    else:
        return None

options = Arguments()
macChanger(options.interface, options.mac_address)

current_mac = currentMac(options.interface).decode()
if current_mac == options.mac_address:
    print("(!) Mac address has changed successfully.")
else:
    print("(!) Failed, couldn't change mac address.")
