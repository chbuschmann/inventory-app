# inventory-app

Inventory 'App'

Select 	[1] Create new item and attach new UUID from scanner
       [2] Check UUID by scanning QR code

[1]
if next row is empty
 for input in user_input:
   user input: Column 1 Title (item)
         Column 2 Title (Where is it placed)
         Column 3 Title (Scan unique QR code with scanner)
save to excel (openpyxl)
print this entry (this row)

[2]
print('Scan QR code now: ')
scanner input()

if code is in dataframe
 print data
else:
 print('item not found')
