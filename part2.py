import urllib.request
def calc (operator,a,b):
    if operator == 'x':
        print(a*b)
    elif operator =='+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '/':
        print(a / b)
    else :
        print("Invalid operator")

url = "https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt"
file = urllib.request.urlopen(url)
for line in file:
	
    #splited =file.read().splitlines()
    oneLine = line.splitlines()
   # spl = line.split()
print(oneLine)
