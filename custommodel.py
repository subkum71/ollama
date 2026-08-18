## Customise the model by adding a model file, Making New Model based on existing .
# """ --> Used for multiline string 
## TODO--> Need to work on it
import requests
import ollama
import subprocess
modelFile = """
FROM qwen3-vl:4b

SYSTEM You work like an IT Project Manager.

Your responsibilities:
- Help with IT project planning and delivery.
- Provide guidance on Agile, Scrum, PMP, and risk management.
- Explain technical concepts clearly.
- Highlight risks, assumptions, and recommended actions.

PARAMETER temperature 0.5
"""

# Create Modelfile
with open("Modelfile", "w") as file:
    file.write(modelFile)

# Create customized Ollama model
subprocess.run(
    ["ollama", "create", "subkum", "-f", "Modelfile"],
     capture_output=True,
    check=True
)
print("Model created successfully")
res = ollama.generate(model="subkum", prompt="Why IT project failed")
print(res["response"])