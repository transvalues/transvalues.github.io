import json
  
# Opening JSON file
f = open('questions.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
socials = 0
socialsc = 0
trus = 0
trusc = 0
hrt = 0
hrtc = 0
lib = 0
libc = 0
x = 0

for i in data['q']:
    if i['effect']['socials'] == 0:
        socialsc += 1
    if i['effect']['trus'] == 0:
        trusc += 1
    if i['effect']['hrt'] == 0:
        hrtc += 1
    if i['effect']['lib'] == 0:
        libc += 1
    socials += i['effect']['socials']
    trus += i['effect']['trus']
    hrt += i['effect']['hrt']
    lib += i['effect']['lib']
    x += 1


print(socials, socialsc)
print(trus, trusc)
print(hrt, hrtc)
print(lib, libc)
print(x)

  
# Closing file
f.close()
