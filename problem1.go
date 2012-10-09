// Project Euler, Problem 1
// Add all the natural numbers below one thousand that are multiples of 3 or 5.

package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 1000; i++ {
		if i == (i/3)*3 || i == (i/5)*5 {
			sum += i
			fmt.Print(i, " ")
		}
	}
	fmt.Println("sum is ", sum)
}
