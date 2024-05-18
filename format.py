message = "Atakan Çalıkoğlu yaşım 22"

message = message.replace('Atakan','Hayrünisa')
message = message.replace(' ','*')

print(message)

message2 = "Kebapçıyı Dürüm Yaptıııııık Dürüm"

message2 = message2.center(50,'=')

print(message2)

result= message2.count('e')
print(result)
result2=message2.count('ı',0,15) #I karakterinin 0 15 arasında kaç tane oldugunu gösteriyor

message3 = "www.araba.com"
result3 = message3.endswith('com') #message3 com ile bitiyor mu
print(result3)

result4 = 'helloworld'.isalpha()  #içindekilerin hepsi harf mi diye bakıyor
print(result4)

result5 = '123'.isdigit() # içindekiler rakam mı
print(result5)

result6 = 'Contents'.center(50,'*')
print(result6)

result6 = 'Contents'.ljust(50,'*')  #sola yaslayarak yapar , rjust sağa yaslayarak yapar
print(result6)

course = 'Hello Software Earth'

result7 = course.split(' ')   #course karakter dizisini boşluklarından ayırın
print(result7)
