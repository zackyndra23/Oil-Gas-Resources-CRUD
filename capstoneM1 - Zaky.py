# Zaky Indra Satria Putra
# JCDS  0406 008
# Program CRUD Sumber Daya MIGAS

# Library yang dipakai
from tabulate import tabulate
from colorama import init
from termcolor import colored
import os
import time
init()

# Pendefinisian variabel bertipe dictionary dalam list
listMigas = [
    {
        'Perusahaan': 'Moon Energy',
        'Wilayah Indonesia': 'Barat',
        'Status': 'Lead',
        'Lapangan': 'MINYAK BUMI',
        'Jumlah': 79
    },
    {
        'Perusahaan': 'Bukit Berbaris',
        'Wilayah Indonesia': 'Barat',
        'Status': 'Discovery',
        'Lapangan': 'MINYAK BUMI',
        'Jumlah': 52
    },
    {
        'Perusahaan': 'Boolean Petroleum',
        'Wilayah Indonesia': 'Tengah',
        'Status': 'Prospect',
        'Lapangan': 'MINYAK BUMI',
        'Jumlah': 87
    },
    {
        'Perusahaan': 'Selebew Ltd.',
        'Wilayah Indonesia': 'Timur',
        'Status': 'Discovery',
        'Lapangan': 'GAS ALAM',
        'Jumlah': 103
    },
    {
        'Perusahaan': 'Pernah Minat',
        'Wilayah Indonesia': 'Barat',
        'Status': 'Dry',
        'Lapangan': 'MIGAS',
        'Jumlah': 87
    },
    {
        'Perusahaan': 'Bukit Berbaris',
        'Wilayah Indonesia': 'Tengah',
        'Status': 'Dry',
        'Lapangan': 'GAS ALAM',
        'Jumlah': 54
    },
    {
        'Perusahaan': 'Moon Energy',
        'Wilayah Indonesia': 'Timur',
        'Status': 'Dry',
        'Lapangan': 'MIGAS',
        'Jumlah': 15
    },
    {
        'Perusahaan': 'Selebew Ltd.',
        'Wilayah Indonesia': 'Tengah',
        'Status': 'Lead',
        'Lapangan': 'MIGAS',
        'Jumlah': 138
    },
    {
        'Perusahaan': 'Pernah Minat',
        'Wilayah Indonesia': 'Tengah',
        'Status': 'Discovery',
        'Lapangan': 'MIGAS',
        'Jumlah': 107
    },
    {
        'Perusahaan': 'Boolean Petroleum',
        'Wilayah Indonesia': 'Timur',
        'Status': 'Lead',
        'Lapangan': 'GAS ALAM',
        'Jumlah': 52
    },
]

# Fungsi menampilkan menu utama
def hi():
    os.system('cls')
    time.sleep(0.3)
    print(f'''
    Selamat Datang di Database Sumberdaya MIGAS Indonesia

    List Menu :
     1. Daftar dan Laporan sumberdaya MIGAS
     2. Tambah Sumberdaya
     3. Update Sumberdaya
     4. Menghapus Data Pelaporan Sumberdaya
     5. Analisis Sumberdaya
     6. Keluar Program
    ''')

# Fungsi pilihan opsi inputan
def pilih_opsi():
    option = int(input(colored('Masukkan Pilihan Anda: ', 'yellow')))
    return option

# Fungsi kembali ke menu sebelumnya atau menu utama
def kembali():
    back = str(input(colored('\nKembali ke menu sebelumnya (Y/N)? ', 'yellow')).capitalize())
    return back

#
def simpan():
    confirm = str(input(colored('\nApakah Anda Ingin Menyimpannya (Y/N)? ', 'yellow')).capitalize())
    return confirm

def menu1():
    os.system('cls')
    print(colored('''
          ================ Menu #1: Daftar dan Laporan Sumberdaya) ==================
    ''', 'blue'))
    time.sleep(0.3)
    print(tabulate(indexed_data, headers='keys', tablefmt = 'github'))

def menu2():
    os.system('cls')
    time.sleep(0.6)
    print(colored('          ================ Menu #2: Tambah Sumberdaya ==================', 'blue'))

def menu3():
    os.system('cls')
    time.sleep(0.6)
    print(colored('          ================ Menu #3: Update Sumberdaya ==================', 'blue'))

def menu4():
    os.system('cls')
    time.sleep(0.6)
    print(colored('          ================ Menu #4: Menghapus Data Pelaporan Sumberdaya ==================', 'blue'))

def menu5():
    os.system('cls')
    time.sleep(0.6)
    print(colored('          ================ Menu #5: Analisis Sumberdaya ==================', 'blue'))

def cek_int(index):
    hsl = index.isdigit()
    return hsl

