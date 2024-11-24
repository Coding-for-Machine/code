# Go imajidan foydalanamiz
FROM golang:1.21-alpine

# Ishlash papkasini yaratamiz
WORKDIR /app

# Go mod va sum fayllarini konteynerga nusxalaymiz
COPY go.mod go.sum ./

# Kerakli kutubxonalarni o‘rnatamiz
RUN go mod tidy

# Kodni konteynerga nusxalaymiz
COPY . /app

# Go dasturini kompilyatsiya qilamiz
RUN go build -o main .

# Dastur ishga tushuriladi
CMD ["./main"]
