from math import pi

shape = input('ต้องการหาพื้นที่ของ วงกลม(c) สามเหลี่ยม(t) หรือสี่เหลี่ยม(r): ')
if shape == 'c':
  r = float(input('ป้อนรัศมีของวงกลม: '))
  area = pi * r * r
elif shape == 't':
  b = float(input('ป้อนความยาวฐาน: '))
  h = float(input('ป้อนความสูง: '))
  area = (1 / 2) * b * h
elif shape == 'r':
  w = float(input('ป้อนความกว้าง: '))
  l = float(input('ป้อนความยาว: '))
  area = w * l
else:
  print('รูปดังกล่าวมีพื้นที่', area, 'ตารางหน่วย')