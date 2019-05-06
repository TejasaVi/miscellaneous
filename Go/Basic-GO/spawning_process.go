package main

import ("fmt"
		"os/exec")

func main() {
	dataCmd := exec.Command("date")
	dataOut, err := dataCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println(">date\n",string(dataOut))

	fmt.Println("This will be executed unlike execing process")
}

