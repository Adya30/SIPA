import os
import pandas as pd
from datetime import datetime
from tabulate import tabulate

# CSV HANDLE
def akun_admin_csv():
    file_path = 'admin.csv'
    if not os.path.exists(file_path):
        buat_header = pd.DataFrame([{'username': 'admin', 'password': 'admin123'}])
        buat_header.to_csv(file_path, index=False)

def akun_petani_csv():
    file_path = 'akun.csv'
    if not os.path.exists(file_path):
        buat_header = pd.DataFrame(columns=['username', 'password', 'nama lengkap', 'jenis kelamin', 'tgl lahir', 'no telp', 'alamat'])
        buat_header.to_csv(file_path, index=False)

def jadwal_tanam_csv():
    file_path = 'jadwal_tanam.csv'
    if not os.path.exists(file_path):
        buat_header = pd.DataFrame(columns=['username', 'tanggal tanam', 'jenis tanaman', 'keterangan', 'status'])
        buat_header.to_csv(file_path, index=False)

def rekomendasi_pupuk_csv():
    file_path = 'pupuk.csv'
    if not os.path.exists(file_path):
        buat_header = pd.DataFrame(columns=['jenis tanaman', 'untuk cuaca', 'pupuk yang cocok', 'saran'])
        buat_header.to_csv(file_path, index=False)

def laporan_petani_csv():
    file_path = 'laporan.csv'
    if not os.path.exists(file_path):
        buat_header = pd.DataFrame(columns=['username', 'jenis laporan',  'laporan', 'jawaban dan solusi'])
        buat_header.to_csv(file_path, index=False)
# ====================================================================================================

def menu_utama():
    os.system('cls')
    print('===========================================================')
    print('                  SELAMAT DATANG DI SIPA                   ')
    print('            SISTEM INFORMASI PENJADWALAN SAWAH             ')
    print('===========================================================')
    print('''Halaman Utama :
    1. LOGIN ADMIN
    2. LOGIN PETANI
    3. REGISTER''')
    pilih = input('Masukkan Pilihan : ')
    if pilih == '1':
        os.system('cls')
        login_admin()
    elif pilih == '2':
        os.system('cls')
        login_petani()
    elif pilih == '3':
        os.system('cls')
        register()
    else:
        input('Inputan salah, enter untuk ulangi')
        os.system('cls')
        menu_utama()

def register():
    os.system('cls')
    akun_petani_csv()
    print('=============================================================')
    print('                     REGISTER PETANI                         ')
    print('=============================================================')
    print('''Perhatikan Syarat dan Ketentuan : 
        - Tanggal lahir harus sesuai format (YYYY-MM-DD)
        - Username minimal 4 karakter
        - Password minimal 8 karakter''')
    nama_lengkap = input('Masukkan Nama Lengkap : ').title()
    tanggal_lahir = input('Masukkan Tanggal Lahir (YYYY-MM-DD) : ')
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')
    konfirmasi_password = input('Masukkan Konfirmasi Password : ')
    while True:
            konfirmasi = input('Apakah nama user dan password sudah sesuai (y/t) : ').lower()
            if konfirmasi == 'y' :
                if len(nama_lengkap) < 2:
                    input('Username minimal 4 karakter')
                    os.system('cls')
                    register()
                try:
                    datetime.strptime(tanggal_lahir, '%Y-%m-%d')
                except ValueError:
                    input('Format tanggal salah, format (YYYY-MM-DD)')
                    os.system('cls')
                    register()
                if len(username) < 4:
                    input('Username minimal 4 karakter')
                    os.system('cls')
                    register()
                if len(password) < 8:
                    input('Password minimal 8 karakter')
                    os.system('cls')
                    register()
                if password != konfirmasi_password:
                    input('Konfirmasi password tidak cocok')
                    os.system('cls')
                    register()         

                file_akun = pd.read_csv('akun.csv')
                if username in file_akun['username'].values:
                    input('Username sudah terdaftar, silakan gunakan username lain')
                    os.system('cls')
                    register()

                data_baru = pd.DataFrame([{
                    'username': username,
                    'password': password,
                    'nama lengkap': nama_lengkap,
                    'jenis kelamin': '-',
                    'tgl lahir': tanggal_lahir,
                    'no telp': '-',
                    'alamat': '-'
                }])

                file_akun = pd.concat([file_akun, data_baru], ignore_index=True)
                file_akun.to_csv('akun.csv', index=False)
                input('Edit profil berhasil, tekan enter untuk kembali')
                os.system('cls')
                menu_petani()

            elif konfirmasi == 't' :
                input('Silahkan tekan enter untuk kembali')
                menu_utama()    
            else :
                print('Input invalid, ulangi')
            
