from Dao import Dao

host = '127.0.0.1'
user = 'root'
password = 'mestre175'
db = 'mkt2'
banco = Dao(host, user, password, db)
# banco.__select('a','b','c')


dados = "'1','joão','Ç^~; . , '"
# print(dados)
result2 = banco.insert("pais_id, usuario_email, usuario_senha", "mkt2.usuario", dados)
print(result2)

result = banco.select("*", "mkt2.usuario")
print(result)