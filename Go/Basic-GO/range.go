package main

import "fmt"

func main() {
	kvs:= make(map[string]string)
	kvs["A"] = "Apple"
	kvs["B"] = "Ball"
	kvs["C"] = "Cat"
	for key,pair := range kvs {
		fmt.Println(key, pair);
	}

	nums := []int{1,2,3,4,5,6}
	for num := range nums {
		fmt.Println(num)
	}
}
