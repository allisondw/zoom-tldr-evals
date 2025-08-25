import json, subprocess, time, pathlib, sys
cmd = ["python","-m","evals.cli.oaieval","cot/gpt-3.5-turbo","Chinese_character_riddles.dev.v0"]
ts=time.strftime("%Y%m%d-%H%M%S")
out=pathlib.Path("reports"); out.mkdir(exist_ok=True)
p=subprocess.run(cmd, capture_output=True, text=True)
log=out/f"riddles_{ts}.json"
log.write_text(json.dumps({"cmd":" ".join(cmd),"rc":p.returncode,"stdout":p.stdout,"stderr":p.stderr,"ts":ts}, indent=2))
print(f"Wrote {log} rc={p.returncode}")
sys.exit(0)
