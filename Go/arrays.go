package main

import "fmt"

func main () {
	var a[10]int
	fmt.Println("Initial:",a);
	a[2] = 10
	fmt.Println("After setting value:",a);
}
