print('- * ยินดีต้อนรับสู่รถโดยสารค่ะ ไม่ทราบว่ามากันทั้งหมดที่ท่านคะ * -')
all = int (input ('มีผู้โดยสารทั้งหมดกี่คน:'))
children = int (input ('มีผู้โดยสารอายุตํ่ากว่า 3 ขวบกี่คน:'))
elders = int (input ('มีผู้โดยสารอายุตั้งเเต่ 60 ปีขึ้นไปกี่คน:'))
regular = (all - children - elders)
fare_elders = elders*(10/2)
fare_regular = regular*10
total = fare_elders + fare_regular
print ('จํานวนผู้โดยสารทั้งหมด',all,'คน')
print ('เป็นเด็กอายุตํ่ากว่า 3 ขวบ',children,'คน')
print ('เป็นผู้สูงอายุ',elders,'คน')
print ('เป็นผู้โดยสารคิดอัตราปกติ',regular,'คน')
print ('เป็นผู้โดยสารรวมทั้งสิ้น',total,'บาท')
if all<=30 and total>=200:
  total_discounted = total - (total*0.1)
  print ('ลดราคา 10% คิดเป็นค่าโดยสารทั้งสิ้น',total_discounted,'บาท')
print('- * ขอบคุณที่ใช้บริการค่ะ ขอให้เดินทางโดยสวัสดิภาพ * -')