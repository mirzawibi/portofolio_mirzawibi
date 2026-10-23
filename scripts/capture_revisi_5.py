import asyncio
import json
import base64
import urllib.request
import subprocess
import os

async def main():
    artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\5dfb1928-4f07-46b8-84bd-e62d15786eb5"
    os.makedirs(artifact_dir, exist_ok=True)

    edge_cmd = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless=new",
        "--disable-gpu",
        "--remote-debugging-port=9224",
        "http://127.0.0.1:8000/?skip_intro=1"
    ]
    proc = subprocess.Popen(edge_cmd)
    await asyncio.sleep(2.5)

    try:
        import websockets
        tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9224/json").read())
        page_tab = next(t for t in tabs if "Muhammad Mirza" in t["title"] or "127.0.0.1:8000" in t["url"])
        ws_url = page_tab["webSocketDebuggerUrl"]
        print("Connected to:", ws_url)

        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            cmd_counter = 0
            async def send_cmd(method, params=None):
                nonlocal cmd_counter
                cmd_counter += 1
                payload = {"id": cmd_counter, "method": method}
                if params:
                    payload["params"] = params
                await ws.send(json.dumps(payload))
                while True:
                    raw = await ws.recv()
                    data = json.loads(raw)
                    if data.get("id") == cmd_counter:
                        return data

            await send_cmd("Page.enable")
            await send_cmd("DOM.enable")
            await send_cmd("Emulation.setDeviceMetricsOverride", {
                "width": 1280, "height": 900, "deviceScaleFactor": 1, "mobile": False
            })

            # Reveal all items: remove opacity 0 from reveal classes
            await send_cmd("Runtime.evaluate", {
                "expression": """
                (() => {
                    document.querySelectorAll('.reveal').forEach(el => el.classList.add('reveal-visible'));
                    const b = document.getElementById('mirza-bubble');
                    if (b) b.classList.add('active-bubble');
                    const rev = document.getElementById('candle-revelation-message');
                    if (rev) rev.style.opacity = '1';
                })()
                """
            })
            await asyncio.sleep(0.5)

            clip_eval = """
            (() => {
                const getBox = (el) => {
                    if (!el) return null;
                    const r = el.getBoundingClientRect();
                    return {
                        x: Math.max(0, r.left + window.scrollX),
                        y: Math.max(0, r.top + window.scrollY),
                        width: r.width,
                        height: r.height,
                        scale: 1
                    };
                };

                const heroSec = document.querySelector('#tentang');
                const uspSec = document.querySelector('.usp-enhanced-grid')?.closest('section');
                const gateway = document.querySelector('.urban-traffic-gateway-avenue');
                const timelineSec = document.querySelector('.transit-metro-timeline')?.closest('section');
                const footerSec = document.querySelector('footer');

                return {
                    hero: getBox(heroSec),
                    nilai_tambah: getBox(uspSec),
                    gateway: getBox(gateway),
                    timeline: getBox(timelineSec),
                    footer: getBox(footerSec)
                };
            })()
            """
            res = await send_cmd("Runtime.evaluate", {"expression": clip_eval, "returnByValue": True})
            boxes = res.get("result", {}).get("result", {}).get("value", {})
            print("Boxes detected:", list(boxes.keys()))

            async def capture_box(box, filename):
                if not box or box["width"] <= 0 or box["height"] <= 0:
                    print(f"Skipping {filename}")
                    return
                shot = await send_cmd("Page.captureScreenshot", {
                    "format": "png",
                    "clip": {
                        "x": float(box["x"]),
                        "y": float(box["y"]),
                        "width": float(box["width"]),
                        "height": float(box["height"]),
                        "scale": 1
                    },
                    "captureBeyondViewport": True
                })
                img_bytes = base64.b64decode(shot["result"]["data"])
                out_path = os.path.join(artifact_dir, filename)
                with open(out_path, "wb") as f:
                    f.write(img_bytes)
                print(f"Captured {filename} ({len(img_bytes)} bytes)")

            await capture_box(boxes.get("hero"), "preview_hero_revisi_5.png")
            await capture_box(boxes.get("nilai_tambah"), "preview_nilai_tambah_revisi_5.png")
            await capture_box(boxes.get("gateway"), "preview_gateway_traffic_5.png")
            await capture_box(boxes.get("timeline"), "preview_timeline_metro_5.png")
            await capture_box(boxes.get("footer"), "preview_footer_revisi_5.png")

    finally:
        proc.terminate()
        print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
