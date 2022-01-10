
'''db = {'order_with_names':{},
'final_order':[],
'list_of_products':[] 
'costs_of_products':{}
}
'''
costs_of_products = {}
order_with_names = {} 
final_order = []
list_of_products = []


def order(list_of_products, costs_of_products): #funkcja przyjmuje listę stringów produktów i dict produktów z ceną zadeklarowanych przez Producenta, z tych produktów Klient wybiera co i ile chce, funkcja zwraca dict - pojedyncze zamówienie 

	print(f'''Złóż swoje zamówienie
Dostępne warzywa i owoce: {list_of_products}''')
	for products, cost in costs_of_products.items():
		print(f'{products} - {cost} zł/kg')
	single_order = {}
	while True:
		name_of_product = input('Warzywa/owoce, które chcesz zamówić: ')
		if name_of_product in list_of_products:
			number_of_kilograms = int(input('Ilość kilogramów: '))
			single_order[name_of_product] = number_of_kilograms
		else:
			print('Nasi producenci nie hodują takich warzyw/owoców.')
		print(single_order)


		quit = input('''dalsze zamówienie - kliknij enter
koniec zamówienia - kliknij 0 i enter
''')
		if quit == '0':
			print('Dziękujemy za złożone zamówienie!')
			break
	return single_order


def add_products(): #funkcja dla Producenta zwraca listę hodowanych przez niego artykułów oraz dict z produkatami i ceną 

	print('Dodaj możliwe do wyhodowania warzywa i owoce.')

	while True:
		name_of_product = input('Warzywa/owoce, które chcesz dodać: ')
		cost_of_product = int(input('Cena za kilogram: '))
		list_of_products.append(name_of_product)
		costs_of_products[name_of_product] = cost_of_product
		print(costs_of_products)

		quit = input('''dalsze dodawanie - kliknij enter
koniec dodawania - kliknij 0 i enter
''')
		if quit == '0':
			print('Dziękujemy za deklarację upraw!')
			break
	return list_of_products, costs_of_products


def sum_of_orders(final_order): # funkcja przyjmuje listę final order - wszystkie zamówienia, zwraca podsumowanie dla Producenta - ile czego ma wyhodować
	if final_order != []:
		print(f'Liczba zamówień: {len(final_order)}')
		print(final_order)
		all_all = []
		for value in final_order.values():
			for product, amount in value.items():
				all_all.append({product:amount})
		print(all_all)
		result = {}
		for product in all_all:
			for k in product.keys():
				result[k] = result.get(k, 0) + product[k] # tu się dzieje jakaś magia
	return result


def new_client(): # funkcja dodaje nowego klienta i jego zamówienie 
	name = input('Podaj imię i nazwisko: ') 
	order_with_names[name] = order(list_of_products, costs_of_products)
	return order_with_names

def new_producent():
	producent_name = input('Podaj imię i nazisko:')


def final_cost(name, final_order): # czy potrzebna?
	exact_order = final_order[name]
	print(exact_order)
	return exact_order


def suma(exact,costs_of_products,harvest_all): # funkcja przyjmuje konkretne zamówienie, dict z produktami i cenami i finalne zbiory, zwraca rachunek
	final = 0
	for key in exact.keys():
		cost = round(costs_of_products.get(key)*exact[key]*harvest_all.get(key),2)
		final += round(cost,2)
		print(f'''Kwota do zapłaty za {key} ({costs_of_products.get(key)}zł/kg) to: {cost}zł
{costs_of_products.get(key)}zł/kg * {exact[key]} kg * {round(harvest_all.get(key),2)} nadwyżki/niedoboru zbiorów''') #dobra, tutaj powinno być pytanie czy Klient chce tę nadwyżkę, kiedyś
	print(f'Łączna kwota do zapłaty to: {round(final,2)}zł')
	return suma


def harvest(total_order): # funkcja przyjmuje zamówienie, zwraca wynik zbiorów  
	harvest = dict()
	for zbiory, kg in total_order.items():
		actual_number_of_kilograms = int(input(f'{zbiory}: '))
		harvest[zbiory] = actual_number_of_kilograms/kg
		#harvest[zbiory].append(actual_number_of_kilograms)
	return harvest	


def main():
	total_order = []
	print('Witamy w Kooperatywie Dobrze!')

	while True:

		kto = input(''' 
		Kim jesteś?
		1) Klientem
		2) Producentem
		''')
			
		if kto == '1':
			while True:
				action = input('''Co chcesz zrobić?
					a) złożyć zamówienie
					b) odebrać zamówienie
					''')
				if action == 'a':
					if list_of_products != []:
						final_order = new_client()
					else:
						print('Nasi producenci jeszcze nie przedstawili deklaracji upraw.')
				if action == 'b':
					if total_order != []:
						name = input('Podaj imię i nazwisko: ')
						exact = final_cost(name, final_order)
						all_all_all = suma(exact,costs_of_products,harvest_all)
					else:
						print('Nie możesz jeszcze odebrać zamówienia')
				else:
					break

		elif kto == '2':

			while True:
				action = input('''Co chcesz zrobić?
					a) złożyć deklarację upraw
					b) przyjąć zamówienie
					c) wprowadzić dane odnośnie zbiorów
					d) wystawić rachunek
					''')
				if action == 'a':
					final_list_of_products = add_products()
				if action == 'b': 	
					if order_with_names != {}:
						total_order = sum_of_orders(final_order)
						print(f'Łączna ilość warzyw/owoców do wyhodowania: {total_order}')
					else:
						print('Brak zamówień')
				if action == 'c':
					print(f'Ile wydało Ci się zebrać plonów? Pamiętaj, że Twoje łączne zamówienie obejmowało: {total_order}')
					if order_with_names != {}:
						harvest_all = harvest(total_order)
					else:
						print('''Nie możesz teraz wykonać tego działania.
Najpierw należy złożyć deklarację upraw i przyjąć zamówienie''')
				if action == 'd':
					name = input('Podaj imię i nazwisko osoby zamawiającej: ')
					exact = final_cost(name, final_order)
					all_all_all = suma(exact,costs_of_products,harvest_all)

				else:
					break	

print(main())






