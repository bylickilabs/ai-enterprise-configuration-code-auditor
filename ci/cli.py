import argparse
import json
import sys

from analysis.scanner import scan_project
from ci.exit_codes import exit_code_for_risk
from reports.json_export import export_json


def run_cli():
    parser = argparse.ArgumentParser(
        description="AI Enterprise Configuration & Code Auditor – CI Mode"
    )
    parser.add_argument("--zip", required=True, help="Project ZIP file")
    parser.add_argument("--profile", default="BASE", help="Compliance profile")
    parser.add_argument("--lang", default="en", help="Language (de/en)")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    result = scan_project(args.zip, args.profile)

    if args.json:
        print(json.dumps(export_json(result, args.lang), indent=2))

    sys.exit(exit_code_for_risk(result["risk_level"]))