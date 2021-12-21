'''Zgłosiła się do Was kooperatywa spożywcza, która ma problem z komunikacją na linii
producenci i klienci.
▸ Chcą, żeby producenci mogli dodawać możliwe do wyhodowania warzywa i owoce.
▸ Chcą mieć możliwość składania zamówień przez klientów na warzywa i owoce z dostępnej listy.
▸ Chcą, żeby producenci mogli przyjąć na siebie zlecenia i po zbiorach powinni móc wpisać ile udało im się wychodować jedzenia.
▸ Po zbiorach klienci mogą odebrać jedzenie, proporcjonalnie do swojego zamówienia, czyli jeśli zamówiłem 10 kg ziemniaków, a wyhodowano 10% więcej, to mogę odebrać
11 kg ziemniaków.
▸ * Ceny, czyli chcemy mieć możliwość ustalenia ceny za dane warzywo/owoc i wynagradzania producentów za to co się sprzedało.

producent:
- dodawanie warzyw/owoców ((jeden pies, nie trzeba tu chyba rozróżniać czy jabłko jest owocem czy warzywem))
- dodawanie ceny ((przed czy po zbiorach?)) 
- ilość w kg po zbiorach - ile procent więcej/mniej im się udało ((czyli na początku liczymy ile było zamówień
a potem się do tego odnosimy))
- finalny zysk 

klient:
- składanie zamówienia
	- co 
	- ile zamawia
	- finalny rachunek 

etapy:
---- przed zbiorami ----
1) dodawanie             PRODUCENT input
2) składanie zamówień    KLIENCI input
3) przyjmowanie zlecenia PRODUCENT (po prostu informacja? ten punkt powinien zablokować możliwość powrotu do 2 poprzednich)
---- po zbiorach ----
3) wynik zbiorów + cena	 PRODUCENT input
4) info dla klienta i dla producenta = rachunek? 

'''

total_order = []
order_with_names = {} #zmieniłam na słownik gdzie kluczem jest imię, a wartością zamówienie w postaci kolejnego słownika
final_order = []
list_of_products = [] 
costs_of_products = {}


def order(list_of_products):

	print(f'''Złóż swoje zamówienie
Dostępne warzywa i owoce: {list_of_products}''')
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



def add_products(): 
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




def sum_of_orders(final_order): # ta funkcja jest chyba przekombinowana, ale już się zapadłam w jednym toku myślenia
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
				result[k] = result.get(k, 0) + product[k] # tu się dzieje jakaś magia, nie rozumiem ale działa
	return result



def new_client():
	name = input('Podaj imię i nazwisko: ') # można też jakoś nadawać numery klientom, ale to rozwiązanie wydało mi się łatwiejsze
	order_with_names[name] = order(list_of_products)
	return order_with_names

def final_cost(name, final_order):
	exact_order = final_order[name]
	print(exact_order)
	return exact_order


def suma(exact,costs_of_products,harvest_all):
	final = 0
	for key in exact.keys():
		cost = round(costs_of_products.get(key)*exact[key]*harvest_all.get(key),2)
		final += round(cost,2)
		print(f'''Cena za {key} to: {cost}zł
{costs_of_products.get(key)}zł/kg * {exact[key]} kg * {round(harvest_all.get(key),2)} nadwyżki zbiorów''')
	print(f'Łączna kwota do zapłaty to: {final}zł')


def harvest(total_order):
	harvest = dict()
	for zbiory, kg in total_order.items():
		actual_number_of_kilograms = int(input(f'{zbiory}: '))
		harvest[zbiory] = actual_number_of_kilograms/kg
		#harvest[zbiory].append(actual_number_of_kilograms)
	return harvest 	


def main():
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
					if order_with_names != {}:
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






