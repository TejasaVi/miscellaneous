package main

import "fmt"


func addtion(a int, b int)int {
	return a+b
}


func main() {
	fmt.Println("Sample Addtion:", addtion(1,2))
	fmt.Println("Recursive Sample Addtion:", addtion(3,addtion(1,2)))
}
