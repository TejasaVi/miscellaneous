package main

import "fmt"


func InSeq() func() int {
	i:=0
	return func() int {
		i++;
		return i;
	}
}

func main() {
	NextSeq := InSeq()
	fmt.Println(NextSeq())
	fmt.Println(NextSeq())
	fmt.Println(NextSeq())
	fmt.Println(NextSeq())
	fmt.Println(NextSeq())
}
