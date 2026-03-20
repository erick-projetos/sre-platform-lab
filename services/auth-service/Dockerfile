# imagem base
FROM golang:1.23-alpine

# diretório de trabalho
WORKDIR /app

# copiar arquivos
COPY . .

# compilar aplicação
RUN go build -o auth-service

# expor porta
EXPOSE 8001

# rodar serviço
CMD ["./auth-service"]