def login_petani():
    os.system('cls')
    akun_petani_csv()
    global usernamelogin
    print('=============================================================')
    print('                       LOGIN PETANI                          ')
    print('=============================================================')
    username = input('Masukkan username : ')
    password = input('Masukkan Password : ')
    while True:
        konfirmasi = input('Apakah anda ingin melanjutkan login (y/t) : ').lower()
        if konfirmasi == 'y':
            baca_file = pd.read_csv('akun.csv')

            filter_username = baca_file[(baca_file['username'] == username) & (baca_file['password'] == password)]

            if not filter_username.empty:
                usernamelogin = username
                print('Login berhasil!')
                input('tekan enter untuk lanjut ke menu')
                os.system('cls')
                menu_petani()

            else:
                print('Username atau password salah, ulangi')
                input('tekan enter untuk ulangi login')
                os.system('cls')
                login_petani()

        elif konfirmasi == 't':
            os.system('cls')
            menu_utama()
        else:
            print('Inputan invalid, ulangi')

def login_admin():
    os.system('cls')
    akun_admin_csv()
    print('=============================================================')
    print('                         LOGIN ADMIN                         ')
    print('=============================================================')
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')
    while True:
        konfirmasi = input('Apakah anda ingin melanjutkan login (y/t) : ').lower()
        if konfirmasi == 'y':
            baca_file = pd.read_csv('admin.csv')
            filter_username = baca_file[(baca_file['username'] == username) & (baca_file['password'] == password)]
            if not filter_username.empty:
                print('Login berhasil!')
                input('tekan enter untuk lanjut ke menu')
                os.system('cls')
                menu_admin()

            else:
                print('Username atau password salah, ulangi')
                input('tekan enter untuk ulangi login')
                os.system('cls')
                login_admin()

        elif konfirmasi == 't':
            os.system('cls')
            menu_utama()
        else:
            print('Inputan invalid, ulangi')

def menu_petani():
    os.system('cls')
    print('=================================================')
    print('                  MENU PETANI                    ')
    print('=================================================')
    print(f'Halo selamat datang {usernamelogin}')
    print('''Menu Petani :
        1. Buat Jadwal Tanam
        2. Lihat Jadwal Tanam
        3. Edit Jadwal Tanam
        4. Rekomendasi Pupuk
        5. Riwayat Tanam
        6. Laporan Tanaman
        7. Edit Profil
        0. Logout''')
    pilih = input('Masukkan Pilihan : ')
    if pilih == '1':
        os.system('cls')
        buat_jadwal_tanam()

    elif pilih == '2':
        os.system('cls')
        lihat_jadwal_tanam() 

    elif pilih == '3':
        os.system('cls')
        edit_jadwal_tanam()
    
    elif pilih == '4':
        os.system('cls')
        rekomendasi_pupuk()

    elif pilih == '5':
        os.system('cls')
        riwayat_tanam()

    elif pilih == '6':
        os.system('cls')
        laporan_tanam()
        
    elif pilih == '7':
        os.system('cls')
        edit_profil()  
    
    elif pilih == '0':
        while True:
            konfirmasi = input('Apakah yakin Anda ingin keluar (y/t) : ').lower()
            if konfirmasi == 'y':
                os.system('cls')
                menu_utama()
            elif konfirmasi == 't':
                os.system('cls')
                menu_petani()
            else:
                print('Inputan invalid, ulangi')
    
    else:
        input('Inputan invalid, enter untuk ulangi')
        os.system('cls')
        menu_petani()

def tampilkan_jadwal_tanam():
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_jadwal_username = jadwal[jadwal['username'] == usernamelogin]
    if filter_jadwal_username.empty:
        print('Belum ada jadwal yang tersedia')
    else:
        jadwal_tampil = filter_jadwal_username.copy()
        jadwal_tampil = jadwal_tampil.drop('username', axis=1)
        print(tabulate(jadwal_tampil, headers=['No'] + list(jadwal_tampil.columns), tablefmt='fancy_grid', showindex=range(1, len(jadwal_tampil) + 1)))

def buat_jadwal_tanam():
    os.system('cls')
    jadwal_tanam_csv()
    print('===========================================================')
    print('                     BUAT JADWAL TANAM                     ')
    print('===========================================================')
    tampilkan_jadwal_tanam()
    print('''
        1. Buat Jadwal Tanam
        0. Kembali ke menu''')
    pilih = input('Masukkan Pilihan : ')
    if pilih == '1':
        os.system('cls')
        lanjut_buat_jadwal() 

    elif pilih == '0':
        os.system('cls')
        menu_petani()

    else:
        input('Inputan Invalid, enter untuk ulangi')
        os.system('cls')
        buat_jadwal_tanam()

