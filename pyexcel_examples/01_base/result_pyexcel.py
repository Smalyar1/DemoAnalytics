import pyexcel as pe
data = pe.get_array(file_name="prices.xlsx")
# data = pe.get_array(file_name="prices.ods")
print(data)
