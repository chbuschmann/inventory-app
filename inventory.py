import xlrd

file_location = r"excel_files/Inventory.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
qrCode = input('Please scan QR code now: ')

columns_to_output = [1, 5, 6, 7]
# Iterate over every rows of the file
for row in range(sheet.nrows):
	# If the user name match the input
	if qrCode == sheet.cell_value(row, 5):
		# Iterate over the column to output list
		for col in columns_to_output:
			# Printing the cell at given column in the row.
			print(str(sheet.cell_value(row, col)))
