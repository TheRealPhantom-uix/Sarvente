import os
print('Setting up sarvente. Please wait...')

def cls():
	try:
		os.system('cls')
	except:
		os.system('clear')

open('data/mode.txt', 'w').write('')
open('data/status.txt', 'w').write('')
open('data/token.txt', 'w').write('')
open('data/output.txt', 'w').write('')
cls()

import requests
import pyautogui as pag
import time
import dhooks

version = 'v1.2'



def main():
	cls()
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
6 - Spam tool
7 - Get bot server list
\n''')
	mode = input()
	if(mode == '1'):
		cls()
		print('Selected crash discord server.')
		time.sleep(3)
		cls()
		token = input('Enter discord bot token: ')
		cls()
		print('Saving...')
		token_file = open('data/token.txt', 'w')
		token_file.write(token)
		token_file.close()
		time.sleep(1)
		print('Saved!')
		time.sleep(2)
		cls()
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
		cls()
		print('Selected webhook sender.')
		time.sleep(3)
		cls()
		url = input('Enter webhook url: ')
		cls()
		print('Connecting to the webhook...')
		try:
			hook = dhooks.Webhook(url)
		except:
			input('Incorrect webhook url. Press ENTER to quit.')
			main()
		print('Connected!')
		while True:
			cls()
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
		cls()
		print('Selected give administrative role.')
		time.sleep(3)
		cls()
		owner_id = input('Enter your id: ')
		token = input('Enter discord bot token: ')
		cls()
		print('Saving...')
		token_file = open('data/token.txt', 'w')
		token_file.write(token)
		token_file.close()
		time.sleep(1)
		print('Saved!')
		time.sleep(2)
		cls()
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
		open('data/output.txt', 'w').write('')
		while open('data/status.txt', 'r').read() != 'connected':
			pass
		print('Connected.')
		print('If bot has permission ADMINISTRATOR, created role sarvente and gived to your id.')
		input('Press ENTER to quit.')
		os.system('taskkill /f /im cmd.exe')
		main()
	if mode == '4':
		cls()
		print('Selected dox generator.')
		time.sleep(3)
		cls()
		nickname1 = input("Enter victim's nickname: ")
		cls()
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
		cls()
		print('Selected telegram bot sender.')
		time.sleep(3)
		token = input('Enter telegram bot token: ')
		url = f'https://api.telegram.org/bot{token}/'
		cls()
		print('Setting up sender:')
		username = input('1. Enter your username: ')
		cls()
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
		cls()
		print(f'Message received!\n\nSender configured:\nChat ID: {chatid}')
		time.sleep(2)
		while True:
			cls()
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
		cls()
		print('Selected spam tool.')
		time.sleep(3)
		cls()
		print('Sarvente - Spam Tool')
		print('----------------------------')
		interval = float(input('Enter interval: '))
		message = input('Enter message: ')
		pag.FAILSAFE = True
		cls()
		print('To stop, move the mouse pointer over the upper right corner of the screen.')
		input('Press ENTER to start.')
		cls()
		print('Stating in 5')
		time.sleep(1)
		cls()
		print('Stating in 4')
		time.sleep(1)
		cls()
		print('Stating in 3')
		time.sleep(1)
		cls()
		print('Stating in 2')
		time.sleep(1)
		cls()
		print('Stating in 1')
		time.sleep(1)
		cls()
		print('Spamming!')
		while True:
			try:
				time.sleep(interval)
				pag.typewrite(message)
				pag.press('enter')
			except:
				break
	if mode == '7':
		cls()
		print('Selected bot server list.')
		time.sleep(3)
		cls()
		token = input('Enter token: ')
		with open('data/token.txt', 'w') as f:
			f.write(token)
			f.close()
		cls()
		print('Summoning bot module..')
		with open('data/mode.txt', 'w') as f:
			f.write('serverlist')
			f.close()
		cls()
		print('Waiting for connect. Print "!connect" to connect.')
		os.system('cd data&python bot.py')
		cls()
		os.system('cd data&type output.txt')
		with open('data/output.txt', 'w') as f:
			f.write('')
			f.close()
		input('\nPress ENTER to quit.')
		main()

	main()

main()