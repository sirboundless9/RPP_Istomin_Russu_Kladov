stroka = str(input('Введите строку'))
StrokaFuture = stroka.split()
print(sum(map(lambda x:
              x.startswith('m') + x.startswith('M'), StrokaFuture)))