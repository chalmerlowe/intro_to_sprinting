#
#
#
def addition():
	# Needs input validation
	print("The sum is ", float(input("Enter the first number:\t\t")) + float(input("Enter the second number:\t")))

def factorial():
	# Needs input validation
	n = int(input("Enter the number:\t"))
	if n < 0:
		print("Factorial not defined for negitive numbers.\n")
	elif n == 0:
		print("0! = 1")
	else:
		f = 1
		for i in range(1, n+1):
			f = f * i
		print('{}! = {}\n'.format(n,f))

def diplay_menu(menu_keys):
	print("\nSelect the operation you wish to use: \n")
	i = 0
	for key in menu_keys:
		i+= 1
		print("\t", i, "\t", key)
	print("\n\t 'X' To Exit\n")

# Add new functions to menu items
menu_items = {"Add":addition,
				"Factorial":factorial }

menu_keys = sorted(menu_items.keys())

selected_operation = ""

while(selected_operation.upper() != "X" ):
	diplay_menu(menu_keys)
	selected_operation = input("Select Operation: ")

	if selected_operation.isdigit() and int(selected_operation) <= len(menu_keys) and int(selected_operation) > 0:
		menu_items[menu_keys[int(selected_operation)-1]]()