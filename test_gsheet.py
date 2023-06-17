importt datetime as dt
from fastapi imprort Body
import yfinance as yf
import xlwings as xw
from app import app

@app.post('/hello')
def hello(data: dict = Body(...)):
  book = xw.Book(json=data)
  sheet = book.sheets[0]
  sheet['A1'].value = 'Hello xlwings'
  return book.json()
