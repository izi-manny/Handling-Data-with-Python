cupcake_data = open('CupcakeInvoices.csv')


for row in cupcake_data:
    print(row) # Loops through all the data and print each row.
    cupcakes = row.rstrip('\n').split(',') # Turn into list
    print(cupcakes[2]) #print type of cupcakes


cupcake_data.seek(0)

total = 0

for row in cupcake_data:
    cupcakes = row.rstrip('\n').split(',')
    product = int(cupcakes[3]) * float(cupcakes[4])
    print(product) # prints the total for each invoice
    total += product
print(total) # prints the total for all invoices combined

cupcake_data.close()
