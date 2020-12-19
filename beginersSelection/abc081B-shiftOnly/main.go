package main

import "fmt"

func main() {
	var N, count int
	count = 0

	fmt.Scanf("%d", &N)

	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &A[i])
	}

	for {
		existAdd := false

		for i := 0; i < N; i++ {
			if A[i]%2 != 0 {
				existAdd = true
			}
		}

		if existAdd {
			break
		}

		for i := 0; i < N; i++ {
			A[i] /= 2
		}
		count++
	}

	fmt.Println(count) //println(count) と書くとAtCoderではなぜかエラーになる
}
