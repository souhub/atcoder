package main

import "fmt"

func main() {
	// Define the variables.
	var H, W int

	// Input the values.
	fmt.Scanf("%d %d", &H, &W)
	A := make([]int, H*W)
	for k := 0; k < H*W; k++ {
		fmt.Scanf("%d", &A[k])
	}

	// Get the minimum value from "A" array.
	min := getMin(A, H, W)

	// Find the difference and sum it up.
	sum := 0
	for i := 0; i < H*W; i++ {
		dA := A[i] - min
		sum += dA
	}

	// Output the answer.
	fmt.Println(sum)

}

func getMin(A []int, H, W int) (min int) {
	min = A[0]
	minNum := 0
	for j := minNum; j < H*W; j++ {
		if A[j] < min {
			min = A[j]
			minNum = j
		}
	}
	return
}
