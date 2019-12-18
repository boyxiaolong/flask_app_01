from app import app

@app.add_template_filter
def allentruncate(str):
    return str[:4]
