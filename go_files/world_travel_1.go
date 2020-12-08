package main

import (
	"fmt"
	"reflect"
)

func main() {
	for i := reflect.Invalid; i <= reflect.UnsafePointer; i++ {
		fmt.Printf("%d:%s\n", i, i)
	}

	type A1 struct {
		a int
		b int8
		c int8
	}
	type A2 struct {
		a int8
		b int
		c int8
	}
	var s1 A1
	var s2 A2
	fmt.Printf("struct size: %d:%d\n", reflect.TypeOf(s1).Size(), reflect.TypeOf(s2).Size())
	// struct size: 16:24 存疑
}
