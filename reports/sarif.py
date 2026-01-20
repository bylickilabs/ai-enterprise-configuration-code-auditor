def export_sarif(scan_result: dict) -> dict:
    return {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "AI Enterprise Configuration & Code Auditor"
                }
            },
            "results": [
                {
                    "level": f["severity"].lower(),
                    "message": {"text": f["message"]},
                    "locations": [{
                        "physicalLocation": {
                            "artifactLocation": {
                                "uri": f["file"]
                            }
                        }
                    }]
                }
                for f in scan_result["findings"]
            ]
        }]
    }