package main

import "fmt"


func main() {


	i := 0
	for i<=10 {
		fmt.Println("Number = %d",i);
		i = i+1;
	}
	for {
		fmt.Println("Loop break");
		break;
	}
	for j:=1;j<5;j++ {
		fmt.Println("Number = %d",j);
	}

	var list = [...]int {1,2,3,4,45,6}

	for j := range list{
		fmt.Println("Number: %d",j)
	}
}
