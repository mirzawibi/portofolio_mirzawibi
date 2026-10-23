import asyncio
import json
import base64
import urllib.request
import subprocess
import time
import os
import websockets

async def main():
    # Launch Edge with remote debugging
    proc = subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless=new",
        "--disable-gpu",
        "--remote-debugging-port=9222",
        "http://127.0.0.1:8000/"
    ])
    await asyncio.sleep(2)

    try:
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read())
        page_tab = next(t for t in tabs if "Muhammad Mirza" in t["title"] or "127.0.0.1:8000" in t["url"])
        ws_url = page_tab["webSocketDebuggerUrl"]
        print("Connected to:", ws_url)

        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            async def send_cmd(cmd_id, method, params=None):
                payload = {"id": cmd_id, "method": method}
                if params:
                    payload["params"] = params
                await ws.send(json.dumps(payload))
                while True:
                    raw = await ws.recv()
                    data = json.loads(raw)
                    if data.get("id") == cmd_id:
                        return data

            # Enable Page
            await send_cmd(1, "Page.enable")
            
            # Set Metrics
            await send_cmd(2, "Emulation.setDeviceMetricsOverride", {
                "width": 1280, "height": 900, "deviceScaleFactor": 1, "mobile": False
            })

            js_query = """
            (() => {
                const results = {};
                for (const sec of document.querySelectorAll('section, footer')) {
                    const r = sec.getBoundingClientRect();
                    results[sec.id || sec.tagName] = {
                        top: r.top + window.scrollY,
                        height: r.height,
                        visible: r.height > 0
                    };
                }
                return results;
            })()
            """

            # Evaluate layout
            res = await send_cmd(3, "Runtime.evaluate", {
                "expression": js_query, "returnByValue": True
            })
            print("Section Layout:", json.dumps(res.get("result", {}).get("result", {}).get("value", {}), indent=2))

            # Capture Screenshot
            shot_res = await send_cmd(4, "Page.captureScreenshot", {
                "format": "png", "captureBeyondViewport": True
            })
            img_data = base64.b64decode(shot_res["result"]["data"])
            
            artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\5dfb1928-4f07-46b8-84bd-e62d15786eb5"
            out_file = os.path.join(artifact_dir, "preview_dark_urban_full_clean.png")
            with open(out_file, "wb") as f:
                f.write(img_data)
            print(f"Full page screenshot saved to {out_file} (Size: {len(img_data)} bytes)")

    finally:
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(main())
