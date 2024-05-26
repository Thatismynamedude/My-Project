import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color('DarkMagenta','Gold')
t.width(5)

shape = input('ต้องการหาพื้นที่ของ วงกลม(c) หรือ สี่เหลี่ยมจัตุรัส(r): ')
if shape == 'c':
  r = float(input('ป้อนรัศมีของวงกลม: '))
  t.shape("circle")
  t.circle(r)
  t.end_fill
elif shape == 'r':
  w = float(input('ป้อนขนาดของสี่เหลี่ยม: '))
  for i in range(4):
    t.fd(w)
    t.left(90)
else:
  print('กรุญาพิมพ์ c , r เท่านั่น')