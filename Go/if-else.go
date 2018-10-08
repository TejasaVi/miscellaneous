package main

import "fmt"


func main() {


	if 17%2 == 0 {
		fmt.Println("Mod operator returned zero value");
	} else if 17%2 == 1 {
		fmt.Println("Mod operator returned value 1");
	} else {
		fmt.Println("Mod operator returned value non-zero value");
	}
}