def update():
    time.sleep(0.3)
    while True:
        os.system('cls')
        menu3()
        print(tabulate(indexed_data, headers='keys', tablefmt = 'github'))
        index_sdm = input(colored('\nMasukkan Index Sumberdaya yang Ingin Diupdate: ', 'yellow'))
        index_sdm1 = cek_int(index_sdm)
        if(index_sdm == ''):
            print(colored('\nInvalid! Masukkan Index Yang Tersedia Dalam Daftar', 'red'))
            time.sleep(1)
            continue
        elif(index_sdm1 == False):
            print(colored('\nInvalid! Masukkan Index Yang Tersedia Dalam Daftar', 'red'))
            time.sleep(1)
            continue
        elif(int(index_sdm) > len(listMigas) or int(index_sdm) <= 0):
            print(colored('\nInvalid! Masukkan Index Yang Tersedia Dalam Daftar', 'red'))
            time.sleep(1)
            continue
        else:
            statusNew = str(input(colored('\nMasukkan Status Sumberdaya Baru (Lead/Prospect/Discovery/Dry): ', 'yellow')).capitalize())
            lapanganNew = str(input(colored('\nMasukkan Jenis Lapangan Sumberdaya Baru (Minyak Bumi / Gas Alam / MIGAS): ', 'yellow')).upper())
            jumlahNew = int(input(colored('\nMasukkan Jumlah Sumberdaya Baru : ', 'yellow')))
            confirm = simpan()
            if(confirm == 'Y'):
                listMigas[int(index_sdm)-1]['Status'] = statusNew
                listMigas[int(index_sdm)-1]['Lapangan'] = lapanganNew
                listMigas[int(index_sdm)-1]['Jumlah'] = jumlahNew
                print(colored('Data Berhasil Disimpan', 'green'))
                time.sleep(1)
                break
            else:
                print(colored('Data Tidak Disimpan', 'red'))
                time.sleep(1)
                break

def hapus():
    time.sleep(0.3)
    while True:
        os.system('cls')
        menu4()
        print(tabulate(indexed_data, headers='keys', tablefmt = 'github'))
        index_sdm = input(colored('\nMasukkan Index Sumberdaya yang Ingin Diupdate: ', 'yellow'))
        index_sdm1 = cek_int(index_sdm)
        if(index_sdm == ''):
            print(colored('\nInvalid! Masukkan Index Yang Tersedia Dalam Daftar', 'red'))
            time.sleep(1)
            continue
        elif(index_sdm1 == False):
            print(colored('\nInvalid! Masukkan Index Yang Tersedia Dalam Daftar', 'red'))
            time.sleep(1)
            continue
        elif(int(index_sdm) > len(listMigas) or int(index_sdm) <= 0):
            print(colored('\nInvalid! Masukkan Index Yang Tersedia Dalam Daftar', 'red'))
            time.sleep(1)
            continue
        else:
            confirm = simpan()
            if(confirm == 'Y'):
                del listMigas[int(index_sdm)-1]
                print(colored('Data Berhasil Dihapus dan Disimpan', 'green'))
                time.sleep(1)
                break
            else:
                print(colored('Data Tidak Disimpan', 'red'))
                time.sleep(1)
                break

index_brt = []; index_tgh = []; index_tmr = []; jml_brt = 0; jml_tgh = 0; jml_tmr = 0
jumlah_brt = []; jumlah_tgh = []; jumlah_tmr = []

def scan_jumlah(list, index, sum, count, inisial, values, final):
    index = []; sum = []
    # count = 0
    for i in range(len(list)):
        if(list[i][inisial] == values):
            index.append(i)
        else:
            continue
    for i in index:
        sum.append(list[i][final])
    for i in sum:
        count += i
    print(count)
    return count

