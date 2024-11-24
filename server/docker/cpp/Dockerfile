# C++ uchun imajdan foydalanamiz
FROM gcc:10

# Ishlash papkasini yaratish
WORKDIR /app

# C++ fayllarini konteynerga nusxalash
COPY . /app

# C++ dasturini kompilyatsiya qilish
RUN g++ -o myapp main.cpp

# Dastur boshlanishi
CMD ["./myapp"]
