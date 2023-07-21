#Ler qualquer input e devolver true or false para vários tipos de is

a = input('Digite algo :')
print('O tipo primitivo deste valor é ',type(a))
print('só tem espaços ? ', a.isspace())
print('este valor tem só maiúsculas ? ', a.isupper())
print('este valor é um número ? ', a.isnumeric())
print('este valor só tem minúsculas ?', a.islower())
print('este valor é alfabético ?', a.isalpha())
print('este valor é alfanumérico ?', a.isalnum())
print('este valor está capitalizado ?', a.istitle())