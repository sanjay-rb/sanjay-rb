from app import app

@app.errorhandler(404)
def not_found(e):
  return '404'