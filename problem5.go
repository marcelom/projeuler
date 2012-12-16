// Project Euler, Problem 5
// What is the smallest number divisible by each of the numbers 1 to 20?

package main

import "fmt"

var n int = 20
var s [21]int
var prod int = 1

// The key here is to make a sieve, and then multiply... lets see how it goes...
func main() {
	//s := [n+1]int // this is the sieve. 0 means not visited, 1 means visited,
	// 2 means last visited - use 1 extra, to make things simpler...
	for a := 2; a < n+1; a++ {
		for b := a; b < n+1; b += a {
			if s[b] == 0 {
				if b < 20-a {
					s[b] = 1
				} else {
					s[b] = 2
				}
			} else {
				break
			}
		}
	}
	for a := 1; a < n+1; a++ {
		if s[a] == 2 {
			fmt.Print(a," x ")
			prod *= a
		}
	}
	fmt.Println(prod)
}
