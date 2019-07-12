#!/usr/bin/python3


'''
Mathool - Math Tools Termux
This project was created by Dfv47 with Black Coder Crush. 
Copyright 11 - 06 - 2k19 @m_d4fv
'''

try:
        import os,sys,math
except Exception as F:
        exit("[ModuleErr] %s"%(F))
if sys.version[0] in '2':
        exit("[sorry] use python version 3")

# Color
n='\033[0;00m' #normal
a='\033[1;30m' #grey
r='\033[1;31m' #red
g='\033[1;32m' #green
y='\033[1;33m' #yellow
b='\033[1;34m' #blue
p='\033[1;35m' #purple
c='\033[1;36m' #cyan
w='\033[1;37m' #white
br='\033[91;7m' #bgred

def banner(): 
    print (c+52*"-") 
    print (g+" 8b    d8    db  888888 88  88  "+r+"v.1.5") 
    print (g+" 88b  d88   dPYb   88   88  88  "+y+"* "+w+"Author  "+y+":"+w+" Dfv47") 
    print (g+" 88YbdP88  dP__Yb  88   888888  "+y+"* "+w+"Version "+y+":"+w+" Python") 
    print (g+" 88 YY 88 dP''''Yb 88   88  88  "+w+"Mathematics "+y+"- "+w+"Tools") 
    print (c+52*"-") 

def awal():
    print (b+"  ["+w+"01"+b+"] "+w+"Penjumlahan          "+b+"["+w+"07"+b+"] "+w+"Bangun Datar")
    print (b+"  ["+w+"02"+b+"] "+w+"Pengurangan          "+b+"["+w+"08"+b+"] "+w+"Bangun Ruang")
    print (b+"  ["+w+"03"+b+"] "+w+"Perkalian            "+b+"["+w+"09"+b+"] "+w+"Bilangan Prima")
    print (b+"  ["+w+"04"+b+"] "+w+"Pembagian            "+b+"["+w+"10"+b+"] "+w+"Faktor Bilangan")
    print (b+"  ["+w+"05"+b+"] "+w+"Persentase           "+b+"["+w+"11"+b+"] "+w+"Pangkat Tiga")
    print (b+"  ["+w+"06"+b+"] "+w+"Pangkat Dua          ")
    print (r+"  ["+w+"00"+r+"] "+w+"Tentang              "+r+"["+w+"99"+r+"] "+w+"Keluar")

def tentang():
    os.system('clear')
    banner()
    print (b+"  * "+w+"Mathematic project in python script ")
    print (b+'\n  ['+w+'+'+b+'] '+w+'Coded  '+b+':'+w+' @m_d4fv')
    print (b+'  ['+w+'+'+b+'] '+w+'Author '+b+':'+w+' Dfv47')
    print (b+'  ['+w+'+'+b+'] '+w+'Team   '+b+':'+w+' Black Coder Crush')
    print (b+'  ['+w+'+'+b+'] '+w+'Phone  '+b+':'+w+' 6282223108828')
    print (b+'  ['+w+'+'+b+'] '+w+'Email  '+b+':'+w+' daffamfthhsn21@gmail.com')
    print (b+'  ['+w+'+'+b+'] '+w+'Thanks '+b+':'+w+' ZoneExploiter, CytoXploit')


