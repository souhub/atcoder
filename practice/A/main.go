package main

import "fmt"

// link https://atcoder.jp/contests/practice/tasks/practice_1

var a, b, c int
var s string

func main() {

	fmt.Scanf("%d", &a)
	fmt.Scanf("%d %d", &b, &c)
	fmt.Scanf("%s", &s)

	fmt.Printf("%d %s", a+b+c, s)

}
