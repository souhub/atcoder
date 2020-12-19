package main

import (
	"fmt"
)

func main() {

	// Define the variables.
	var N, aliceScores, bobScores int

	// Input the values.
	fmt.Scanf("%d", &N)

	a := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &a[i])
	}

	// Algorithm
	for n := 1; n <= N; n++ {

		// Search the highest number
		highestNumber, k := getHighestNumber(a, N)

		// Decide who to add the points to.
		if n%2 == 0 {
			// Give Bob the points.
			bobScores += highestNumber
		} else {
			// Give Alice the points.
			aliceScores += highestNumber
		}

		// Remove the highest number(a[k]) from arrays
		a[k] = 0
	}

	// Output the difference
	fmt.Println(aliceScores - bobScores)
}

// Define "getHigestNumber" function.
func getHighestNumber(a []int, N int) (highestNumber, k int) {
	highestNumber = a[0]
	k = 0
	for j := 1; j < N; j++ {
		if highestNumber < a[j] {
			highestNumber = a[j]
			k = j
		}
	}
	return
}
