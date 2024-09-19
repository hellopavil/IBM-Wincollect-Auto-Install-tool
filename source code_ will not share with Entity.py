import xml.etree.ElementTree as ET
import os

print ("                  Windows Onboarding Tool 28-02-2023_PJ1.1\n")
# make sure syslog ip is not updated
valuenotset = 0
tree = ET.parse("update_option_wec.xml")
root = tree.getroot()
os.system('cmd /c "mkdir \"C:\\Program Files\\IBM\\WinCollect\\xml_files\\" >nul"')
# Find the Parameter element with name="Address" and replace the value
for param_elem in root.findall('.//Parameter[@name="Address"]'):
    if param_elem.get('value') == 'SYSLOGIP':
        valuenotset = 1

if valuenotset == 1:
 syslogipvalue = input('\nPlease Enter SYSLOG IP ->')

# First file
 tree = ET.parse(r"update_option_wec.xml")
 root = tree.getroot()

 # Find the Parameter element with name="Address" and replace the value
 for param_elem in root.findall('.//Parameter[@name="Address"]'):
    if param_elem.get('value') == 'SYSLOGIP':
        param_elem.set('value', syslogipvalue)
 
 tree.write(r"update_option_wec.xml")
# Second file
 tree = ET.parse(r"update_option_nonad.xml")
 root = tree.getroot()

 # Find the Parameter element with name="Address" and replace the value
 for param_elem in root.findall('.//Parameter[@name="Address"]'):
    if param_elem.get('value') == 'SYSLOGIP':
        param_elem.set('value', syslogipvalue)

 # Write the modified XML back to a file
 tree.write(r"update_option_nonad.xml")

 # third file
 tree = ET.parse(r"update_option_iis.xml")
 root = tree.getroot()

 # Find the Parameter element with name="Address" and replace the value
 for param_elem in root.findall('.//Parameter[@name="Address"]'):
    if param_elem.get('value') == 'SYSLOGIP':
        param_elem.set('value', syslogipvalue)

 # Write the modified XML back to a file
 tree.write(r"update_option_iis.xml")
 # fourth file
 tree = ET.parse(r"update_option_dhcp.xml")
 root = tree.getroot()

 # Find the Parameter element with name="Address" and replace the value
 for param_elem in root.findall('.//Parameter[@name="Address"]'):
    if param_elem.get('value') == 'SYSLOGIP':
        param_elem.set('value', syslogipvalue)

 # Write the modified XML back to a file
 tree.write(r"update_option_dhcp.xml")
 # fiveth file
 tree = ET.parse(r"update_option_ex.xml")
 root = tree.getroot()

 # Find the Parameter element with name="Address" and replace the value
 for param_elem in root.findall('.//Parameter[@name="Address"]'):
    if param_elem.get('value') == 'SYSLOGIP':
        param_elem.set('value', syslogipvalue)

 # Write the modified XML back to a file
 tree.write(r"update_option_ex.xml")

os.system('cmd /c "copy /y *.xml \"C:\\Program Files\\IBM\WinCollect\\xml_files\\" >nul"')

print ("\n1 Installing Wincollect in Domain based WEC Server")
print ("2 Configuring WEC server")
print ("3 Wincollect installation in Non-Domain Server")
print ("4 Wincollect installation in IIS Servers")
print ("5 Wincollect installation in DHCP Servers")
print ("6 Wincollect installation in Exchange Servers")
print ("7 Wincollect Upgrade")
print ("8 Information Gathering\n")


