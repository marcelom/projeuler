package main

import (
	"fmt"
)

func main() {
	var longest, terms uint32

	for i := uint32(1); i <= 1000000; i++ {
		j := i
		this_terms := uint32(1)

		for j != 1 {
			this_terms++

			if this_terms > terms {
				//fmt.Println(i,j)
				terms = this_terms
				longest = i
			}

			if j%2 == 0 {
				j = j / 2
			} else {
				j = 3*j + 1
			}

		}
	}

	fmt.Println("Longest is", longest, "(with", terms, "terms)")
}