def main():
    try:
        daf = input(w+'\n['+y+'>'+w+'] Pilih '+y+': ')
        if daf =='daffa':
            main()
        elif daf == '01' or daf == '1' :
            jumlah()
        elif daf == '02' or daf == '2' :
            kurang() 
        elif daf == '03' or daf == '3' :
            kali() 
        elif daf == '04' or daf == '4' :
            bagi() 
        elif daf == '05' or daf == '5' :
            persen() 
        elif daf == '06' or daf == '6' :
            pangkatdua()
        elif daf == '11' :
            pangkattiga()
        elif daf == '07' or daf == '7' :
            pilbangundatar()
        elif daf == '08' or daf == '8' :
            pilbangunruang()
        elif daf == '09' or daf == '9' :
            prima()
        elif daf == '10' :
            bilangan()
        elif daf == '99' :
            exit()
        elif daf == '00' :
            tentang()
        else:
            if daf [0:4] == '':
                    print ("")
                    print ("     "+br+"[!] command '"+daf+"' not found"+n+"") 
                    print ('     '+br+'[!] type "help" to show command'+n+'') 
                    print ("")
                    main()
            else:
                    print ("")
                    print ("     "+br+"[!] command '"+daf+"' not found"+n+"") 
                    print ('     '+br+'[!] type "help" to show command'+n+'') 
                    print ("")
                    main()
    
    except Exception as e:
           print(e)
    except KeyboardInterrupt:
        print ("") 
        print ("") 
        print ("      "+y+"("+r+" Ctrl + C "+y+")"+r+" Detected"+n+"") 
        print ("       "+r+"["+y+"!"+r+"] "+y+"Program Exiting...") 
        print ("       "+r+"["+y+"!"+r+"] "+y+"Thanks For Using DfvXploit")            

#Penjumlahan
def jumlah(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Penjumlahan') 
    ab= float(input(b+'['+w+'+'+b+'] '+w+'Angka pertama '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'+'+b+'] '+w+'Angka kedua   '+b+':'+w+' ')) 
    jumlah = ab+cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil         '+b+':'+w,jumlah) 
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pengurangan
def kurang(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Pengurangan')   
    ab= float(input(b+'['+w+'-'+b+'] '+w+'Angka pertama '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'-'+b+'] '+w+'Angka kedua   '+b+':'+w+' ')) 
    kurang = ab-cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil         '+b+':'+w,kurang) 
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Perkalian
def kali(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Perkalian')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Angka pertama '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Angka kedua   '+b+':'+w+' ')) 
    kali = ab*cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil         '+b+':'+w,kali) 
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()
   
#Pembagian
def bagi(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Pembagian')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Angka pertama '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Angka kedua   '+b+':'+w+' ')) 
    bagi = ab/cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil         '+b+':'+w,bagi) 
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()
    
#Persentase
def persen(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Persentase')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Masukkan angka '+b+':'+w+' ')) 
    persen = ab*100
    print (b+'['+w+'#'+b+'] '+w+'Hasil          '+b+':'+w,persen)
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()
    
#Pangkat Dua
def pangkatdua(): 
   os.system('clear') 
   banner() 
   print(b+'\n['+w+'#'+b+'] '+w+'Pangkat Dua')   
   ab= float(input(b+'['+w+'*'+b+'] '+w+'Masukkan angka '+b+':'+w+' ')) 
   pangdua = ab*ab
   print (b+'['+w+'#'+b+'] '+w+'Hasil          '+b+':'+w,pangdua)
   input(w+"\n["+y+"?"+w+"] Press enter to menu...")
   os.system('clear')
   start()
   
#Pangkat_Tiga
def pangkattiga(): 
   os.system('clear') 
   banner() 
   print(b+'\n['+w+'#'+b+'] '+w+'Pangkat tiga')   
   ab= float(input(b+'['+w+'*'+b+'] '+w+'Masukkan angka '+b+':'+w+' ')) 
   pangtiga = ab*ab*ab
   print (b+'['+w+'#'+b+'] '+w+'Hasil          '+b+':'+w,pangtiga)
   input(w+"\n["+y+"?"+w+"] Press enter to menu...")
   os.system('clear')
   start()
   
#Pilihan_bangun_datar
def pilbangundatar() :	
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Persegi           "+b+"["+w+"05"+b+"] "+w+"Jajar Genjang")
    print (b+"  ["+w+"02"+b+"] "+w+"Persegi panjang   "+b+"["+w+"06"+b+"] "+w+"Trapesium")
    print (b+"  ["+w+"03"+b+"] "+w+"Segitiga          "+b+"["+w+"07"+b+"] "+w+"Belah Ketupat")
    print (b+"  ["+w+"04"+b+"] "+w+"Lingkaran         "+b+"["+w+"08"+b+"] "+w+"Layang Layang")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar '+y+': ')
    if df == '01' or df == '1' :
        persegi()
    elif df == '02' or df == '2' :
        persegi_panjang()
    elif df == '03' or df == '3' :
        segitiga()
    elif df == '04' or df == '4' :
        luas_lingkaran()
    elif df == '05' or df == '5' :
        jajargenjang()
    elif df == '06' or df == '6' :
        trapesium()
    elif df == '07' or df == '7' :
        belah_ketupat()
    elif df == '08' or df == '8' :
        layang_layang()
    else :
        start()

#Pilihan_persegi
def persegi():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas persegi ")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling persegi ")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+'Persegi'+y+' : ')
    if df == '01' or df == '1' :
        luas_persegi()
    elif df == '02' or df == '2' :
        keliling_persegi()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
        
#Luas_persegi
def luas_persegi() :
    os.system('clear') 
    banner() 
    print (b+'\n['+w+'#'+b+'] '+w+'Luas persegi')   
    x= float(input(b+'['+w+'*'+b+'] '+w+'Panjang sisi  '+b+':'+w+' ')) 
    luas= x*x
    print (b+'['+w+'#'+b+'] '+w+'Hasil         '+b+':'+w, luas, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Keliling_persegi
def keliling_persegi() :
    os.system('clear') 
    banner() 
    print (b+'\n['+w+'#'+b+'] '+w+'Keliling persegi')     
    x= float(input(b+'['+w+'*'+b+'] '+w+'Panjang sisi  '+b+':'+w+' ')) 
    keliling = 4*x
    print (b+'['+w+'#'+b+'] '+w+'Hasil         '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()
    
#Pilihan_persegi_panjang
def persegi_panjang():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas persegi panjang ")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling persegi panjang ")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+'Persegi panjang'+y+' : ')
    if df == '01' or df == '1' :
        luas_persegipanjang()
    elif df == '02' or df == '2' :
        keliling_persegipanjang()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
       
#Luas_persegi_panjang
def luas_persegipanjang(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas persegi panjang')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang sisi '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Lebar sisi   '+b+':'+w+' ')) 
    luas = ab*cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Keliling_persegi_panjang
def keliling_persegipanjang () :
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Kelilig persegi panjang')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang sisi '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Lebar sisi   '+b+':'+w+' ')) 
    keliling = 2*(ab+cd)
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan_segitiga
def segitiga():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas segitiga ")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling segitiga ")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+'Segitiga'+y+' : ')
    if df == '01' or df == '1' :
        luas_segitiga()
    elif df == '02' or df == '2' :
        keliling_segitiga()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()

