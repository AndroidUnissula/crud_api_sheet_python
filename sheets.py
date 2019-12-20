# https://www.youtube.com/watch?v=cnPlKLEGR7E&t=46s
# pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

crud = ServiceAccountCredentials.from_json_keyfile_name("crud.json", scope)

client = gspread.authorize(crud)

#menyambungkan dengan file yang ada di google sheet
# variable = client.open("nama_file_spreadsheets").nama_sheets
sheet = client.open("crud_python").sheet1

# mengambil semua data
data = sheet.get_all_records()
print("ISI SEMUA DATA : ")
pprint(data)
print(100*"=")

#menampilkan data baris ke - ...
row = sheet.row_values(3)
print("BARIS KE-3 BERISI :")
pprint(row)
print(100*"=")

#menampilkan isi dari colom
col = sheet.col_values(2)
print("ISI DARI COLOM KE-2 :")
pprint(col)
print(100*"=")

#menampilkan data cell tertentu
cell = sheet.cell(2,2).value
print("MENAMPILKAN ISI COLOM (2,2) :")
print("data baris 2 kolom dua adalah : ", cell)
print(100*"=")


#menambahkan data baru pada baris ke - 4
# data_baru = [3,"Johan Stiya Budi", 9243827]
# sheet.insert_row(data_baru,4)

# Menghapus data pada baris ke-4
# sheet.delete_row(6)

#merubah data baris ke 4 kolom ke 2 dengan value = "Naruto"
# sheet.update_cell(4,2,"Naruto")

#menampilkan jumlah baris spreadsheet
print("MENAMPILKAN JUMLAH BARIS YANG ADA DI SPREADSHEET")
jumlahbaris= sheet.row_count
print(jumlahbaris, "baris")
print(100*"=")

#menampilkan jumlah data yang ada isinya
print("jumlah data : " , len(data), " baris")

# menambahkan data pada baris terakhir
nama= input("masukkan nama : ")
nim= int(input("masukkan nim : "))
datas = len(data)
sheet.insert_row([datas+1,nama,nim],datas+2)

# Mencari data ke-
# cari_data = input("masukkan nomor data : ")
# aa = sheet.col_values(1)
# for i in aa:
#     if i == cari_data:
#         dapat = int(cari_data)+1
#         print(sheet.row_values(dapat))