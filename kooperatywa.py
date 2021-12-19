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
order_with_names = []
final_order = []
list_of_products = [] 


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
		list_of_products.append(name_of_product)
		print(list_of_products)

		quit = input('''dalsze dodawanie - kliknij enter
koniec dodawania - kliknij 0 i enter
''')
		if quit == '0':
			print('Dziękujemy za deklarację upraw!')
			break
	return list_of_products



def sum_of_orders(final_order): # ta funkcja jest chyba przekombinowana, ale już się zapadłam w jednym toku myślenia
	if final_order != []:
		print(f'Liczba zamówień: {len(final_order)}')
		print(final_order)
		all_all = []
		for orders in final_order:
			for key, value in orders[1].items():
				all_all.append({key:value})
		print(all_all)
		result = {}
		for product in all_all:
			for k in product.keys():
				result[k] = result.get(k, 0) + product[k] # tu się dzieje jakaś magia, nie rozumiem ale działa
	return result



def new_client():
	name = input('Podaj imię i nazwisko: ') # można też jakoś nadawać numery klientom, ale to rozwiązanie wydało mi się łatwiejsze
	order_with_names.append((name, order(list_of_products)))
	return order_with_names



def main():
	print('Witamy w Kooperatywie Dobrze!')

	while True:

		kto = input(''' 
		Kim jesteś?
		1) Klientem
		2) Producentem
		''')
			
		if kto == '1':
			if list_of_products != []:
				final_order = new_client()
			else:
				print('Nasi producenci jeszcze nie przedstawili deklaracji upraw.')

		elif kto == '2':

			while True:
				action = input('''Co chcesz zrobić?
					a) złożyć deklarację upraw
					b) przyjąć zamówienie
					c) wprowadzić dane odnośnie zbiorów
					d) 
					''')
				if action == 'a':
					final_list_of_products = add_products()
				if action == 'b': 	
					if order_with_names != []:
						total_order = sum_of_orders(final_order)
						print(f'Łączna ilość warzyw/owoców do wyhodowania: {total_order}')
					else:
						print('Brak zamówień')
				if action == 'c':
					print(f'Ile wydało Ci się zebrać plonów? Pamiętaj, że Twoje łączne zamówienie obejmowało: {total_order}')
					if order_with_names != []:
						harvest = dict()
						for zbiory, kg in total_order.items():
							actual_number_of_kilograms = int(input(f'{zbiory}: '))
							harvest[zbiory] = [kg]
							harvest[zbiory].append(actual_number_of_kilograms)
						return harvest # zwraca mi słownik - klucz = artykuł, wartość = lista z 2 wartościami - ile miało być i ile wyszło finalnie - z tego policzę procent 	
					else:
						print('''Nie możesz teraz wykonać tego działania.
Najpierw należy złożyć deklarację upraw i przyjąć zamówienie''')
				if action == 'd':
					print('raz')
					print(final_order)
					test = final_order.append('hej')
					return test	
				else:
					break

		




print(main())




