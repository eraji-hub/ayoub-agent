from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# تحميل النموذج مرة واحدة
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/phi-3-mini")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/phi-3-mini")
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

def analyze_data(target, texts):
    prompt = f"""
    قم بتحليل المعلومات التالية عن {target} واستخرج:
    - Founders
    - Partners
    - Contacts
    - ملخص شامل
    - أي علاقات مهمة بين الأشخاص أو الشركات

    البيانات:
    {''.join(texts[:5])}
    """
    result = llm_pipeline(prompt, max_length=500)[0]['generated_text']
    return result
