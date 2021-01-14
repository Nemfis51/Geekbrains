time = int(input('Введите время в секундах: '))
seconds = time % 60
minutes = time // 60
hours = time // 3600
print(f"чч:мм:сс   {hours} : {minutes % 60:02} : {seconds:02}")