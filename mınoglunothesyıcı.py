
sayı=input("sınav notunu gir.\n") # kullanıcıdan veri aldık
sayı=int(sayı) # tam sayı olsun virgüllü falan girerlerse
print("harf notun:")    
if sayı>=80:
        print("A")
        sayı+=10
        if sayı<100 :
            print("notun A ama çok daha yüksek alabilirdin")
        else:
            print("helall")
elif 50<sayı<80:
    print("ĞIQK")
else:
    print("ıyy disgusting not")
    
              
