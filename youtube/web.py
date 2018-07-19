
import webbrowser
print('====================================')
print('Enter youtube video url for download') 
print('====================================')

url  = raw_input()
index = url[:12]+'ss'+url[12:]
webbrowser.open(index)
