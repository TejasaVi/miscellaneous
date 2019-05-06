package main

import "fmt"


type person struct {
	name string;
	age int;
}
func main() {
	fmt.Println(person{"Bob", 20})
	fmt.Println(person{name: "Fred", age:30})
	fmt.Println(person{name: "Dred"})
	p := person{"Tejas", 27}
	sp := &p
	fmt.Println(sp)

}
