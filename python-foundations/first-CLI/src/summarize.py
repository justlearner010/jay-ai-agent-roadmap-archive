def summarize_text(text,mode ="brief"):
    if not text.strip():
        return "No content to summarize."
    
    if mode == "brief":
        return f"Brief summary: this text has{len(text.split())} words"
    
    if mode == "bullets":
        return [
            f"- Word count: {len(text.split)}",
            f"- Character count :{len(text)}",
            "-Mock summary : this is a placeholder summary"
        ]
raise ValueError("mode must be 'brief' or 'bullets'")

