package main

import (
	"encoding/json"
	"log"
	"net/http"
)

func healthHandler(w http.ResponseWriter, r *http.Request) {
	response := map[string]string{
		"status":  "ok",
		"service": "auth-service",
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {

	http.HandleFunc("/health", healthHandler)

	log.Println("Auth service running on port 8001")

	err := http.ListenAndServe(":8001", nil)
	if err != nil {
		log.Fatal(err)
	}
}
