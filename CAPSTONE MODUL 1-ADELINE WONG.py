# Menu Utama
menu=['1. Akses Data Karyawan',
      '2. Tambah Data Karyawan',
      '3. Update Data Karyawan',
      '4. Hapus Data Karyawan',
      '5. Keluar dari Program']

# Variabel Sample Data Karyawan
data_karyawan=[
    {'id': 'A001','nama': 'Andi Saputra','umur':25,'departemen':'Komersial','posisi':'Staff'},
    {'id': 'A002','nama': 'Iwan','umur':29,'departemen':'Operasional','posisi':'Supervisor'},
    {'id': 'A003','nama': 'Intan','umur':23,'departemen':'IT','posisi':'Staff'},
    {'id': 'A004','nama': 'Andi Aja','umur':30,'departemen':'IT','posisi':'Departemen Head'},
    {'id': 'A005','nama': 'James Saputra','umur':50,'departemen':'Marketing','posisi':'Departemen Head'}
    ]

# Membuat format header informasi tabel 
def headertabel():
    print('No.\t | ID\t | Nama\t\t\t\t | Umur\t | Departemen\t | Posisi\t\t |')
    print('--------------------------------------------------------------------------------------------------')

# Membuat format header garis
def garis():
    print('---------------------------------------------------------------')

# Membuat format jika input menu yang dimasukkan salah
def wrong_menu():
    print('\n**Input Menu yang Anda Masukkan Tidak Sesuai**\n')

# Membuat filter pencarian pada data karyawan dengan ID karyawan (hasil dalam list(index,data))
# dengan catatan ID Karyawan adalah kolom unique
def filter_by_id(search_id):
    hasilFilterID = []
    for i,j in enumerate(data_karyawan):
        if search_id.lower() == j['id'].lower():
            hasilFilterID.append((i,j))
    return hasilFilterID

# Membuat filter pencarian pada data karyawan dengan Nama karyawan (hasil dalam list(index,data))
# nama di filter secara per kata dimana dapat mengeluarkan hasil lebih dari 1
def filter_by_name(search_name):
    hasilFilterNama = []
    search_words = search_name.lower().split()
    for i,j in enumerate(data_karyawan):
        name_words = j['nama'].lower().split()
        # fungsi all() akan mengecek jika seluruh kata yang dicari ada di data nama
        # word in name_words akan mengeluarkan hasil boolean (True atau False) 
        if all(word in name_words for word in search_words):
            hasilFilterNama.append((i,j))
    return hasilFilterNama

# Membuat filter pencarian pada data karyawan dengan Nama Departemen (hasil dalam list(index,data))
def filter_by_dept(search_id):
    hasilFilterID = []
    for i,j in enumerate(data_karyawan):
        if search_id.lower() == j['departemen'].lower():
            hasilFilterID.append((i,j))
    return hasilFilterID

# Membuat filter pencarian pada data karyawan dengan posisi karyawan (hasil dalam list(index,data))
def filter_by_posisi(search_id):
    hasilFilterID = []
    for i,j in enumerate(data_karyawan):
        if search_id.lower() == j['posisi'].lower():
            hasilFilterID.append((i,j))
    return hasilFilterID

