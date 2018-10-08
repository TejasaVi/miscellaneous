package main

import "fmt"


func main() {

	mp:= make(map[string]int)
	fmt.Println("emp:",mp);
	mp["Key1"] = 12
	mp["Key2"] = 22
	mp["Key3"] = 32
	mp["Key4"] = 42
	mp["Key5"] = 52
	mp["Key6"] = 62
	fmt.Println("After value :",mp);
	fmt.Println("Accessing value :",mp["Key1"]);
}
