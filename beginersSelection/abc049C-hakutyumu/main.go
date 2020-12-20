package main

import (
	"fmt"
)

func main() {

	// Define the variables.
	var S, rT string
	answer := "NO"

	// Input the values.
	fmt.Scanf("%s", &S)

	// Reverse "S".
	rS := reverse(S)

	// Algorithm
	n := 0
	for {
		// Why couldn't I get out of the if statement with the switch statement default?
		if string(rS[n+4]) == "d" {
			rT += "maerd"
			n += 5
		} else if string(rS[n+4]) == "r" {
			rT += "resare"
			n += 6
		} else if string(rS[n+4]) == "e" {

			switch string(rS[n+3]) {
			case "a":
				rT += "remaerd"
				n += 7
			case "r":
				rT += "esare"
				n += 5
			}
		} else {
			break
		}

		if len(S) <= len(rT) {
			break
		}
	}

	T := reverse(rT)
	if S == T {
		answer = "YES"
	}
	// Output the answer
	fmt.Println(answer)
}

// Define "reverse function.
func reverse(s string) string {
	rs := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		rs[i], rs[j] = rs[j], rs[i]
	}
	return string(rs)
}
