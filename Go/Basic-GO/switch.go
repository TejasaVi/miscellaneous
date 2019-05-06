package main


import "fmt"



func main () {


	i:= 1
	switch i {
		case 1:
			fmt.Println("case 1");
		case 2:
			fmt.Println("case 2");
		default:
			fmt.Println("case Default");
	}
}