# ALGORITMA=============================================================================
def merge_sort_tanggal(nama_data):
    if len(nama_data) <= 1:
        return nama_data
    mid = len(nama_data) // 2
    left = merge_sort_tanggal(nama_data[:mid])
    right = merge_sort_tanggal(nama_data[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_data = []
    while left and right:
        if pd.to_datetime(left[0]['tanggal tanam']) <= pd.to_datetime(right[0]['tanggal tanam']):
            sorted_data.append(left.pop(0))
        else:
            sorted_data.append(right.pop(0))
    sorted_data.extend(left or right)
    return sorted_data

def quick_sort(data_list, key):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[len(data_list) // 2][key]
    left = [x for x in data_list if x[key] < pivot]
    middle = [x for x in data_list if x[key] == pivot]
    right = [x for x in data_list if x[key] > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)

def binary_search(data, target):
    hasil = []
    low, high = 0, len(data) - 1
    while low <= high:
        tengah = (low + high) // 2
        tanggal = datetime.strptime(data[tengah]['tanggal tanam'], '%Y-%m-%d')
        if tanggal == target:
            kiri = tengah
            while kiri >= 0 and datetime.strptime(data[kiri]['tanggal tanam'], '%Y-%m-%d') == target:
                hasil.insert(0, kiri)
                kiri -= 1
            kanan = tengah + 1
            while kanan < len(data) and datetime.strptime(data[kanan]['tanggal tanam'], '%Y-%m-%d') == target:
                hasil.append(kanan)
                kanan += 1
            break
        elif tanggal < target:
            low = tengah + 1
        else:
            high = tengah - 1
    return hasil

def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    hasil = []
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return hasil
    while prev < min(step, n):
        if arr[prev] == x:
            hasil.append(prev)
        elif arr[prev] > x:
            break 
        prev += 1
    while step < n:
        if arr[step] == x:
            hasil.append(step)
        elif arr[step] > x:
            break
        step += 1
    return hasil
# ======================================================================================
def lanjut_buat_jadwal():
    os.system('cls')
    tampilkan_jadwal_tanam()
    tanaman = input('Masukkan jenis tanaman yang ingin ditanam : ').title()
    tanggal_tanam = input('Masukkan tanggal tanamnya format (YYYY-MM-DD) : ')
    keterangan = input('Masukkan keterangan : ')
    konfirmasi = input('Apakah anda yakin ingin menambahkan data (y/t) : ').lower()
    while True:
        if konfirmasi == 'y':
            if tanaman == '':
                input('Anda belum menginputkan jenis tanaman')
                os.system('cls')
                lanjut_buat_jadwal()
            try:
                datetime.strptime(tanggal_tanam, '%Y-%m-%d')
            except ValueError:
                input('Format tanggal salah, format (YYYY-MM-DD)')
                os.system('cls')
                lanjut_buat_jadwal()
            if keterangan == '':
                keterangan = '-'
            
            jadwal = pd.read_csv('jadwal_tanam.csv')

            data_baru = pd.DataFrame([{
                'username': usernamelogin,
                'jenis tanaman': tanaman,
                'tanggal tanam': tanggal_tanam,
                'keterangan': keterangan,
                'status': 'Belum Dikerjakan'
            }])

            jadwal = pd.concat([jadwal, data_baru], ignore_index=True)
            data_user = jadwal[jadwal['username'] == usernamelogin].to_dict(orient='records')
            sorting_data_tanggal_user = merge_sort_tanggal(data_user)

            data_lain = jadwal[jadwal['username'] != usernamelogin].to_dict(orient='records')

            semua_data = data_lain + sorting_data_tanggal_user
            semua_file = pd.DataFrame(semua_data)
            semua_file.to_csv('jadwal_tanam.csv', index=False)

            print('Data berhasil ditambahkan')
            input('tekan enter untuk kembali')
            os.system('cls')
            buat_jadwal_tanam()
        elif konfirmasi == 't':
            os.system('cls')
            buat_jadwal_tanam()
        else:
            print('Inputan invalid, ulangi')
            os.system('cls')
            lanjut_buat_jadwal()

def lihat_jadwal_tanam():
    os.system('cls')
    print('=================================================')
    print('                LIHAT JADWAL TANAM               ')
    print('=================================================')
    tampilkan_jadwal_tanam()
    print('''Menu Pencarian:
      1. Cari dari Tanggal
      2. Cari dari Jenis Tanaman
      0. Kembali ke Menu 
    ''')
    pilih = input('Masukkan pilihan: ')
    if pilih == '1':
        os.system('cls')
        cari_dari_tanggal()
    elif pilih == '2':
        os.system('cls')
        cari_dari_tanaman()
    elif pilih == '0':
        os.system('cls')
        menu_petani()
    else:
        input('Inputan invalid, enter untuk ulangi')
        lihat_jadwal_tanam()

def cari_dari_tanggal():
    os.system('cls')
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_jadwal_username = jadwal[jadwal['username'] == usernamelogin]
    data_user = filter_jadwal_username.to_dict(orient='records')
    tampilkan_jadwal_tanam()
    
    while True:
        tanggal_cari = input('Masukkan tanggal yang ingin dicari (YYYY-MM-DD) : ')
        try:
            target_date = datetime.strptime(tanggal_cari, '%Y-%m-%d')
            break
        except ValueError:
            print('Format tanggal tidak sesuai. Gunakan format YYYY-MM-DD.')
    
    hasil = binary_search(data_user, target_date)
    
    if hasil:
        hasil_data = [data_user[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data).drop('username', axis=1)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil)+1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        lihat_jadwal_tanam()
    else:
        print(f'Tidak ditemukan jadwal pada tanggal {tanggal_cari}')
        input('tekan enter untuk kembali')
        os.system('cls')
        lihat_jadwal_tanam()

def cari_dari_tanaman():
    os.system('cls')
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_jadwal_username = jadwal[jadwal['username'] == usernamelogin]
    data_user = filter_jadwal_username.to_dict(orient='records')
    daftar_tanaman = [item['jenis tanaman'] for item in data_user]
    tampilkan_jadwal_tanam()

    tanaman_cari = input('Masukkan nama tanaman yang ingin dicari : ').title()

    hasil = jump_search(daftar_tanaman, tanaman_cari)

    if hasil:
        hasil_data = [data_user[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data).drop('username', axis=1)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil) + 1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        lihat_jadwal_tanam()
    else:
        print(f'Tanaman dengan nama {tanaman_cari} tidak ditemukan.')
        input('tekan enter untuk kembali')
        os.system('cls')
        lihat_jadwal_tanam()

def edit_jadwal_tanam():
    os.system('cls')
    tampilkan_jadwal_tanam()
    print('''
        1. Lanjut Edit Jadwal
        2. Hapus Jadwal
        0. Kembali ke menu''')
    pilih = input('Masukkan Pilihan : ')
    if pilih == '1':
        os.system('cls')
        lanjut_edit()
    elif pilih == '2':
        os.system('cls')
        hapus_jadwal()
    elif pilih == '0':
        os.system('cls')
        menu_petani()
    else:
        input('Inputan Invalid, enter untuk ulangi')
        os.system('cls')
        edit_jadwal_tanam()

def lanjut_edit():
    os.system('cls')
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_jadwal = jadwal[jadwal['username'] == usernamelogin]
    data_user = filter_jadwal.to_dict(orient='records')
    tampilkan_jadwal_tanam()

    try:
        nomor = int(input('Masukkan nomor jadwal yang ingin diedit: '))
    except ValueError:
        input('Input bukan angka, tekan enter untuk kembali.')
        os.system('cls')
        edit_jadwal_tanam()

    if nomor < 1 or nomor > len(data_user):
        input('Nomor tidak valid, tekan enter untuk kembali.')
        os.system('cls')
        edit_jadwal_tanam()

    index_asli = filter_jadwal.index[nomor - 1]
    edit_tanaman = input('Masukkan jenis tanaman : ').title()
    edit_tanggal = input('Masukkan tanggal tanam format (YYYY-MM-DD) : ')
    edit_keterangan = input('Masukkan keterangan : ')
    edit_status = input('Masukkan status (belum dikerjakan, proses, selesai) : ').title()

    if edit_tanaman:
        jadwal.at[index_asli, 'jenis tanaman'] = edit_tanaman
    if edit_tanggal:
        try:
            datetime.strptime(edit_tanggal, '%Y-%m-%d')
            jadwal.at[index_asli, 'tanggal tanam'] = edit_tanggal
        except ValueError:
            input('Format tanggal salah. tekan enter untuk kembali.')
            os.system('cls')
            lanjut_edit()
    if edit_keterangan:
        jadwal.at[index_asli, 'keterangan'] = edit_keterangan
    if edit_status in ['Belum Dikerjakan', 'Proses', 'Selesai']:
        jadwal.at[index_asli, 'status'] = edit_status
    elif edit_status == '':
        input('Status invalid, enter untuk ulangi')
        os.system('cls')
        lanjut_edit()

    data_user = jadwal[jadwal['username'] == usernamelogin].to_dict(orient='records')
    data_lain = jadwal[jadwal['username'] != usernamelogin].to_dict(orient='records')

    data_user_sorted = merge_sort_tanggal(data_user)

    semua_data = data_lain + data_user_sorted
    semua_file = pd.DataFrame(semua_data)
    semua_file.to_csv('jadwal_tanam.csv', index=False)

    print('Jadwal berhasil diperbarui')
    input('tekan enter untuk kembali')
    os.system('cls')
    edit_jadwal_tanam()

def hapus_jadwal():
    os.system('cls')
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_jadwal = jadwal[jadwal['username'] == usernamelogin]
    data_user = filter_jadwal.to_dict(orient='records')
    tampilkan_jadwal_tanam()

    try:
        nomor = int(input('Masukkan nomor jadwal yang ingin dihapus: '))
    except ValueError:
        input('Input bukan angka, tekan enter untuk kembali.')
        os.system('cls')
        edit_jadwal_tanam()

    if nomor < 1 or nomor > len(data_user):
        input('Nomor tidak valid, tekan enter untuk kembali.')
        os.system('cls')
        edit_jadwal_tanam()

    data_user = [data_user[i] for i in range(len(data_user)) if i != (nomor - 1)]
    data_user_sorted = quick_sort(data_user, 'tanggal tanam')
    data_lain = jadwal[jadwal['username'] != usernamelogin].to_dict(orient='records')
    semua_data = data_lain + data_user_sorted
    pd.DataFrame(semua_data).to_csv('jadwal_tanam.csv', index=False)

    input('Jadwal berhasil dihapus, tekan enter untuk kembali.')
    os.system('cls')
    edit_jadwal_tanam()

def tampilkan_pupuk():
    pupuk = pd.read_csv('pupuk.csv')
    if pupuk.empty:
        print('Belum ada rekomendasi pupuk yang tersedia')
    else:
        df_tampil = pupuk.copy()
        print(tabulate(df_tampil, headers=['No'] + list(df_tampil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_tampil) + 1)))

def rekomendasi_pupuk():
    os.system('cls')
    rekomendasi_pupuk_csv()
    print('===================================================')
    print('                REKOMENDASI PUPUK                  ')
    print('===================================================')
    tampilkan_pupuk()
    print('''
        1. Cari pupuk berdasarkan jenis tanaman
        2. Cari pupuk berdasarkan cuaca
        0. Kembali ke Menu
    ''')
    pilih = input('Masukkan Pilihan : ')
    if pilih == '1':
        cari_pupuk_tanam()
    elif pilih == '2':
        cari_pupuk_cuaca()
    elif pilih == '0':
        os.system('cls')
        menu_petani()
    else:
        input('Inputan tidak valid. Silakan coba lagi.')
        os.system('cls')
        rekomendasi_pupuk()

def cari_pupuk_tanam():
    os.system('cls')
    jadwal = pd.read_csv('pupuk.csv')
    data_pupuk = jadwal.to_dict(orient='records')
    daftar_pupuk = [item['jenis tanaman'] for item in data_pupuk]
    tampilkan_pupuk()
    tanaman_cari = input('Masukkan nama tanaman yang ingin dicari : ').title()

    hasil = jump_search(daftar_pupuk, tanaman_cari)

    if hasil:
        hasil_data = [data_pupuk[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil) + 1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        rekomendasi_pupuk()
    else:
        print(f'Tanaman dengan nama {tanaman_cari} tidak ditemukan.')
        input('tekan enter untuk kembali')
        os.system('cls')
        rekomendasi_pupuk()

def cari_pupuk_cuaca():
    os.system('cls')
    jadwal = pd.read_csv('pupuk.csv')
    data_pupuk = jadwal.to_dict(orient='records')
    daftar_pupuk = [item['untuk cuaca'] for item in data_pupuk]
    tampilkan_pupuk()
    tanaman_cari = input('Masukkan cuaca yang ingin dicari : ').title()

    hasil = jump_search(daftar_pupuk, tanaman_cari)

    if hasil:
        hasil_data = [data_pupuk[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil) + 1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        rekomendasi_pupuk()
    else:
        print(f'Tanaman dengan nama {tanaman_cari} tidak ditemukan.')
        input('tekan enter untuk kembali')
        os.system('cls')
        rekomendasi_pupuk()

def tampilkan_riwayat():
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_riwayat = jadwal[(jadwal['username'] == usernamelogin) & (jadwal['status'] == 'Selesai')]
    if filter_riwayat.empty:
        print('Belum ada riwayat tanam yang selesai')
    else:
        jadwal_tampil = filter_riwayat.copy()
        jadwal_tampil = jadwal_tampil.drop('username', axis=1)
        print(tabulate(jadwal_tampil, headers=['No'] + list(jadwal_tampil.columns), tablefmt='fancy_grid', showindex=range(1, len(jadwal_tampil) + 1)))

def riwayat_tanam():
    os.system('cls')
    print('===================================================')
    print('                  RIWAYAT TANAM                    ')
    print('===================================================')
    tampilkan_riwayat()
    print('''
        1. Cari Riwayat dari Tanaman
        2. Cari Riwayat dari Tanggal
        0. Kembali ke menu''')
    pilih = input('Masukkan Pilihan : ')
    if pilih == '1':
        os.system('cls')
        riwayat_dari_tanaman()
    
    elif pilih == '2':
        os.system('cls')
        riwayat_dari_tanggal()
    
    elif pilih == '0':
        os.system('cls')
        menu_petani()
    
    else:
        input('Inputan Invalid ulangi')
        os.system('cls')
        riwayat_tanam()

def riwayat_dari_tanaman():
    os.system('cls')
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_riwayat = jadwal[(jadwal['username'] == usernamelogin) & (jadwal['status'] == 'Selesai')]
    data_user = filter_riwayat.to_dict(orient='records')
    daftar_tanaman = [item['jenis tanaman'] for item in data_user]
    tampilkan_riwayat()

    tanaman_cari = input('Masukkan nama tanaman yang ingin dicari : ').title()

    hasil = jump_search(daftar_tanaman, tanaman_cari)

    if hasil:
        hasil_data = [data_user[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data).drop('username', axis=1)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil) + 1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        riwayat_tanam()
    else:
        print(f'Tanaman dengan nama {tanaman_cari} tidak ditemukan.')
        input('tekan enter untuk kembali')
        os.system('cls')
        riwayat_tanam()

def riwayat_dari_tanggal():
    os.system('cls')
    jadwal = pd.read_csv('jadwal_tanam.csv')
    filter_riwayat = jadwal[(jadwal['username'] == usernamelogin) & (jadwal['status'] == 'Selesai')]
    data_user = filter_riwayat.to_dict(orient='records')
    tampilkan_riwayat()
    
    while True:
        tanggal_cari = input('Masukkan tanggal yang ingin dicari (YYYY-MM-DD) : ')
        try:
            target_date = datetime.strptime(tanggal_cari, '%Y-%m-%d')
            break
        except ValueError:
            print('Format tanggal tidak sesuai. Gunakan format YYYY-MM-DD.')
    
    hasil = binary_search(data_user, target_date)
    
    if len(hasil) > 0:
        hasil_data = [data_user[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data).drop('username', axis=1)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil)+1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        riwayat_tanam()
    else:
        print(f'Tidak ditemukan jadwal pada tanggal {tanggal_cari}')
        input('tekan enter untuk kembali')
        os.system('cls')
        riwayat_tanam()

def tampilkan_laporan():
    laporan = pd.read_csv('laporan.csv')
    filter_laporan = laporan[(laporan['username'] == usernamelogin)]
    if filter_laporan.empty:
        print('Belum ada laporan tanaman')
    else:
        laporan_tampil = filter_laporan.copy()
        laporan_tampil = laporan_tampil.drop('username', axis=1)
        print(tabulate(laporan_tampil, headers=['No'] + list(laporan_tampil.columns), tablefmt='fancy_grid', showindex=range(1, len(laporan_tampil) + 1)))

def laporan_tanam():
    os.system('cls')
    laporan_petani_csv
    print('============================================')
    print('               LAPORAN TANAMAN              ')
    print('============================================')
    tampilkan_laporan()

    jenis_laporan = input('Masukkan jenis laporan (contoh: pertanyaan, keluhan, kesehatan, dsb.) : ').title()
    lapor = input('Masukkan laporan atau pertanyaan : ')
    
    while True:
        konfirmasi = input('Apakah Anda yakin mengajukan laporan (y/t) : ').lower()
        if konfirmasi == 'y':
            file_laporan = pd.read_csv('laporan.csv')
            data_baru = pd.DataFrame([{
                'username': usernamelogin,
                'jenis laporan': jenis_laporan,
                'laporan': lapor,
                'jawaban dan solusi': 'Belum Dijawab',
            }])
            file_laporan = pd.concat([file_laporan, data_baru], ignore_index=True)
            file_laporan.to_csv('laporan.csv', index=False)
            print('Laporan berhasil diajukan.')
            input('tekan enter untuk kembali ke menu.')
            os.system('cls')
            menu_petani() 

        elif konfirmasi == 't':
            os.system('cls')
            menu_petani()  

        else:
            print('Inputan invalid, ulangi')

def edit_profil():
    os.system('cls')
    df = pd.read_csv('akun.csv', dtype={'no telp': str})
    index_user = df[df['username'] == usernamelogin].index
    user_data = df.loc[index_user[0]]

    print(f'Nama Lengkap Lama   : {user_data['nama lengkap']}')
    print(f'Password            : {user_data['password']}')
    print(f'Jenis Kelamin       : {user_data['jenis kelamin']}')
    print(f'Tanggal Lahir       : {user_data['tgl lahir']}')
    print(f'Nomor Telepon       : {user_data['no telp']}')
    print(f'Alamat              : {user_data['alamat']}')

    nama_lengkap = input('Masukkan Nama Baru (enter untuk tetap) : ') or user_data['nama lengkap']
    password = input('Masukkan Password Baru (enter untuk tetap) : ') or user_data['password']
    jenis_kelamin = input('Masukkan Jenis Kelamin (laki-laki/perempuan, enter untuk tetap) : ') or user_data['jenis kelamin']
    tgl_lahir = input('Masukkan Tanggal Lahir (YYYY-MM-DD, enter untuk tetap) : ') or user_data['tgl lahir']
    no_telp = input('Masukkan Nomor Telepon (enter untuk tetap) : ') or user_data['no telp']
    alamat = input('Masukkan Alamat (enter untuk tetap) : ') or user_data['alamat']

    while True:
        konfirmasi = input('Apakah Anda yakin mau mengedit profil (y/t) : ').lower()
        if konfirmasi == 'y':
            try:
                datetime.strptime(tgl_lahir, '%Y-%m-%d')
            except ValueError:
                print('Format atau nilai tanggal lahir tidak valid! Gunakan format (YYYY-MM-DD)')
                input('tekan enter untuk kembali')
                os.system('cls')
                edit_profil()

            if jenis_kelamin.lower() not in ['laki-laki', 'perempuan']:
                print('Jenis kelamin harus laki-laki atau perempuan')
                input('tekan enter untuk kembali')
                os.system('cls')
                edit_profil()
        
            if len(password) < 8:
                print('Password minimal 8 karakter')
                input('tekan enter untuk ulangi')
                os.system('cls')
                edit_profil()

            if not no_telp.isdigit():
                print('Nomor telepon harus berupa angka')
                input('tekan enter untuk kembali')
                os.system('cls')
                edit_profil()
                
            data_baru = pd.DataFrame([{
                'username': usernamelogin,
                'password': password,
                'nama lengkap': nama_lengkap,
                'jenis kelamin': jenis_kelamin,
                'tgl lahir': tgl_lahir,
                'no telp': no_telp,
                'alamat': alamat
            }])

            df = df.drop(index_user[0])
            df = pd.concat([df, data_baru], ignore_index=True)
            df.to_csv('akun.csv', index=False)
            input('Edit profil berhasil, tekan enter untuk kembali')
            os.system('cls')
            menu_petani()

        elif konfirmasi == 't':
            os.system('cls')
            menu_petani()
        
        else:
            print('Inputan invalid, ulangi')

def menu_admin():
    os.system('cls')
    print('=================================================')
    print('                   MENU ADMIN                    ')
    print('=================================================')
    print('''Menu Admin : 
          1. Lihat Jadwal Tanam Petani
          2. Input Data Pupuk
          3. Laporan Petani
          4. Edit Username dan Password
          0. Logout''')
    pilih = input('Masukkan Pilihan : ')
    
    if pilih == '1':
        os.system('cls')
        lihat_jadwal_petani()
                
    elif pilih == '2':
        os.system('cls')
        input_pupuk()
    
    elif pilih == '3':
        os.system('cls')
        laporan_petani()

    elif pilih == '4':
        os.system('cls')
        edit_admin()

    elif pilih == '0':
        while True:
            konfirmasi = input('Apakah yakin Anda ingin keluar (y/t) : ').lower()
            if konfirmasi == 'y':
                os.system('cls')
                menu_utama()
            
            elif konfirmasi == 't':
                os.system('cls')
                menu_admin()
            
            else:
                print('Inputan invalid')
    
    else:
        input('Inputan invalid, enter untuk ulangi')
        os.system('cls')
        menu_admin()

def tampilkan_seluruh_jadwal():
    jadwal = pd.read_csv('jadwal_tanam.csv')
    if jadwal.empty:
        print('Belum ada jadwal yang tersedia')
    else:
        jadwal_tampil = jadwal.copy()
        print(tabulate(jadwal_tampil, headers=['No'] + list(jadwal_tampil.columns), tablefmt='fancy_grid', showindex=range(1, len(jadwal_tampil) + 1)))

def lihat_jadwal_petani():
    os.system('cls')
    jadwal_tanam_csv()
    tampilkan_seluruh_jadwal()
    print('''
        1. Cari berdasarkan username
        0. Kembali ke menu''')
    while True:
        pilih = input('Masukkan Pilihan : ')
        if pilih == '1':
            os.system('cls')
            cari_berdasarkan_username()

        elif pilih == '0':
            os.system('cls')
            menu_admin()

        else:
            print('Inputan invalid, ulangi')

def cari_berdasarkan_username():
    os.system('cls')
    akun = pd.read_csv('jadwal_tanam.csv')
    data_user = akun.to_dict(orient='records')
    daftar_user = [item['username'] for item in data_user]
    tampilkan_seluruh_jadwal()

    user = input('Masukkan nama user yang ingin dicari : ')

    hasil = jump_search(daftar_user, user)

    if hasil:
        hasil_data = [data_user[i] for i in hasil]
        df_hasil = pd.DataFrame(hasil_data)
        print(tabulate(df_hasil, headers=['No'] + list(df_hasil.columns), tablefmt='fancy_grid', showindex=range(1, len(df_hasil) + 1)))
        input('Jadwal ditemukan, tekan enter untuk kembali')
        os.system('cls')
        lihat_jadwal_petani()
    else:
        print(f'Tanaman dengan nama {user} tidak ditemukan.')
        input('tekan enter untuk kembali')
        os.system('cls')
        lihat_jadwal_petani()

def input_pupuk():
    os.system('cls')
    rekomendasi_pupuk_csv()
    tampilkan_pupuk()
    print('''
        1. Tambah data Pupuk
        2. Hapus data Pupuk
        0. Kembali ke menu''')
    while True:
        pilih = input('Masukkan Pilihan : ')
        if pilih == '1':
            os.system('cls')
            lanjut_pupuk()

        elif pilih == '2':
            os.system('cls')
            hapus_data_pupuk()

        elif pilih == '0':
            os.system('cls')
            menu_admin()

        else:
            print('Inputan invalid, ulangi')

def lanjut_pupuk():
    os.system('cls')
    laporan_petani_csv()
    tampilkan_pupuk()
    jenis_tanaman = input('Masukkan jenis tanaman untuk pupuk : ')
    untuk_cuaca = input('Masukkan cuaca yang cocok : ')
    pupuk = input('Masukkan pupuk yang cocok : ')
    saran = input('Masukkan saran yang cocok : ')
    while True:
        konfirmasi = input('Apakah data pupuk sudah benar (y/t) : ')
        if konfirmasi == 'y':
            file_laporan = pd.read_csv('pupuk.csv')
            data_baru = pd.DataFrame([{
                'jenis tanaman': jenis_tanaman,
                'untuk cuaca': untuk_cuaca,
                'pupuk yang cocok': pupuk,
                'saran': saran
            }])

            file_laporan = pd.concat([file_laporan, data_baru], ignore_index=True)
            sorted_list = quick_sort(file_laporan.to_dict(orient='records'), 'jenis tanaman')
            sorted_df = pd.DataFrame(sorted_list)
            sorted_df.to_csv('pupuk.csv', index=False)

            print('Pupuk berhasil berhasil titambahkan.')
            input('tekan enter untuk kembali ke menu.')
            os.system('cls')
            input_pupuk()
        
        elif konfirmasi == 't':
            os.system('cls')
            input_pupuk()
        
        else:
            print('Inputan invalid, ulangi')

def hapus_data_pupuk():
    pupuk = pd.read_csv('pupuk.csv')
    data_pupuk= pupuk.to_dict(orient='records')
    tampilkan_pupuk()
    try:
        nomor = int(input('Masukkan nomor jadwal yang ingin dihapus: '))
    except ValueError:
        input('Input bukan angka, tekan enter untuk kembali.')
        os.system('cls')
        input_pupuk()

    if nomor < 1 or nomor > len(data_pupuk):
        input('Nomor tidak valid, tekan enter untuk kembali.')
        os.system('cls')
        input_pupuk()

    data_pupuk = [data_pupuk[i] for i in range(len(data_pupuk)) if i != (nomor - 1)]
    data_pupuk_sorted = quick_sort(data_pupuk, 'jenis tanaman')
    pd.DataFrame(data_pupuk_sorted).to_csv('pupuk.csv', index=False)

    input('Jadwal berhasil dihapus, tekan enter untuk kembali.')
    os.system('cls')
    input_pupuk()

def tampilkan_seluruh_laporan():
    laporan = pd.read_csv('laporan.csv')
    if laporan.empty:
        print('Belum ada laporan yang tersedia')
    else:
        laporan_tampil = laporan.copy()
        print(tabulate(laporan_tampil, headers=['No'] + list(laporan_tampil.columns), tablefmt='fancy_grid', showindex=range(1, len(laporan_tampil) + 1)))

def laporan_petani():
    os.system('cls')
    laporan = pd.read_csv('laporan.csv')
    data_laporan = laporan.to_dict(orient='records')
    tampilkan_seluruh_laporan()
    try:
        nomor = int(input('Masukkan nomor laporan yang ingin dijawab : '))
    except ValueError:
        input('Input bukan angka, tekan enter untuk kembali')
        os.system('cls')
        menu_admin()

    if nomor < 1 or nomor > len(data_laporan):
        input('Nomor laporan tidak valid. tekan enter untuk kembali.')
        os.system('cls')
        menu_admin()

    jawaban = input('Masukkan jawaban dan solusi untuk laporan ini : ')

    while True:
        konfirmasi = input('Apakah yakin ingin menjawab (y/t) : ').lower()
        if konfirmasi == 'y':
            laporan.at[nomor - 1, 'jawaban dan solusi'] = jawaban
            laporan.to_csv('laporan.csv', index=False)
            print('Jawaban berhasil disimpan.')
            input('tekan enter untuk kembali ke menu.')
            os.system('cls')
            menu_admin()

        elif konfirmasi == 't':
            os.system('cls')
            menu_admin()

        else:
            print('Input invalid, ulangi')

def edit_admin():
    os.system('cls')
    admin = pd.read_csv('admin.csv')
    admin_data = admin.loc[0]
    print(f'Username saat ini : {admin_data["username"]}')
    print(f'Password saat ini : {admin_data["password"]}')

    username = input('Masukkan username baru (Enter untuk tetap) : ') or admin_data['username']
    password = input('Masukkan password baru (Enter untuk tetap) : ') or admin_data['password']
    while True:
        konfirmasi = input('Apakah Anda yakin mengubah data admin ini (y/t) : ').lower()
        if konfirmasi == 'y':
            admin.at[0, 'username'] = username
            admin.at[0, 'password'] = password
            admin.to_csv('admin.csv', index=False)
            print('Akun admin berhasil diperbarui.')
            input('Tekan Enter untuk kembali ke menu.')
            os.system('cls')
            menu_admin()

        elif konfirmasi == 't':
            os.system('cls')
            menu_admin()

        else:
            print('Input invalid, ulangi')

menu_utama()
