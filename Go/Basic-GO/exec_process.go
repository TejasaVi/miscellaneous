package main


import ("syscall"
		"os/exec"
		"os")
import "fmt"


func main() {
	bniary, LookErr := exec.LookPath("ls")
	if LookErr != nil {
		 panic(LookErr)
	}
	fmt.Println(bniary)
	args := []string{"ls", "-a", "-l", "-h"}
	fmt.Println(args)
	env:= os.Environ()
	fmt.Println(env)
	execErr := syscall.Exec(bniary, args, env)
	if execErr != nil {
		 panic(execErr)
	}
}
