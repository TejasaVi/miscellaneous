package main
import "fmt"

func foobar(from string) {
	i := 0
	for i<3 {
		i++
		fmt.Println(from,":",i)
	}
}

func main() {
	foobar("Main")
	go foobar("goroutine")
	fmt.Scanln()
	fmt.Println("Done")
}
