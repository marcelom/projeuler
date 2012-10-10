// Project Euler, Problem 5
// What is the smallest number divisible by each of the numbers 1 to 20?

package main

import "fmt"

var n uint64 = 600851475143
var d uint64 = 2

// The key here is to make a sieve, and then multiply... lets see how it goes...
func main() {
	n:=20 // sieve limit
	s := [n+1]int // this is the sieve. 0 means not visited, 1 means visited, 2 means last visited, use 1 extra, take make things simpler...
	for a:=1; a<n+1; a++{
		for b:=a; b<20; b++{
			if s[b] == 0 {
				s[b







	for n > 1 {
		for n%d == 0 {
			n /= d
		}
		d++
	}
	fmt.Println("Largest Prime Factor is ", d-1)
}