# Read : Akses data karyawan keseluruhan ataupun dengan data tertentu
def akses_data():
    while True:
        print('\n------------------------Menu Akses Data------------------------')
        print('1. Akses Seluruh Data Karyawan')
        print('2. Akses Data Karyawan Tertentu')
        print('3. Kembali ke Menu Utama')
        garis()

        aks=input("\n Mohon Masukkan Angka Pilihan Sub-Menu Anda (1-3):")
        
        if aks =='1':
            if len(data_karyawan) !=0:
                print('\nData Karyawan:')
                headertabel()
                for i,j in enumerate(data_karyawan):
                    print(f"{i+1}\t | {j['id']}\t | {j['nama']:<15}\t\t | {j['umur']}\t | {j['departemen']:<10}\t | {j['posisi']:<20}\t |")
            else:
                print('\n*Tidak Ada Data Karyawan*')
        
        elif aks =='2':
            if len(data_karyawan) !=0:
                while True:
                    print('\n-----------------------Menu Akses Data 2-----------------------')
                    print('1. Akses Data dengan ID atau Nama Karyawan')
                    print('2. Akses Data dengan Nama Departemen atau Posisi Karyawan')
                    print('3. Kembali ke Menu Sebelumnya')
                    garis()
                    aks_sub=input("Mohon Masukkan Angka Pilihan Sub-Menu Anda (1-3):")
                    if aks_sub=='1':
                        aks_idn=input('Masukkan ID atau Nama Karyawan:')

                        # Melakukan filter dengan ID dan Nama. Jika hasil match dengan input, list filter_input akan mempunyai isi 
                        filter_inpAks_idn = filter_by_id(aks_idn) + filter_by_name(aks_idn)                
                        
                        if filter_inpAks_idn:
                            garis()
                            headertabel()
                            for i, j in filter_inpAks_idn:
                                print(f"{i+1}\t | {j['id']}\t | {j['nama']:<15}\t\t | {j['umur']}\t | {j['departemen']:<10}\t | {j['posisi']:<20}\t |")
                        else:
                            print(f'\n*Tidak Ada Data Karyawan dengan No. ID atau Nama {aks_idn.capitalize()}*')
                    
                    elif aks_sub=='2':
                        aks_dp=input('Masukkan Departemen atau Posisi:')

                        # Melakukan filter dengan departemen dan posisi. Jika hasil match dengan input, list filter_input akan mempunyai isi 
                        filter_inpAks_dp = filter_by_dept(aks_dp) + filter_by_posisi(aks_dp)                
                        
                        if filter_inpAks_dp:
                            garis()
                            headertabel()
                            for i, j in filter_inpAks_dp:
                                print(f"{i+1}\t | {j['id']}\t | {j['nama']:<15}\t\t | {j['umur']}\t | {j['departemen']:<10}\t | {j['posisi']:<20}\t |")
                        else:
                            print(f'\n*Tidak Ada Data Karyawan dengan Departemen atau Posisi {aks_dp.capitalize()}*')
                
                    elif aks_sub=='3':
                        break
                    
                    else:
                        wrong_menu()
            
            else:
                print('\n*Tidak Ada Data Karyawan*')
        
        elif aks =='3':
            main_menu()
        
        else:
            wrong_menu()

# Create : Membuat data Karyawan Baru
def new_data():
    while True:
        print('\n----------------------Menu Penambahan Data-----------------------')
        print('1. Tambah Data Karyawan')
        print('2. Kembali ke Menu Utama')
        garis()

        new=input("\n Mohon Masukkan Angka Pilihan Sub-Menu Anda (1-2):")

        if new =='1':
            garis()
            inpID=input('Masukkan ID Karyawan:').upper()
          
            filter_inpID=filter_by_id(inpID)

            if filter_inpID:
                garis()
                print('No ID yang anda masukkan sudah ada dengan detail berikut:')
                headertabel()
                for i, j in filter_inpID:
                    print(f"{i+1}\t | {j['id']}\t | {j['nama']:<15}\t\t | {j['umur']}\t | {j['departemen']:<10}\t | {j['posisi']:<20}\t |")

            else:
                inpNama=input('Masukkan Nama Karyawan:').capitalize()
                inpUmur=input('Masukkan Umur Karyawan:').capitalize()
                inpDep=input('Masukkan Departemen Karyawan:').capitalize()
                inpPos=input('Masukkan Posisi Karyawan:').capitalize()

                garis()
                print('Data Tambahan:')
                print(f'ID: {inpID}, Nama: {inpNama}, Umur: {inpUmur}, Departemen: {inpDep}, Posisi: {inpPos}')
                garis()
                
                while True:
                    konf_new=input('Apakah anda yakin data berikut akan anda simpan? (Y/N):').upper()
                    if konf_new == 'Y':
                        data_karyawan.append({'id': inpID,'nama': inpNama,'umur':inpUmur,'departemen':inpDep,'posisi':inpPos})
                        garis()
                        print('Data Telah Berhasil Disimpan')
                        garis()
                        break
                    elif konf_new == 'N':
                        garis()
                        print('Data Tidak Tersimpan\n')
                        garis()
                        break
                    else:
                        wrong_menu()
        
        elif new =='2':
            main_menu()
        
        else:
            wrong_menu()
        
