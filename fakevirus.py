import time

waiting = 10
print("Your PC will be self-destroyed in 10 seconds. \nDo not try anything for impeaching that, else damages will be increased!!!")

def fake_mining(shares):
	current_share = 0
	count = 0
	while (count < shares):
		current_share = current_share+1
		print("Found share", current_share, "- yay")
		count = count + 1
		time.sleep(10)


time.sleep(waiting)
print("Removing user data...")
time.sleep(10)
print("Done! ")
time.sleep(0.5)

print("Mining bitcoin with your computer (a hack should be profitable!)")
fake_mining(10)
print("finished")

time.sleep(2)

print("\n\n\n")


print("But...\n\n\n")
print("    ____  ")
print("   /----\  ")
print("   |-  -|")
print("   | <> |     ")
print("   \(--)/  <=|D'OH")
print("    |  | \n")
print("All that was a joke! ")
print("This program is only a fake virus made for checking your awareness against real threats. \n\nSorry if you believed that it was real. \n\nKeeping your softwares up to date, not downloading files from random sites (Github is a good source because the source code is public), and not opening strange emails are good ways to avoid getting hacked.")
time.sleep(100)
