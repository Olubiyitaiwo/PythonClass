def remove_items():

	total_unwanted_items = add_to_cart()
	item_not_needed = int(input("Select items to remove: "))
	
	match(item_removed):
		case 1:
			total_unwanted-items.remove(list_of_laptop)
		 
		case 2:
			total_unwanted-items.remove(list_of_phone)
		
		case 3:
			total_unwanted-items.remove(list_of_headphone)
	return total_unwanted-items	
	item_removed = add_to_cart()
	
def selected_items():
	
	total_items = add_to_cart()
	print(total_items)
	
def add_to_cart():
	
	general_items_puchased = []
	list_of_laptop = ["Laptop", 1000]
	list_of_phone = ["Phone", 500]
	list_of_headphone = ["Headphone",100]
	items = view_products
	print(items)
		
	match(items):
		case 1:
			general_items_puchased.append(list_of_laptop)
			
		case 2:
			general_items_puchased.append(list_of_phone)
			
		case 3:
			general_items_puchased.append(list_of_headphone)
	general_items_puchased = add_to_cart()
	option = input("Do you wish to continue?: ")
	if option == "no":
		main_menu()
		
	if option =="yes":
		print(general_items_puchased)
		add_to_cart()	
	return general_items_puchased
	
		

def view_products():
	print("""
1. Laptop - $1000
2. Phone - $500
3. Headphone - $100	
""")
	input_value = int(input("Click to add product: "))
	add_to_cart()
	return input_value
	

def main_menu():
	print("""Welcome to jessica's E-Store 
1. View Products 
2. Add to Cart 
3. Remove from cart 
4. View cart 
5. Checkout 
6.Exit""")

	user_choice = int(input("Pick from the menu list: "))
	match(user_choice):
		case 1:
			view_products()
		#case 2:
			add_to_cart()
		#case 3:
			#Remove from cart
		#case 4:
			#View cart
		#case 5:
			#Checkout
		#case 6:
			#Exit

main_menu()
#add_to_cart()
#selected_items()
