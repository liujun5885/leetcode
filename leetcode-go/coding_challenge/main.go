package main

import (
	"fmt"
	log "github.com/sirupsen/logrus"
	"os"
	"sync"
)

type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func (c *Container) get(name string) int {
	return c.counters[name]
}

func initApp() {
	log.SetFormatter(&log.TextFormatter{
		FullTimestamp: true,
	})
	log.SetReportCaller(true)
	log.SetOutput(os.Stdout)
	log.SetLevel(log.DebugLevel)
}

func main() {
	//runtime.GOMAXPROCS(2)

	initApp()

	c := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
			//log.Info(fmt.Sprintf("increase key: %s, value: %d, pid: %d", name, c.get(name), os.Getpid()))
		}
		wg.Done()
	}

	wg.Add(4)
	go doIncrement("a", 100)
	go doIncrement("a", 100)
	go doIncrement("b", 100)
	go doIncrement("b", 100)

	wg.Wait()
	fmt.Println(c.counters)
}
