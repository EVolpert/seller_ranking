# Derivando da imagem oficial do MySQL
FROM mysql:8.0

# Adicionando os scripts SQL para serem executados na criação do banco
ADD ./db/create_database.sql /docker-entrypoint-initdb.d/create_database.sql
RUN chmod -R 775 /docker-entrypoint-initdb.d