package main


import "fmt"

func zeroval(i int) {
	i = 0;
}

func zeroptr(iptr *int) {
	*iptr = 0;
}

func main() {
	var i int  = 1;
	fmt.Println(i)
	zeroval(i)
	fmt.Println(i)
	zeroptr(&i)
	fmt.Println(i)

}