#Luas_segitiga
def luas_segitiga(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas segitiga')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Alas        '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Tinggi      '+b+':'+w+' ')) 
    luas=0.5*ab*cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Kelilig_segitiga
def keliling_segitiga(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Kelilig segitiga')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang AB  '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Panjang BC  '+b+':'+w+' ')) 
    ca= float(input(b+'['+w+'*'+b+'] '+w+'Panjang CA  '+b+':'+w+' '))    
    keliling = ab+bc+ca
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()
    
#Lingkaran
def luas_lingkaran(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas Lingkaran')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Jari-jari   '+b+':'+w+' ')) 
    luas = 22/7*ab*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan jajargenjang    
def jajargenjang():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas jajargenjang ")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling jajargenjang ")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+' jajargenjang'+y+' : ')
    if df == '01' or df == '1' :
        luas_jajargenjang()
    elif df == '02' or df == '2' :
        keliling_jajargenjang()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
    
#Luas_jajargenjang
def luas_jajargenjang(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas Jajargenjang')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Tinggi     '+b+':'+w+' ')) 
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Alas       '+b+':'+w+' '))    
    luas = ab*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil      '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Keliling_jajargenjang
def keliling_jajargenjang(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Jajargenjang')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang AB   '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Panjang BC   '+b+':'+w+' '))    
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Panjang CD   '+b+':'+w+' '))        
    da= float(input(b+'['+w+'*'+b+'] '+w+'Panjang DA   '+b+':'+w+' '))            
    keliling = ab+bc+cd+da
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan trapesium
def trapesium():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas trapesium")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling trapesium ")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+' trapesium'+y+' : ')
    if df == '01' or df == '1' :
        luas_trapesium()
    elif df == '02' or df == '2' :
        keliling_trapesium()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
                
