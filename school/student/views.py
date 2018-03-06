from django.shortcuts import render

#設定載入對應的Model
from student.models import student

#取得student資料表所有資料
#SELECT * FROM student
def getList (request):
  response = {}
  data = student.objects.all()
  response['data'] = data

  #將取得的資料扔給Template使用
  return render(request, 'getList.html', response)

#取得student單筆資料
#SELECT * FROM student Where pk = [外部變數pk代入]
def getRow (request):
  response = {}
  data = student.objects.get(pk=pk)

  #將取得的資料扔給Template使用
  return render(request, 'getRow.html', response)

#新增一筆資料到student資料表
#INSERT INTO student (name, gender, born, email, phone, country, city, area, address, zip) VALUES ('Peter', 'M', '1984-03-04', 'teed7334@gmail.com', '0932179286', '台灣', '新北市', '新店區', '中興路二段192號6樓之2', '123')
def add (request):

  response = {}

  if request.method == 'POST':

    data = request.POST
    errors = {}
    by_pass = True

    for key in data:
      errors[key] = False
      if '' == data[key].strip():
        errors[key] = True
        by_pass = False

    response['errors'] = errors

    if by_pass:
      student.objects.create(
        name=data['name'],
        gender=data['gender'],
        account=data['account'],
        password=data['password'],
        born=data['born'],
        email=data['email'],
        phone=data['phone'],
        country=data['country'],
        city=data['city'],
        area=data['area'],
        address=data['address'],
        zip=data['zip'],
      )

  #將取得的資料扔給Template使用
  return render(request, 'add.html', response)



#修改student資料表中，pk為外部變數pk代入的資料
#UPDATE student SET name='Fielia', gender='F', born='1999-03-02', email='fielia@yahoo.com', phone='0900123456', country='台灣', city='新北市', area='板橋區', address='館前路111號', zip='246' WHERE pk = [外部變數pk代入]
def edit (request, pk):
  response = {}
  data = student.objects.get(id=pk)
  response['data'] = data

  #將取得的資料扔給Template使用
  return render(request, 'edit.html', response)

#刪除student資料表中，pk為外部變數pk代入的資料
#DELETE FROM student WHERE pk = [外部變數pk代入]
def remove (request, pk):
  data = student.objects.get(id=pk)
  data.delete()

  #將取得的資料扔給Template使用
  return render(request, 'remove.html')
