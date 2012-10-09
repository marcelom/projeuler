// Project Euler, Problem 2
// By considering the terms in the Fibonacci sequence whose values do
// not exceed four million, find the sum of the even-valued terms.

package main

import "fmt"

func main() {
	a := 2 // im starting with the sequence already in 2 and 3
	b := 3
	sum := 0
	for a <= 4000000 {
		fmt.Print(a, " ")
		sum += a
		a, b = b, a+b // advance the sequence in 3 iterations: get the next even...
		a, b = b, a+b
		a, b = b, a+b
	}
	fmt.Println("sum is ", sum)
}
