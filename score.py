print('วิเคาระห์ผลคะแนนสอบ')
work = input('คุณมีงานค้างส่งหรือไม่ ( มี , ไม่มี ): ')
if work == 'มี':
  print('ผลที่ได้ : ร.')
if work == 'ไม่มี':
  score = int(input('คุณมีช่วงคะแนนเท่าไหร่: '))
  if score > 49 :
     print('ผ่าน')
  elif score > 69 :
       print('ดี')
  elif score > 89 :
      print('เยี่ยม')
  else:
      print('ไม่ผ่าน')