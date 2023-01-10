import pyautogui
import pyperclip
import pandas
import numpy
import openpyxl
import time

pyautogui.PAUSE = 1


# Step 1: Enter the company's system

pyautogui.hotkey('ctrl', 'alt', '0') # Open the browser
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Step 2: Navigate to the report location

time.sleep(3) # Waiting time in seconds
pyautogui.click(x=519, y=416, clicks=2)

# Step 3: Export the report

time.sleep(3)
pyautogui.click(x=609, y=500)
pyautogui.click(x=1609, y=236)
pyautogui.click(x=1286, y=843)

#Step 4: Calculate the indicators (income and quantity of products)

time.sleep(3)
tabela = pandas.read_excel(r'C:\Users\andre\Downloads\Vendas - Dez.xlsx')

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Step 5: Send an e-mail to board of directors

time.sleep(3)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/?ogbl#inbox') # Enter my email
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=123, y=255) # Click to write email
pyautogui.write('andreluis0703@gmail.com')
pyautogui.press('enter')
pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = """
Dears, good morning!

Yesterday's billing was: R${faturamento:,.2f}
The number of products was: R${quntidade:,}

SY, André Ramos
"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