#Luas_trapesium
def luas_trapesium(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas Trapesium')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Sisi atas    '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Sisi bawah   '+b+':'+w+' '))    
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Tinggi       '+b+':'+w+' '))        
    luas = (ab+bc)*cd/2
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Keliling_trapesium
def keliling_trapesium(): 
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Trapesium')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang AB   '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Panjang BC   '+b+':'+w+' '))    
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Panjang CD   '+b+':'+w+' '))        
    da= float(input(b+'['+w+'*'+b+'] '+w+'Panjang DA   '+b+':'+w+' '))            
    keliling = ab+bc+cd+da
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan_belah_ketupat
def belah_ketupat():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas Belah Ketupat ")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling Belah Ketupat ")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+'Belah-Ketupat'+y+' : ')
    if df == '01' or df == '1' :
        luas_belahketupat()
    elif df == '02' or df == '2' :
        keliling_belahketupat()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
        
#Luas_belah_ketupat
def luas_belahketupat () :
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas Belah Ketupat')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Diagonal 1   '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Diagonal 2   '+b+':'+w+' '))    
    luas = 0.5*ab*bc
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Keliling_belah_ketupat
def keliling_belahketupat () :
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Belah Ketupat')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang Sisi '+b+':'+w+' ')) 
    keliling = 4*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan_layang_layang
def layang_layang():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Luas Layang Layang ")
    print (b+"  ["+w+"02"+b+"] "+w+"Keliling Layang Layang")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun datar'+y+'/'+w+'Layang-Layang'+y+' : ')
    if df == '01' or df == '1' :
        luas_layanglayang()
    elif df == '02' or df == '2' :
        keliling_layanglayang()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
        
#Luas_layang_layang
def luas_layanglayang () :
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Luas Layang Layang')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Diagonal 1   '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Diagonal 2   '+b+':'+w+' '))     
    luas = 0.5*ab*bc
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, luas, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Keliling_layang_layang
def keliling_layanglayang () :
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Layang Layang')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang AB   '+b+':'+w+' ')) 
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Panjang BC   '+b+':'+w+' '))
    keliling = 2*(ab+bc)
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, keliling, w+ 'cm')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()
    
#Pilihan_bangun_ruang
def pilbangunruang() :	
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Kubik           "+b+"["+w+"03"+b+"] "+w+"Limss")
    print (b+"  ["+w+"02"+b+"] "+w+"Balok           "+b+"["+w+"04"+b+"] "+w+"Bola")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun-Ruang '+y+': ')
    if df == '01' or df == '1' :
        kubik()
    elif df == '02' or df == '2' :
        balok()
    elif df == '03' or df == '3' :
        limas()
    elif df == '04' or df == '4' :
        bola()
    else:
        start()

#Pilihan_Kubik
def kubik():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Keliling Kubik ")
    print (b+"  ["+w+"02"+b+"] "+w+"Volume Kubik")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun ruang'+y+'/'+w+'Kubik'+y+' : ')
    if df == '01' or df == '1' :
        keliling_kubik()
    elif df == '02' or df == '2' :
        volume_kubik()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()
        
#Keliling_Kubik
def keliling_kubik() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Kubik')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang Sisi '+b+':'+w+' '))
    keliling= 6*ab*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, keliling, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Volume_Kubik
def volume_kubik() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Volume Kubik')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang Sisi '+b+':'+w+' '))
    volume= ab*ab*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil        '+b+':'+w, volume, w+ 'cm3')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan_Balok
