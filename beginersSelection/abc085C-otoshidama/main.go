package main

import "fmt"

func main() {
	// Define the variables.
	var N, Y int

	answer := [3]int{-1, -1, -1}
	// Input the values.
	fmt.Scanf("%d %d", &N, &Y)

	// Algorithn
	for i := 0; i <= N; i++ {
		for j := 0; j <= N-i; j++ {
			for k := 0; k <= N-i-j; k++ {
				actualY := 10000*i + 5000*j + 1000*k
				if actualY == Y && i+j+k == N {
					answer = [3]int{i, j, k}
				}
			}
		}
	}

	// Output the answer
	fmt.Printf("%d %d %d\n", answer[0], answer[1], answer[2])
}
