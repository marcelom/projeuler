// Project Euler, Problem 6
// Find the difference between the sum of the squares of the
// first one hundred natural numbers and the square of the sum

package main

import "fmt"

func main() {
	sum := 0
	sumofsquares := 0
	for i := 1; i <= 100; i++ {
		sum += i
		sumofsquares += i * i
	}
	fmt.Println("difference is ", sum*sum-sumofsquares)
}
