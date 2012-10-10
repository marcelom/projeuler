// Project Euler, Problem 3
// What is the largest prime factor of the number 600851475143

package main

import "fmt"

var n uint64 = 600851475143
var d uint64 = 2

func main() {
	for n > 1 {
		for n%d == 0 {
			n /= d
		}
		d++
	}
	fmt.Println("Largest Prime Factor is ", d-1)
}
