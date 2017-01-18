from Dao import Dao

host = '127.0.0.1'
user = 'root'
password = 'mestre175'
db = 'mkt2'
banco = Dao(host, user, password, db)
# banco.__select('a','b','c')

result = banco.select("*", "mkt2.usuario")

dados = "'1','emaddssadasil','sdasdsadsadsadadenha'"
print(dados)
result2 = banco.insert("pais_id, usuario_email, usuario_senha", "mkt2.usuario", dados)
print(result2)
