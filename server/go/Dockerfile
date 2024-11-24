# Go rasmidan foydalanish
FROM golang:1.18-alpine

# Ishlash uchun katalogni o‘rnatish
WORKDIR /app

# Go mod va sum fayllarini konteynerga nusxalash
COPY go.mod go.sum ./

# Kerakli kutubxonalarni o‘rnatamiz
RUN go mod tidy

# Barcha kodni konteynerga nusxalash
COPY . .

# Go dasturini kompilyatsiya qilish
RUN go build -o main .

# Dasturini ishga tushirish
CMD ["./main"]
