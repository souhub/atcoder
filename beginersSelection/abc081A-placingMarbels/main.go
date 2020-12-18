package main

import "fmt"

func main() {
	// Enter the values
	var s string
	// Count the number of 1
	fmt.Scanf("%s", &s)
	var count int
	count = 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			count++
		}
	}
	// Output the answer
	fmt.Println(count)
}
