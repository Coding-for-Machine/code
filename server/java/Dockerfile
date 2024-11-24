# Java imajidan foydalanamiz
FROM openjdk:17-jdk-slim

# Ishlash papkasini yaratish
WORKDIR /app

# Java kodini konteynerga nusxalash
COPY . /app

# Dastur qurilishi
RUN javac app.java

# Dastur boshlanishi
CMD ["java", "app"]
