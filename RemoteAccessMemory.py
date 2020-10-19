import re
import calendar
from dateutil import parser, relativedelta
from datetime import time, date, timedelta
from sty import fg, bg, ef, rs, mute, unmute #for terminal-output coloring

def exocortexRAM_banner():
	print('''\n\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄█░█░█▀▄▄▀█▀▄▀█▀▄▄▀█░▄▄▀█▄░▄█░▄▄█░█░█▀▄██░▄▄▀█░▄▄▀██░▄▀▄░█▄▀
██░▄▄▄█▀▄▀█░██░█░█▀█░██░█░▀▀▄██░██░▄▄█▀▄▀█░███░▀▀▄█░▀▀░██░█░█░██░
██░▀▀▀█▄█▄██▄▄███▄███▄▄██▄█▄▄██▄██▄▄▄█▄█▄█▄▀██░██░█░██░██░███░█▀▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▀███▀█░▄▄░████░▄▄░█▀░████░▄▄▀█░██▀▄▄▀█░████░▄▄▀
██░▀░██░▀▄░█▀▀█░▀▄░██░████░▀▀░█░██░▀▀░█░▄▄░█░▀▀░
███▄███░▀▀░█▄▄█░▀▀░█▀░▀███▄██▄█▄▄█░████▄██▄█▄██▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n''')

# Decide whether to read an existing file, or write to it
def chooose():
	exocortexRAM_banner()
	while True:
		choice = input("Select one: 'review' or 'add' >> ")
		if choice in ("review", "add"):
			if choice == "review":
				print("Opening your notebook for review!")
				exo_notes = open("exocortex.txt", "r")
				readFile(exo_notes)
				exo_notes.close()
			elif choice == "add":
				print("You've chosen to pen down additional thoughts!")
				exo_tasks = open("exocortex.txt", "a")
				writeFile(exo_tasks)
				exo_tasks.close()
			break
		else:
			print("🅧  Invalid input :(\n")

def readFile(notebook):
	
	lineNum = 0
	recorded_thoughts = []
	
	print("\nCurrent Version\n---------------")
	for currentLine in notebook:
		lineNum += 1
		formatted_line = f"{lineNum}: {currentLine}"
		recorded_thoughts.append(formatted_line)
		print(recorded_thoughts[lineNum-1], end="")
	
	# return recorded_thoughts

def writeFile(notebook):

	#extract relevant lines to ActionPlan.txt
	todolist = []
	
	print("\nTake note of your thoughts on any topics of interest you'd like to explore in the future")
	print("If there are any actionable tasks that are @due in a time-sensitive manner or an @important priority, use '@' tags for contextually relevant reviews!")
	print("\nWhen you are done writing, simply type 'done' to exit this journal-entry mode")
	
	while True: #indefinite loop 
		user_response = input(">>") #prompt and save input
		if user_response == "done": #escape clause
			break #break out of while-loop on keyword
		else:
			todolist.append(user_response) #get bot response to user input and print to screen
			continue #restart while-loop... gotta keep that convo alive!
	
	#for_loop_iteration
		# todolist.append(task_to_add)

	list_length = len(todolist)
	for i in range(list_length):
		formatted_string = todolist[i] + "\n"
		notebook.writelines(formatted_string)

	# print("Exocortex has been updated. Here are the entries you've added to the journal!\n")
	# display_updates(todolist)

# PSEUDOCODED STARTER-TEMPLATE IDEA 
# def list_tasks(function args = list of strings, or possibly dict of task + time-prio/import-urgent tags key+val combo)
def display_updates(newly_added_tasks):

	index = 0
	formatted_list = []
	
	for task in newly_added_tasks:
		index += 1
	
		if "@" in task:
	
			# if @contextual_tag signifies priority a-la @important, @flagged, etc
			if "@importan" in task:	#catched "important" ans well as "importance"
				effectValue = 'blink'
				foregroundColor = 'black'
				backgroundColor = 'magenta' #24-bit code for orange is 255,150,50 but it's throwing up errors so ¯\_(ツ)_/¯	
			elif  "@cancel" in task: #catches "@cancel" in the present tense, as well as prior tasks that were "@cancelled"
				effectValue = 'dim'
				foregroundColor = 'black'
				backgroundColor = 'white'
			elif "@drop" in task: # if user chooses to "@drop" the item now, or reflects on something that was "@dropped" in the past
				effectValue = 'hidden'
				foregroundColor = 'white'
				backgroundColor = 'black'
			elif "@done" in task: # even if it was completed at the time of input, "done" tasks are inherently past-tense i.e. over with and archived
				effectValue = 'strike'
				foregroundColor = 'green'
				backgroundColor = 'black'
	
			#if context is a temporal-tag like @due or @defer to signify an ideal start-date or an urgent deadline
			# if "@due" in task:
				# deltaValue = calcUrgency(task) # NOTA BENE: Running out of time :(

