package main

import ("fmt"
		"flag")

func main() {
	// Cmdline named parameter, foo is default value.
	wordPtr := flag.String("word", "foo", "a string")
	// Commandline boolean option, false is default value.
	boolPtr := flag.Bool("fork", false, "a bool")
	// CmdLine integer option, 42 is default value.
	numbPtr := flag.Int("numb", 1, "an int")

	flag.Parse()

	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:",*numbPtr)
	fmt.Println("fork",*boolPtr)
	fmt.Println("tail:", flag.Args())
}

