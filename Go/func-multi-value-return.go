package main

import "fmt"


func division(a int, b int)(int,int){

	return a/b,a%b
}

func main() {
	fmt.Println(division(10,5))
}