# ...And the irony isn't lost on me that I can't format @due dates properly because this project is due soon >_<
# But I'm calling an audible and killing any further development of display_updates() because it's becoming a time-sink

# 	FYI, here is the PSUEDOCODE I wrote for this part prior to coding... 
# 	if line contains temporal_tags #(regex?:date/format OR list_of_days OR time:format)
# 		if before currentTime
# 			bg.red + ef.bold 		# "overdue" styling
# 		elif due_soon = true		# due within 24 hrs
# 			fg.yellow + ef.underl
# 		else 						# i.e. if start OR defer OR due tag value exceeds due_soon conditional check
# 			ef.italic

# Needless to say, "urgency calculations()" was dropped along with the formatted_display() function
# def calculate_Urgency(task_on_Line):
# 	dueValue = scrape_keywords(strip_line(task_on_Line))
# 	if scrape_date(dueValue) > time.hour(24)
# regex turned out to be the bane of my existence... also I had a late start so I'll take partial responsibility for that😅

# NB: After attempting to write my own parser-functions above, I eventually tried to switch tactics and use dateutil.parse
# The results from one solution, or the other, would've yielded me a string of YYYY-MM-DD HH-MM format
# Then I planned to use datetime's built-in strptime(inputVariable, "%format-%template-%here) to return actual integers
# From there, it would've been trivial to use dateutil.timedelta() to calculate >24 hrs, ≤ 24 hrs, or if it was a negative value 
# i.e. an overdue task due date that is prior to the value of datetime.today()

# Oh, also I planned to compare "day" in the stripped taskline to catch keywords like "Monday, Tuesday, etc"
# So scrape_keywords() could've potentially branched off into another function dedicated to non-numeric due-calculations
# buuuuut, Haphestus - the god of technology - didn't look down upon me with favor... or something ಠ_ಠ
# So I rage quit at this point (╯°□°）╯︵ ┻━┻

		formatted_line = ef(effectValue) + fg(foregroundColor) + bg(backgroundColor) +  task + rs.all #swap task+ tags for ▶️ f"{lineNum}: {currentLine}" 
		formatted_list.append(formatted_line)
		print(formatted_list[index-1], end="\n")
	# return formatted_list

#prompt user to rerun program from choose() function's decision tree logic
def again():
	access_RAM_again = input("\nDo you have more tasks you need to remember?\nPlease type Y for YES or N for NO. >> ")
	if access_RAM_again.upper() == 'Y':
		chooose()
	elif access_RAM_again.upper() == 'N':
		RAM_ReviewAndClose()
	else:
		again()

def RAM_ReviewAndClose():
	exocortexRAM_banner()
	print('''\nThank you for using Remote_Access_Memory to offload some of your mental RAM.
Here are the latest entries made to your very own Exo-cortex!''')
	
	finalDraft = open("exocortex.txt", "r")
	readFile(finalDraft)
	finalDraft.close()

	# PROTIP - intersperse sty.un/mute(method) in-between formatted tasks to display notes in plain-text style
	# mute(fg,bg,ef)
	# unmute(fg,bg,ef)
	# UPDATE : couldn't get this to reliably work either, so I'm displaying the final-draft as-is.... bite me :P
	exit

chooose()
again()

#appended this dataset output at the end throughout my coding for testing purposes... so much good that did me T_T
todolist = ["This is an @important task", "So is this @flagged", "This task has been @cancelled", "This task was @dropped due to unforseen circumstances", "This task has been completed! @done"]
todolist.append("This task is @due on Monday")
todolist.append("This task was @due day before yesterday")
todolist.append("This task was @due @yesterday")
todolist.append("This task is @due @today")
todolist.append("This task is @due @tomorrow")
todolist.append("This task is @due day after tomorrow")
todolist.append("This task is @due next week")
todolist.append("This task was @due last week")
todolist.append("This task is @due(2020.10.20)")
todolist.append("This task is @due(+2d")
todolist.append("This task is @due(+4w")
todolist.append("This task is @due(-1d)")
todolist.append("This task is @due(5h50m)")
todolist.append("This task is @due at 15:00 sharp")
display_updates(todolist) #FYI, this actually worked 👌🏼 
# if it wasn't for the intensive time-constraint I would've figured out how to effectively regex text-file contents...