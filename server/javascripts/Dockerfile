# Node.js rasmidan foydalanish
FROM node:16

# Ishlash uchun direktoriyani o'rnatish
WORKDIR /app

# NPM cache'ni tozalash
RUN npm cache clean --force

# package.json va package-lock.json fayllarini nusxalash
COPY package*.json ./

# Npm kutubxonalarini o'rnatish
RUN npm install

# Barcha kodni konteynerga nusxalash
COPY . .

# Konteynerda ishga tushiradigan portni ko'rsatish
EXPOSE 3000

# Dastur ishga tushishi
CMD ["npm", "start"]
