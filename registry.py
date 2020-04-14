import winreg as wreg

# Set executable to registry 
destination = 'C:\\Windows\\System32\\calc.exe'

key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
wreg.SetValueEx(key, 'Calc', 0, wreg.REG_SZ, destination)
key.Close()
