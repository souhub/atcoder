package main

import "fmt"

// Reference: https://atcoder.jp/contests/abc186/tasks

func main() {
	var N, W int
	fmt.Scanf("%d %d", &N, &W)

	max := N / W
	fmt.Println(max)
}
