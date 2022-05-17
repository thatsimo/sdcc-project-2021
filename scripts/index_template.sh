#!/usr/bin/env bash

curl -X PUT "localhost:9200/_index_template/tweets-location" -H 'Content-Type: application/json' -d'
{
  "template": {
    "mappings": {
      "properties": {
        "coordinates": {
          "type": "geo_point"
        }
      }
    }
  },
  "index_patterns": [
    "tweets"
  ]
}
'
