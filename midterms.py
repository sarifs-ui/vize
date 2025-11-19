number1= int(input("sayı yaz\n")) #kullanıcıdan sayı aldık
if number1>100 or number1<=0:  #eğer istedğimizden büyük küçük sayı girerse diye yada kod buga girmesin diye kullanıcıyı yönelendiriyoz
    print("aga düzgün sayı gir")
else: # doğru sayı girdiyse buraya geliyo 
    print("den/dansonraki 100'e tüm tam kare sayılar")
    while number1<100: # sayı 10den küçükse
        if (number1/(number1**0.5))==number1**0.5: # sayı kendi kare köküne bölününce kendi karekökünü veriyorsa bu sayıyı yazdır dedik
            print(int(number1))
            number1= ((number1**0.5)+1)**2  # bu dda bu son tam kare sayıdan sonraki tam kare sayıya gönderiyor
        else:
            number1+=1 #eğer sayı tam kare değilse hem printlemiyo hemde tma kare olana kadar artırmış luyor. X
