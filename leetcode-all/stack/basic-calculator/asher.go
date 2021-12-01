package main

import (
	"fmt"
	"github.com/google/go-cmp/cmp"
	"reflect"
	"strconv"
	"strings"
)

func readWord(s string) (string, string, bool) {
	if len(s) == 0 {
		return "", s, false
	}

	switch s[0] {
	case '(', ')':
		return s[:1], s[1:], true
	case '+', '-':
		i := 0
		for i < len(s) && s[i] == '+' || s[i] == '-' {
			i++
		}
		if s[i] >= '0' && s[i] <= '9' {
			j := i
			for j < len(s) && s[j] >= '0' && s[j] <= '9' {
				j++
			}
			return s[i-1 : j], s[j:], true
		} else {
			return s[i-1 : i], s[i:], true
		}
	default:
		i := 0
		for i < len(s) && s[i] >= '0' && s[i] <= '9' {
			i++
		}
		return s[:i], s[i:], true
	}
}

func calculate(s string) int {
	s = strings.Replace(s, " ", "", -1)
	stack := []interface{}{}
	for word, rest, ok := readWord(s); ok; word, rest, ok = readWord(rest) {
		if word == "+" || word == "-" || word == "(" {
			stack = append(stack, word)
		} else if word == ")" {
			val := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			sum := 0
			for reflect.TypeOf(val).Kind() == reflect.Int {
				sum += val.(int)
				val = stack[len(stack)-1]
				stack = stack[:len(stack)-1]
			}
			operator := "+"
			if len(stack) > 0 && reflect.TypeOf(stack[len(stack)-1]).Kind() == reflect.String {
				operator = stack[len(stack)-1].(string)
				stack = stack[:len(stack)-1]
			}

			if operator == "+" {
				stack = append(stack, sum)
			} else {
				stack = append(stack, -1*sum)
			}
		} else {
			v, _ := strconv.Atoi(word)
			if len(stack) > 0 && reflect.TypeOf(stack[len(stack)-1]).Kind() == reflect.String {
				stack = append(stack, v)
			} else {
				v1 := 0
				if len(stack) > 0 {
					v1 = stack[len(stack)-1].(int)
					stack = stack[:len(stack)-1]
				}
				stack = append(stack, v1+v)
			}
		}
	}

	sum := 0
	for _, v := range stack {
		sum += v.(int)
	}

	return sum
}

func main() {
	s := "(1+(4+5+2)-3)+(6+8)"
	output := calculate(s)
	expected := 23
	if !cmp.Equal(output, expected) {
		fmt.Printf("actual: %v != expected: %v\n", output, expected)
	} else {
		fmt.Println("pass")
	}
}