# Update : Mengubah Data Karyawan Tertentu dengan Input Baru
def update_data():
    while True:
        print('\n-----------------------Menu Update Data------------------------')
        print('1. Update Data Karyawan')
        print('2. Kembali ke Menu Utama')
        garis()

        upd=input("\n Mohon Masukkan Angka Pilihan Sub-Menu Anda (1-2):")

        if upd =='1':
            garis()
            updID=input('Masukkan No ID Karyawan:').upper()
          
            filter_updID=filter_by_id(updID)

            if filter_updID:
                print(f'\nDetail Data untuk ID {updID}:')
                headertabel()
                for i, j in filter_updID:
                    print(f"{i+1}\t | {j['id']}\t | {j['nama']:<15}\t\t | {j['umur']}\t | {j['departemen']:<10}\t | {j['posisi']:<20}\t |")
                
                while True:
                    kolom_upd=input('\nMasukkan nama kolom yang akan dilakukan penggantian data:').lower()
                    if kolom_upd == 'id' or kolom_upd =='nama' or kolom_upd =='umur' or kolom_upd =='departemen' or kolom_upd =='posisi':
                        break
                    else: wrong_menu()

                data_upd=input(f'Masukkan data baru untuk kolom {kolom_upd}:').capitalize()

                while True:
                    konf_upd=input('\nApakah anda yakin data berikut akan anda simpan? (Y/N):').upper()
                    if konf_upd == 'Y':
                        data_karyawan[filter_updID[0][0]][kolom_upd]=data_upd
                        garis()
                        print('Data Telah Berhasil Disimpan')
                        garis()
                        break
                    elif konf_upd == 'N':
                        garis()
                        print('Data Tidak Tersimpan')
                        garis()
                        break
                    else:
                        wrong_menu()
            
            else:
                print(f'\n*Tidak Ada Data Karyawan dengan No. ID {updID}*')
        
        elif upd =='2':
            main_menu()
        
        else:
            wrong_menu()  

# Delete : Menghapus data karyawan
def delete_data():
    while True:
        print('\n-----------------------Menu Hapus Data------------------------')
        print('1. Hapus Data Karyawan dengan No. ID')
        print('2. Hapus Semua Data Karyawan')
        print('3. Kembali ke Menu Utama')
        garis()

        del_data=input("\n Mohon Masukkan Angka Pilihan Sub-Menu Anda (1-3):")

        if del_data =='1':
            garis()
            delID=input('Masukkan No ID Karyawan:').upper()
          
            filter_delID=filter_by_id(delID)

            if filter_delID:
                print(f'\nDetail Data untuk ID {delID}:')
                headertabel()
                for i, j in filter_delID:
                    print(f"{i+1}\t | {j['id']}\t | {j['nama']:<15}\t\t | {j['umur']}\t | {j['departemen']:<10}\t | {j['posisi']:<20}\t |")

                while True:
                    konf_del=input(f'Apakah anda yakin untuk menghapus data dengan ID {delID}? (Y/N):').upper()
                    if konf_del == 'Y':
                        del data_karyawan[filter_delID[0][0]]
                        garis()
                        print('Data Telah Berhasil Dihapus')
                        garis()
                        break
                    elif konf_del == 'N':
                        garis()
                        print('Data Tidak Terhapus')
                        garis()
                        break
                    else:
                        wrong_menu()
            
            else:
                print(f'\n*Tidak Ada Data Karyawan dengan No. ID {delID}*')
        
        elif del_data =='2':
            while True:
                    konf_del=input(f'Apakah anda yakin untuk menghapus semua data karyawan? (Y/N):').upper()
                    if konf_del == 'Y':
                        data_karyawan.clear()
                        garis()
                        print('Semua Data Telah Berhasil Dihapus')
                        garis()
                        break
                    elif konf_del == 'N':
                        garis()
                        print('Data Tidak Terhapus')
                        garis()
                        break
                    else:
                        wrong_menu()
        
        elif del_data =='3':
            main_menu()
        
        else:
            wrong_menu() 

# Fungi Main Menu
def main_menu():
    while True:
        print('\n----------------Data Karyawan PT. Makmur Sukses----------------')
        for i in menu:
            print(i)
        garis()
        ops=input("Mohon Masukkan Angka Pilihan Menu Anda (1-5):")
        if ops== '1':
            akses_data()
        elif ops=='2':
            new_data()
        elif ops=='3':
            update_data()
        elif ops=='4':
            delete_data()
        elif ops=='5':
            print('\n**Terima kasih dan Sampai Jumpa Kembali**\n')
            quit()
        else:
            wrong_menu()

# Start Program
main_menu()