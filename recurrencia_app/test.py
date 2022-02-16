from urllib.request import urlopen, Request


response = urlopen('http://localhost:8000/recurrencia/peticion').read()
    
for word in response.split():
    if len(word) > 40:
        print(word)
        empty = ''
        response = response.replace(word, empty.encode())
        
print('fin!!!!!!!')
