import requests

# API Endpoints
SYNC_URL = "https://vocabautomationdotnet.onrender.com/api/Vocab/sync"
SEND_BATCH_URL = "https://vocabautomationdotnet.onrender.com/api/Vocab/send-batch/general_vocabulary"

def trigger_sync():
    try:
        print("🔄 Triggering sync...")
        response = requests.post(SYNC_URL)
        response.raise_for_status()
        print("✅ Sync response:", response.text)
    except Exception as e:
        print("❌ Sync failed:", e)

def trigger_send_batch():
    try:
        print("📦 Sending vocab batch...")
        response = requests.post(SEND_BATCH_URL)
        response.raise_for_status()
        print("✅ Send batch response:", response.text)
    except Exception as e:
        print("❌ Send batch failed:", e)

if __name__ == "__main__":
    trigger_sync()
    trigger_send_batch()
