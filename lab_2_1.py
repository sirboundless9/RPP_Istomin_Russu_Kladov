stroka = str(input('Введите строку'))
stroka_future = stroka.split()
print(sum(map(lambda x:
              x.startswith('m') + x.startswith('M'), StrokaFuture)))
