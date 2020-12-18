package main

import (
	"fmt"
	"log"
)

func main() {
	// 1<=a,b<=1000
	// a,b is natural numbers
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	if (a*b)%2 != 0 {
		fmt.Println("Odd")
	} else if (a*b)%2 == 0 {
		fmt.Println("Even")
	} else {
		log.Fatalln("ERROR")
	}
}
