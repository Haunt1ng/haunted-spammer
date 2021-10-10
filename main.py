import requests
import time
import os
logo = "HAUNTED SPAMMER\nA Haunting Webhook Spammer\n\n\n"""
print(logo)
content = input("What do you want to spam?:  ")
username = input("username?: ")
num = input("times spammed?: ")
delay = input("Delay?: ")
webhook = input("Webhook url: ")
data = {
	"content" : content,
   	"username" : username,
    "avatar_url" : "https://media.discordapp.net/attachments/808273939629473796/872240739067756544/blank.png"
	}
for x in range(int(num)):
    requests.post(webhook, json = data)
    print("[+1]")
    time.sleep(float(delay))
print('Job completed, exiting in 10 seconds')
time.sleep(10)
os.system('exit')