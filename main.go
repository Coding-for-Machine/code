package main

import (
	"log"
	"os"

	"github.com/Coding-for-Machine/code/handle"
	"github.com/gofiber/fiber/v2"
	"github.com/joho/godotenv"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	app := fiber.New()

	app.Get("/", handle.Home)
	// costom geteway server

	app.Get("/getaway", handle.Getaway)

	app.Listen(":" + os.Getenv("PORT"))
}
