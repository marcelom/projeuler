// Project Euler, Problem 7
// What is the 10001'st prime ?

package main

import "fmt"

var primes [10001]int64
var c int64

func main() {
	primes[0] = 2
	c = 3
	i := 0
	for i < 10001 {
		if primes[i] == 0 {
			// found a prime
			primes[i] = c
			fmt.Println(i, c)
			c += 2
			i = 0
			continue
		}
		if c%primes[i] != 0 {
			i++
		} else {
			c += 2
			i = 0
		}
	}
	fmt.Println(primes[i-1])
}
