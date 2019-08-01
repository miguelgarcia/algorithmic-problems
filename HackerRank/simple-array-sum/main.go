package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func sumArray(items []int) int {
	var total int
	for _, v := range items {
		total += v
	}
	return total
}

func main() {
	// Build input reader
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	// Build output writer
	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)
	defer stdout.Close()
	writer := bufio.NewWriterSize(stdout, 1024*1024)

	readLine(reader)
	itemsLine := readLine(reader)
	itemsStr := strings.Split(itemsLine, " ")
	items := make([]int, len(itemsStr))
	for i, v := range itemsStr {
		val, err := strconv.ParseInt(v, 10, 64)
		if err != nil {
			panic(err)
		}
		items[i] = int(val)
	}

	result := sumArray(items)
	fmt.Fprintf(writer, "%d\n", result)
	writer.Flush()
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