while True:
 pavil_input = input("\n<<Please Enter your selection (1 to 8)-> ")
 try:
    num = int(pavil_input)
 except ValueError:
        print("\n<<Please enter the correct option>>\n")
        continue


 if num == 1:
    print("\n<<Installing Wincollect in WEC Server>>\n")
    os.system('cmd /c "msiexec.exe /l*v WC_install.log /qb /i wincollect_install.msi INSTALLDIR=\"C:\\Program Files\\IBM\WinCollect\\" WC_SCRIPT=\"C:\\Program Files\\IBM\WinCollect\\xml_files\\update_option_wec.xml""')
    print("\n<<Installation of Wincollect in WEC Server completed>>\n")
    
 elif num == 2:
    print("\n<<Configuring WEC Server>>\n")
    os.system('cmd /c "netsh http delete urlacl url=http://+:5985/wsman/"')
    os.system('cmd /c "netsh http add urlacl url=http://+:5985/wsman/ sddl=D:(A;;GX;;;S-1-5-80-569256582-2953403351-2909559716-1301513147-412116970)(A;;GX;;;S-1-5-80-4059739203-877974739-1245631912-527174227-2996563517)"') 
    os.system('cmd /c "netsh http delete urlacl url=https://+:5986/wsman/"') 
    os.system('cmd /c "netsh http add urlacl url=https://+:5986/wsman/ sddl=D:(A;;GX;;;S-1-5-80-569256582-2953403351-2909559716-1301513147-412116970)(A;;GX;;;S-1-5-80-4059739203-877974739-1245631912-527174227-2996563517)"')
    os.system('cmd /c "powershell.exe -Command "Enable-PSRemoting""')
    os.system('cmd /c "wevtutil gl security"')
    print("\n<<WEC server is now ready. Please create the Subcription in Event viewer>>\n")
    os.system('cmd /c "eventvwr"')
    
 elif num == 3:
    print("\n<<Installing Wincollect in Non-Domain Server>>\n")
    os.system('cmd /c "msiexec.exe /l*v WC_install.log /qb /i  wincollect_install.msi INSTALLDIR=\"C:\\Program Files\\IBM\WinCollect\\" WC_SCRIPT=\"C:\\Program Files\\IBM\WinCollect\\xml_files\\update_option_nonad.xml""')
    print("\n<<Installation of Wncollect in Non-Domain Server completed>>\n")
    
 elif num == 4:
    print("\n<<Installing Wincollect in IIS Servers>>\n")
    os.system('cmd /c "msiexec.exe /l*v WC_install.log /qb /i  wincollect_install.msi INSTALLDIR=\"C:\\Program Files\\IBM\WinCollect\\" WC_SCRIPT=\"C:\\Program Files\\IBM\WinCollect\\xml_files\\update_option_iis.xml""')
    print("\n<<Installation of Wincollect in IIS Servers completed")
    
 elif num == 5:
    print("\n<<Installing Wincollect in DHCP Servers>>\n")
    os.system('cmd /c "msiexec.exe /l*v WC_install.log /qb /i wincollect_install.msi INSTALLDIR=\"C:\\Program Files\\IBM\WinCollect\\" WC_SCRIPT=\"C:\\Program Files\\IBM\WinCollect\\xml_files\\update_option_dhcp.xml""')
    print("\n<<Installation of Wincollect in DHCP Servers completed>>\n")
    
 elif num == 6:
    print("\n<<Installing Wincollect in Exchange Servers>>\n")
    os.system('cmd /c "msiexec.exe /l*v WC_install.log /qb /i wincollect_install.msi INSTALLDIR=\"C:\\Program Files\\IBM\WinCollect\\" WC_SCRIPT=\"C:\\Program Files\\IBM\WinCollect\\xml_files\\update_option_ex.xml""')
    print("\n<<Installation of wincollect in Exchange Servers completed>>\n")
    
 elif num == 7:
    print("\n<<Wincollect Agent will now upgrade>>\n")
    os.system('cmd /c "msiexec.exe /qn /i wincollect_upgrade.msi"')
    print("\n<<Upgrade Completed>>")
    
 elif num == 8:
    print("<<Hostname name>>\n")
    os.system('cmd /c "hostname"')
    print("\n\n<<Server IP details>>\n")  
    os.system('cmd /c "ipconfig"')
    
 else:
    print("Please enter correct option")
    continue

os.system('cmd /c "pause"')
