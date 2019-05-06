package main

import ("fmt"
		"time")

func main() {
	p := fmt.Println
	now := time.Now()
	sec := now.Unix()
	p(sec)
	nano := now.UnixNano()
	p(nano)
}
