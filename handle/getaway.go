package handle

import "github.com/gofiber/fiber/v2"

func Getaway(c *fiber.Ctx) error {
	return c.SendString("Hello, getaway!")
}
