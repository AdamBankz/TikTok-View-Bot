import requests, time, json, urllib.parse, random, threading

VIDEO = "6930717658832833798"
IID = "7522059562116957969"
DID = "7522057963538187792"



def view(video):
    try:
        version = random.choice([247, 312, 322, 357, 358, 415, 422, 444, 466])
        device = random.choice([
            "SM-G9900", "sm-g950f", "SM-A136U1", "SM-M225FV", "SM-E426B", 
            "SM-M526BR", "SM-M326B", "SM-A528B", "SM-F711B", "SM-F926B", 
            "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B", "SM-A525F"
        ])
        host = random.choice([
            "api16.tiktokv.com", "api.tiktokv.com", 
            "api19.tiktokv.com", "api21.tiktokv.com"
        ])
        params = urllib.parse.urlencode({
            "app_language": "fr",
            "iid": IID,
            "device_id": DID,
            "channel": "googleplay",
            "device_type": device,
            "ac": "wifi",
            "os_version": random.randint(5, 11),
            "version_code": version,
            "app_name": "trill",
            "device_brand": "samsung",
            "ssmix": "a",
            "device_platform": "android",
            "aid": 1180,
            "as": "a1iosdfgh",
            "cp": "androide1",
        })

        # Choose a random proxy for this request
        proxy = random.choice(proxy_pool)

        response = requests.post(
            url=f"https://{host}/aweme/v1/aweme/stats?{params}",
            data=(
                f"&manifest_version_code={version}"
                f"&update_version_code={version}0"
                "&play_delta=1"
                f"&item_id={video}"
                f"&version_code={version}"
                "&aweme_type=0"
            ),
            headers={
                "host": host,
                "connection": "keep-alive",
                "accept-encoding": "gzip",
                "x-ss-req-ticket": str(int(time.time())),
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": f"com.ss.android.ugc.trill/{version} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)"
            },
        )

        print(response.json())
    except Exception as e:
        print("Error:", e)

while True:
    if threading.active_count() < 500:
        threading.Thread(target=view, args=[VIDEO]).start()
