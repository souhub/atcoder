package main

import "fmt"

func main() {
	// Define the variables
	var X, N, topMochi int

	// Input the values.
	fmt.Scanf("%d", &N)
	d := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &d[i])
	}

	// Algorithm
	// Get topMochi
	topMochi, k := getLargestMochi(d, N)
	d[k] = 0

	// for
	for n := 1; n <= N; n++ {
		// Search the largest Kagami Mochi.
		largestMochi, k := getLargestMochi(d, N)
		d[k] = 0

		// Compare the largestMochi to topMochi
		if topMochi == largestMochi {
			continue
		} else if topMochi < largestMochi {
			break
		} else {
			X++
			topMochi = largestMochi
		}
	}

	// Output X
	fmt.Println(X)

}

// Define "getLargestMochi" function
func getLargestMochi(d []int, N int) (largestMochi, k int) {
	largestMochi = d[0]
	k = 0
	for j := 1; j < N; j++ {
		if largestMochi < d[j] {
			largestMochi = d[j]
			k = j
		}
	}
	return
}
