package main

import (
	"fmt"
	"math"
)

func main() {
	var ix, iy, sin, cos, tan float64
	x := 0.0
	y := 1.0
	rx := (x-1.0)*(x-1.0) + y*y
	ix = -(x-1)*(x-1) - y*y + 3*(x-1)*(x-1)*math.Pow(rx, -2.5)
	iy = 3 * y * (x - 1) * math.Pow((x-1)*(x-1)+y*y, -2.5)
	r := math.Sqrt(ix*ix + iy*iy)
	sin = math.Sin(iy / r)
	cos = math.Cos(ix / r)
	tan = sin / cos
	fmt.Printf("(x,y)=(%v.%v)のとき\nix=%v\niy=%v\ntanθ=%v\n", x, y, ix, iy, tan)
}

func reverse(s string) string {
	rs := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		rs[i], rs[j] = rs[j], rs[i]
	}
	return string(rs)
}
