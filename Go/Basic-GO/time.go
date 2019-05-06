package main

import "fmt"
import "time"

func main() {
	p := fmt.Println

	now := time.Now()
	p(now)

	then := time.Date(2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then.Year())
	p(then.Month())
	p(then.Location())
	diff := now.Sub(then)
	p(diff.Hours())
	p(then.Before(now))
	p(then.Weekday())
}
