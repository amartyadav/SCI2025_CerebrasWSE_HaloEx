import json
from cerebras.sdk.client import SdkCompiler


with SdkCompiler() as compiler:
    artifact_path = compiler.compile(
        ".",
        "layout.csl",
        "-arch=wse3 --fabric-dims=762,1172 --fabric-offsets=4,1 --params=M:6,N:6 -o out --max-inlined-iterations=1000000 --memcpy --channels 1",
        "."
    )

# Write the artifact_path to a JSON file
with open("artifact_path.json", "w", encoding="utf8") as f:
    json.dump({"artifact_path": artifact_path,}, f)
