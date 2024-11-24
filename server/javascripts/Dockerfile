# Node.js imajidan foydalanamiz
FROM node:16

# Ishlash papkasini yaratish
WORKDIR /app

# package.json va package-lock.json fayllarini konteynerga nusxalash
COPY package*.json /app/

# Kutubxonalarni o‘rnatish
RUN npm install

# Barcha kodni konteynerga nusxalash
COPY . /app

# Dastur boshlanishi
CMD ["node", "index.js"]