def balok():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Keliling Balok ")
    print (b+"  ["+w+"02"+b+"] "+w+"Volume Balok")
    print (r+"\n  ["+w+"03"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"04"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun ruang'+y+'/'+w+'Balok'+y+' : ')
    if df == '01' or df == '1' :
        keliling_balok()
    elif df == '02' or df == '2' :
        volume_balok()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()

#Keliling_balok
def keliling_balok() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Balok')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang     '+b+':'+w+' '))
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Lebar       '+b+':'+w+' '))
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Tinggi      '+b+':'+w+' '))
    keliling= 2*((ab*bc)+(ab*cd)+(bc*cd))
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, keliling, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Volume_Balok
def volume_balok() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Volume Balok')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Panjang     '+b+':'+w+' '))
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Lebar       '+b+':'+w+' '))
    cd= float(input(b+'['+w+'*'+b+'] '+w+'Tinggi      '+b+':'+w+' '))
    volume= ab*bc*cd
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, volume, w+ 'cm3')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan_Limas
def limas():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Volume Limas")
    print (r+"\n  ["+w+"02"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"03"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun ruang'+y+'/'+w+'Limas'+y+' : ')
    if df == '01' or df == '1' :
        volume_limas()
    elif df == '02' or df == '2' :
        start()
    elif df == '03' or df == '3' :
        exit()
    else :
        start()
        
#Volume_limas
def volume_limas() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Volume Limas')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Luas Alas   '+b+':'+w+' '))
    bc= float(input(b+'['+w+'*'+b+'] '+w+'Tinggi      '+b+':'+w+' '))
    volume = 1/3*ab*bc
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, volume, w+ 'cm3')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Pilihan_Bola
def bola():
    os.system('clear') 
    banner() 
    print (b+"  ["+w+"01"+b+"] "+w+"Keliling Bola")
    print (b+"  ["+w+"01"+b+"] "+w+"Volume Bola")    
    print (r+"\n  ["+w+"02"+r+"] "+w+"Kembali")
    print (r+"  ["+w+"03"+r+"] "+w+"Keluar")
    df = input(w+'\n['+y+'>'+w+'] Pilih'+y+'/'+w+'Bangun ruang'+y+'/'+w+'Bola'+y+' : ')
    if df == '01' or df == '1' :
        keliling_bola()
    elif df == '02' or df == '2' :
        volume_bola()
    elif df == '03' or df == '3' :
        start()
    elif df == '04' or df == '4' :
        exit()
    else :
        start()

#Keliling_bola
def keliling_bola() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Bola')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Jari-jari   '+b+':'+w+' '))
    keliling = 4*22/7*ab*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, keliling, w+ 'cm2')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Volume_bola
def keliling_bola() :    
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Keliling Bola')   
    ab= float(input(b+'['+w+'*'+b+'] '+w+'Jari-jari   '+b+':'+w+' '))
    volume = 4/3*22/7*ab*ab*ab
    print (b+'['+w+'#'+b+'] '+w+'Hasil       '+b+':'+w, keliling, w+ 'cm3')
    input(w+"\n["+y+"?"+w+"] Press enter to menu...")
    os.system('clear')
    start()

#Bilangan_prima
def prima():
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Bilangan Prima')   
    num = int(input(b+'['+w+'*'+b+'] '+w+'Masukkan bilangan '+b+':'+w+' '))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print (b+'['+w+'#'+b+'] '+w+'Angka'+r, num ,w+'Bukan bilangan prima')
                print (b+'['+w+'#'+b+'] '+w+'Karena'+r, i ,w+'Dikali'+w, num//i ,b+':'+w, num)
                break
        else:
            print (b+'['+w+'#'+b+'] '+w+'Angka'+r, num ,w+'Adalah bilangan prima')
    else:
        print (b+'['+w+'#'+b+'] '+w+'Angka'+r, num ,w+'Bukan bilangan prima')

#Faktor_Bilangan
def bilangan():
    os.system('clear') 
    banner() 
    print(b+'\n['+w+'#'+b+'] '+w+'Faktor Bilangan')   
    num = int(input(b+'['+w+'#'+b+'] '+w+'Masukkan bilangan '+b+':'+w+' '))
    fakt(num)
    
def fakt(x):
    print (b+'\n['+w+'#'+b+'] '+w+'Faktor Dari'+r, x ,b+':'+w+' ')
    for i in range(1, x+1):
        if x % i == 0:
            print (b+' *'+w+'',i)
         
def start():
    os.system('clear')
    banner() 
    awal() 
    main()
    
if __name__=='__main__':
    start()
