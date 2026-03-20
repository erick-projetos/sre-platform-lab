package main

import (
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	requests = prometheus.NewCounter(
		prometheus.CounterOpts{
			Name: "auth_requests_total",
			Help: "Total number of requests to auth service",
		},
	)

	requestDuration = prometheus.NewHistogram(
		prometheus.HistogramOpts{
			Name:    "auth_request_duration_seconds",
			Help:    "Request latency",
			Buckets: prometheus.DefBuckets,
		},
	)
)

func authHandler(w http.ResponseWriter, r *http.Request) {
	start := time.Now()

	requests.Inc()

	time.Sleep(100 * time.Millisecond)

	duration := time.Since(start).Seconds()
	requestDuration.Observe(duration)

	w.Write([]byte("Auth service running"))
}

func main() {

	prometheus.MustRegister(requests)
	prometheus.MustRegister(requestDuration)

	http.HandleFunc("/", authHandler)

	// endpoint de métricas
	http.Handle("/metrics", promhttp.Handler())

	http.ListenAndServe(":8001", nil)
}
