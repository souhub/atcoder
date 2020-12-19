package main

import (
	"fmt"
	"math"
)

func main() {
	// Difine the variables.
	var NMax, A, B, sum, answer int

	// Define sum of each digit
	sum = 0

	// Answer
	answer = 0

	// Enter the values.
	fmt.Scanf("%d %d %d", &NMax, &A, &B)

	// Algolithm
	for N := 1; N <= NMax; N++ {

		given := N
		// 10^4.10^3,10^2,10^1,10^0で割って各桁の数を求めて和を取る
		for i := 0; i <= 4; i++ {
			quotient := given / int(math.Pow10(4-i))
			sum += quotient
			given -= int(math.Pow10(4-i)) * quotient
		}
		if A <= sum && sum <= B {
			answer += N
		}
		sum = 0
	}

	// Output the answer.
	fmt.Println(answer)
}
