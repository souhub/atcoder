package main

import (
	"fmt"
	"math"
)

func main() {

	// Define the variables.
	var N, N8 int
	d := make([]int, 6)

	// Input the value.
	fmt.Scanf("%d", &N)

	// Algorithm
	// for i := 1; i <= N; i++ {

	// 	// Check the digimal numbers.
	// 	for k := 0; k < 6; k++ {
	// 		s := strconv.Itoa(i)
	// 		fmt.Println(s)
	// 		if s[k] != '7' {
	// 			count++
	// 		}
	// 	}

	// Convert to octal numbers.
	for n := 5; n >= 0; n-- {
		k := N / int(math.Pow10(n))
		fmt.Println(k)
		if k != 0 {
			N8 += int(math.Pow(8, float64(n)))
		}
		N -= d[n] * int(math.Pow10(n))
	}

	fmt.Println(N8)

	// 	// Check the octal numbers.
	// 	for k := 0; k < 6; k++ {
	// 		s := strconv.Itoa(N8)
	// 		if s[k] != '7' {
	// 			count++
	// 		}
	// 	}
	// }
}
