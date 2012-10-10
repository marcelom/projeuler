// Project Euler, Problem 1
// Add all the natural numbers below one thousand that are multiples of 3 or 5.

package main

import "fmt"

func main() {
	fmt.Println("Solution 1:", p1s1())
	fmt.Println("Solution 2:", p1s2())
	fmt.Println("Solution 3:", p1s3())
}

// Problem 1, Solution 1 - Brute force...
func p1s1() int {
	sum := 0
	for i := 0; i < 1000; i++ {
		if i == (i/3)*3 || i == (i/5)*5 {
			sum += i
			// fmt.Print(i, " ")
		}
	}
	return sum
}

// Problem 1, Solution 2 - Less Brute force...
func p1s2() int {
	sum := 0
	for i := 3; i < 1000; i += 3 {
		sum += i
	}
	for i := 5; i < 1000; i += 5 {
		sum += i
	}
	for i := 15; i < 1000; i += 15 {
		sum -= i
	}
	return sum
}

// Problem 1, Solution 3 - Now we are talking...
func p1s3() int {
	sum := 3*(1000)*(1001)/2 + 5*(1000)*(1001)/2 - 15*1000*1001/2
	return sum
}
