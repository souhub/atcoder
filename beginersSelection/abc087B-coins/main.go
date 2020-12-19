package main

import "fmt"

func main() {
	var A, B, C, X int

	fmt.Scanf("%d", &A)
	fmt.Scanf("%d", &B)
	fmt.Scanf("%d", &C)
	fmt.Scanf("%d", &X)

	count := 0
	sum := 0

	for a := 0; a <= A; a++ {
		sumA := 500 * a
		sum = sumA
		if sum == X {
			count++
			sum = 0
			break
		}

		for b := 0; b <= B; b++ {
			sumB := 100 * b
			sum = sumA + sumB
			if sum == X {
				count++
				sum = 0
				break
			}

			for c := 0; c <= C; c++ {
				sumC := 50 * c
				sum = sumA + sumB + sumC
				if sum == X {
					count++
					sum = 0
					break
				}
			}
		}
		sum = 0
	}

	fmt.Println(count) //print(count) と書くとAtCoderではなぜかエラーになる
}
