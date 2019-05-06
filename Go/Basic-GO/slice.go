package main

import "fmt"

func main() {

	st:= make([]string,3)
	fmt.Println("Intial:",st);
	st[0] = "a"
	st[1] = "b"
	st[2] = "c"
	fmt.Println("After setting values:",st);
	st = append(st,"def")
	fmt.Println("After appending values:",st);
	st = append(st,"asd")
	fmt.Println("Slice[1:3]",st[1:3]);
	fmt.Println("Slice[:3]",st[:3]);
	fmt.Println("Slice[3:]",st[1:3]);
}
