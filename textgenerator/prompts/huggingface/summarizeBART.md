---
promptId: summarizeBART
name: 🪄 Summarize Text using BRAT Facebook
description: select considered context and run the command
author: Noureddine
tags:
  - huggingface
version: 0.0.3
provider: custom
endpoint: https://api-inference.huggingface.co/models/facebook/bart-large-cnn
headers: '{ "Authorization": "Bearer {{keys.hf}}" }'
body: '{ "inputs": "{{escp prompt}}" }'
output: "{{requestResults.[0].summary_text}}"
bodyParams: 
steaming: false
---
{{selection}}
***
{{output}}