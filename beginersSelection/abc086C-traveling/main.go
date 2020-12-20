package main

import "fmt"

// GIVE UP
func main() {
	// Define the variables.
	var N int
	answer := "No"

	// Input the values.
	fmt.Scanf("%d", &N)
	t := make([]int, N+1)
	x := make([]int, N+1)
	y := make([]int, N+1)
	for i := 1; i <= N; i++ {
		fmt.Scanf("%d %d %d", &t[i], &x[i], &y[i])
	}
	fmt.Println(x)

	// Algorithm
	for k := 0; k <= N; k++ {

	}

	// Output the answer.
	fmt.Println(answer)
}
