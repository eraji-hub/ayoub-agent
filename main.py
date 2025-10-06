from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from utils.web_search import search_web
from utils.scraper import scrape_text
from utils.analyzer import analyze_data
from utils.network_builder import build_network

API_KEY = "ayoub_secret_key"
app = FastAPI(title="Ayoub AI Research Agent")

class AnalyzeRequest(BaseModel):
    target: str

@app.get("/")
def home():
    return {"message": "Ayoub AI Research Agent ✅ Running"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # 1️⃣ البحث عن روابط مرتبطة بالشركة/الشخص
    links = search_web(request.target)

    # 2️⃣ جلب النصوص من الصفحات
    texts = []
    for url in links:
        text = scrape_text(url)
        if text:
            texts.append(text)

    # 3️⃣ تحليل البيانات باستخدام LLM
    analysis_result = analyze_data(request.target, texts)

    # 4️⃣ إنشاء خريطة العلاقات
    network_file = build_network(analysis_result)

    # 5️⃣ إعادة النتائج
    return {
        "target": request.target,
        "analysis": analysis_result,
        "network_graph": network_file
    }
