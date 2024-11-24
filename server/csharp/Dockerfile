# .NET Core asosidagi rasmni ishlatish
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

# Ishlash uchun direktoriyani o'rnatish
WORKDIR /src

# C# loyihasini konteynerga nusxalash
COPY ["csharp-project.csproj", "./"]

# NuGet paketlarini tiklash
RUN dotnet restore "csharp-project.csproj"

# Barcha kodni konteynerga nusxalash
COPY . .

# Loyihani kompilyatsiya qilish
RUN dotnet build "csharp-project.csproj" -c Release -o /app/build

# Loyihani ishga tushirish
FROM build AS publish
RUN dotnet publish "csharp-project.csproj" -c Release -o /app/publish

# Yangi konteynerni yaratish va tayyor holga keltirish
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=publish /app/publish .

# Portni ochish
EXPOSE 80

# Dastur ishga tushirilishi
ENTRYPOINT ["dotnet", "csharp-project.dll"]
