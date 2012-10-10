// Project Euler, Problem 9
// Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.

package main

import "fmt"

func main() {
	for a := 1; a < 998; a++ {
		for b := 1; b < 999-a; b++ {
			c := 1000 - a - b
			if a*a+b*b == c*c {
				fmt.Println("Found it: (a b c) = (", a, b, c, ")")
				return
			}
		}
	}
}
