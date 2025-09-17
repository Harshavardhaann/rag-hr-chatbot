import pdfplumber, json

def extract_pdf(pdf_path, out_jsonl):
    docs = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            docs.append({"page": i, "text": text.strip()})
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps(d) + "\n")

if __name__ == "__main__":
    extract_pdf("data/HR-Policy.pdf", "data/docs.jsonl")

