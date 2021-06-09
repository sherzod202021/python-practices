matn = "Bugun havo juda ajoyib hammma ishlarni qilishga zo'r sheroit bo'ldi"
print("hamma" in (matn))
matnn = "Bugun havo juda issiq lekin issiq ham ham yaxshi"
if "lekint" in matnn:
	print("To'g'ri topdingiz ushbu matnda lekin so'zi mavjud")
else:
	print("Ushbu matnda lekin so'zi mavjud emas")


text = "Surxondaryo viloyati Sariosiyo tumani IT park dasturchilari bugun bitiruvchi sertifikatini olishdi"
if "IT park dasturchilarii" in text:
	print("Ushbu matnda 'IT park dasturchilari' sozi mavjud")
else:
	print("Ushbu matnda 'IT park dasturchilari' sozi mavjud emas")


text1 = "Bugun IT park dasturchilarini sertifikat oladigan kuni"
print("sertifikatlar" not in text1)
print("sertifikatlar" in text1)




text2 = "Bugun IT park dasturchilari uchun omadli kun chunki bugun sertifikat olishiyapti"
print(text2[2:12])
print(text2[-12:-2])
print(text2[:8])
		
