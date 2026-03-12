FROM golang:1.22-alpine

WORKDIR /app

COPY . .

RUN go build -o auth-service

EXPOSE 8001

CMD ["./auth-service"]
