import time

waiting = 10
print("Your PC will be self-destroyed in 10 seconds. \nDo not try anything for impeaching that, else damages will be increased !!!")

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
print("Done ! ")
time.sleep(0.5)

print("Mining bitcoin with your computer (a hack should be profitable !)")
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
print("All that was a joke ! ")
print("This program is only a fake virus made for keeping your awareness against real threats. \n\nSorry if you believed that it was real. \n\nKeeping your softwares up to date, avoid downloading files from everywhere (github is a good source because the source code is public), and avoiding to open strange emails are good ways for to lower the risk of seing your computer getting hacked")
time.sleep(100)