while True:
    hi()
    indexed_data = [{"Index": 'SKK-N23-0'+ str(i+1), **row} for i, row in enumerate(listMigas)]
    pilihan = input(colored('Masukkan angka menu yang ingin dijalankan: ', 'yellow'))
    if(pilihan == '1'):
        while True:
            menu1()
            pilihan = kembali()
            if(pilihan == 'Y'):
                break
            else:
                continue

    elif(pilihan == '2'):
        while True:
            menu2()
            while True:
                addPerusahaan = str(input(colored('\nMasukkan Nama Perusahaan : ', 'yellow')).title())
                if(addPerusahaan == ''):
                    os.system('cls')
                    menu2()
                    time.sleep(0.3)
                    continue
                else:
                    print(colored('Berhasil diinput', 'green'))

                os.system('cls')
                time.sleep(0.3)
                addIDN = ''
                while True:
                    menu2()
                    print('''
Sumberdaya terletak pada Indonesia bagian:
 1. Barat
 2. Tengah
 3. Timur
                    ''')
                    wilayahIDN = input(colored('Masukkan letak sumberdaya yang ingin ditambahkan (1-3):', 'yellow'))
                    if(wilayahIDN == '1'):
                        addIDN = 'Barat'
                    elif(wilayahIDN == '2'):
                        addIDN = 'Tengah'
                    elif(wilayahIDN == '3'):
                        addIDN = 'Timur'
                    else:
                        os.system('cls')
                        print(colored('\nInput salah! Silahkan masukkan sesuai opsi (1-3)', 'red'))
                        time.sleep(1)
                        continue
       
                    os.system('cls')
                    time.sleep(0.3)
                    addStatus = ''
                    while True:
                        menu2()
                        print('''
Status sumber daya yang ingin ditambahkan:
 1. Prospect
 2. Lead
 3. Discovery
 4. Dry
                        ''')
                        status = input(colored('Masukkan status sumberdaya yang ingin ditambahkan : ', 'yellow'))
                        if(status == '1'):
                            addStatus = 'Prospect'
                        elif(status == '2'):
                            addStatus = 'Lead'
                        elif(status == '3'):
                            addStatus = 'Discovery'
                        elif(status == '4'):
                            addStatus = 'Dry'
                        else:
                            os.system('cls')
                            print(colored('\nInput salah! Silahkan masukkan sesuai opsi (1-4)', 'red'))
                            time.sleep(1)
                            continue

                        os.system('cls')
                        time.sleep(0.3)
                        addLapangan = ''
                        while True:
                            menu2()
                            print('''
Lapangan sumberdaya berupa:
 1. Minyak Bumi
 2. Gas Alam
 3. MIGAS
                            ''')
                            lapangan = str(input(colored('Masukkan jenis sumberdaya yang terindikasi (1-3): ', 'yellow')).upper())
                            if(lapangan == '1'):
                                addLapangan = 'MINYAK BUMI'
                            elif(lapangan == '2'):
                                addLapangan = 'GAS ALAM'
                            elif(lapangan == '3'):
                                addLapangan = 'MIGAS'
                            else:
                                os.system('cls')
                                print(colored('\nInput salah! Silahkan masukkan sesuai opsi (1-3)', 'red'))
                                time.sleep(1)
                                continue
                            
                            os.system('cls')
                            time.sleep(0.3)
                            while True:
                                os.system('cls')
                                menu2()
                                time.sleep(0.6)
                                addJumlah = input(colored('\nMasukkan jumlah sumberdaya: ', 'yellow'))
                                if(addJumlah.isdigit() == False):
                                    print(colored('\nMasukkan tidak valid, silahkan masukkan bilangan bulat', 'red'))
                                    time.sleep(0.6)
                                    continue
                                else:
                                    listMigas.append({
                                            'Perusahaan': addPerusahaan,
                                            'Wilayah Indonesia': addIDN,
                                            'Status': addStatus,
                                            'Lapangan': addLapangan,
                                            'Jumlah': addJumlah
                                    })
                                    menu1()
                                    pilihan = simpan()
                                    if(pilihan != 'Y'):
                                        del listMigas[-1]
                                    elif(pilihan == 'Y'):
                                        print(colored('Data Sumberdaya Berhasil ditambahkan!', 'green'))
                                        time.sleep(1)
                                        break
                                    break
                                break
                            break
                        break
                    break
                break
            break

    elif(pilihan == '3'):
        update()

    elif(pilihan == '4'):
        hapus()

    elif(pilihan == '5'):
        os.system('cls')
        time.sleep(0.3)
        print('''
List Analisis :
 1. Jumlah Lapangan di Setiap Wilayah
 2. Succes Index
 3. Tabel Analisis
 4. Kembali ke Menu Utama
    ''')
        while True:
            pilihan = input(colored('Masukkan Opsi Analisis yang Ingin Dijalankan (1-4): ', 'yellow'))
            listUrut_wyh = sorted(indexed_data, key=lambda x: x['Wilayah Indonesia'])
            if(pilihan == '1'):
                jml_brt2 = scan_jumlah(listMigas, index_brt, jumlah_brt, jml_brt, 'Wilayah Indonesia', 'Barat', 'Jumlah' )
                jml_tgh2 = scan_jumlah(listMigas, index_tgh, jumlah_tgh, jml_tgh, 'Wilayah Indonesia', 'Tengah', 'Jumlah' )
                jml_tmr2 = scan_jumlah(listMigas, index_tmr, jumlah_tmr, jml_tmr, 'Wilayah Indonesia', 'Timur', 'Jumlah' )

                while True:
                    os.system('cls')
                    time.sleep(0.6)
                    menu5()
                    print(tabulate(listUrut_wyh, headers='keys', tablefmt = 'github'))
                    print(colored(f'''
Analisis yang Didapat:
 1. Wilayah Indonesia bagian Barat memiliki jumlah Sumberdaya MIGAS sebanyak {jml_brt2}
 2. Wilayah Indonesia bagian Tengah memiliki jumlah Sumberdaya MIGAS sebanyak {jml_tgh2}
 3. Wilayah Indonesia bagian Timur memiliki jumlah Sumberdaya MIGAS sebanyak {jml_tmr2}
                    ''', 'green'))
                    pilihan = kembali()
                    if(pilihan != 'Y'):
                        continue
                    else:
                        break
                    break
                break

            elif(pilihan == '2'):
                index_suc = []; jumlah_dis = []; jml_dis = 0
                index_dry = []; jumlah_dry = []; jml_dry = 0
                dis_success = scan_jumlah(listMigas, index_suc, jumlah_dis, jml_dis, 'Status', 'Discovery', 'Jumlah' )
                dry_success = scan_jumlah(listMigas, index_dry, jumlah_dry, jml_dry, 'Status', 'Dry', 'Jumlah' )
                idx_suc = (dis_success/(dis_success+dry_success)) * 100
                listUrut_stat = sorted(indexed_data, key=lambda x: x['Status'])

                while True:
                    os.system('cls')
                    time.sleep(0.6)
                    menu5()
                    print(tabulate(listUrut_stat, headers='keys', tablefmt = 'github'))
                    print(colored(f'''
Success index sumberdaya Minyak Bumi dan Gas Alam (MIGAS) Indonesia sebesar {idx_suc} %
                    ''', 'green'))
                    pilihan = kembali()
                    if(pilihan != 'Y'):
                        continue
                    else:
                        break
                    break
                break

            elif(pilihan == '3'):
                while True:
                    os.system('cls')
                    time.sleep(0.3)
                    print('''
List Analisis :
 1. Urutan Berdasarkan Perusahaan
 2. Urutan Berdasarkan Wilayah Indonesia
 3. Urutan Berdasarkan Status
 4. Urutan Berdasarkan Lapangan
 5. Kembali ke Menu Utama
                    ''')
                    pilihan = input(colored('Masukkan Opsi Analisis yang Ingin Dijalankan (1-4): ', 'yellow'))
                    listUrut_pers = sorted(indexed_data, key=lambda x: x['Perusahaan'])
                    listUrut_lap = sorted(indexed_data, key=lambda x: x['Lapangan'])
                    listUrut_stat = sorted(indexed_data, key=lambda x: x['Status'])
                    while True:
                        if(pilihan == '1'):
                            os.system('cls')
                            time.sleep(0.3)
                            while True:
                                time.sleep(0.3)
                                print(colored('          ================ Menu #5.1: Tabel Analisis (Perusahaan) ==================', 'blue'))
                                print(tabulate(listUrut_pers, headers='keys', tablefmt = 'github'))
                                pilihan = kembali()
                                if(pilihan != 'Y' or pilihan == ''):
                                    continue
                                else:
                                    break
                                break
                            break
                        if(pilihan == '2'):
                            os.system('cls')
                            time.sleep(0.3)
                            while True:
                                time.sleep(0.3)
                                print(colored('          ================ Menu #5.1: Tabel Analisis (Wilayah Indonesia) ==================', 'blue'))
                                print(tabulate(listUrut_wyh, headers='keys', tablefmt = 'github'))
                                pilihan = kembali()
                                if(pilihan != 'Y' or pilihan == ''):
                                    continue
                                else:
                                    break
                                break
                            break
                        if(pilihan == '3'):
                            os.system('cls')
                            time.sleep(0.3)
                            while True:
                                time.sleep(0.3)
                                print(colored('          ================ Menu #5.1: Tabel Analisis (Status) ==================', 'blue'))
                                print(tabulate(listUrut_stat, headers='keys', tablefmt = 'github'))
                                pilihan = kembali()
                                if(pilihan != 'Y' or pilihan == ''):
                                    continue
                                else:
                                    break
                                break
                            break
                        if(pilihan == '4'):
                            os.system('cls')
                            time.sleep(0.3)
                            while True:
                                time.sleep(0.3)
                                print(colored('          ================ Menu #5.1: Tabel Analisis (Lapangan) ==================', 'blue'))
                                print(tabulate(listUrut_lap, headers='keys', tablefmt = 'github'))
                                pilihan = kembali()
                                if(pilihan != 'Y' or pilihan == ''):
                                    continue
                                else:
                                    break
                                break
                            break
                        if(pilihan == '5'):
                            break
                        break
                    break
                break
            break

    elif(pilihan == '6'):
        exit()
    else:
        os.system('cls')
        print(colored('\nInput salah! Silahkan masukkan sesuai opsi (1-6)', 'red'))
        time.sleep(1)
        continue                 

                # os.system('cls')
                # time.sleep(0.6)
                # print(colored('          ================ Menu #5: Analisis Sumberdaya ==================', 'blue'))




