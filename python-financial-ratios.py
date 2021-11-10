#!/usr/bin/python3
import numpy as np
import pandas as pd

#Company info
comapany="e-con systems India pvt ltd,chennai"
year="2019"

#current
current_liabilities=174808172
current_assets=309645001
inventory=15179024
Short_term_receivables=111637933
trade_payables=54862321


#debt/borrow/loans
short_term_debt=25172420 + 54862321 + 1950267
long_term_debt=0
total_assets=330155124
share_capital=1835160
Reserves=153511792
fixed_assets= 4819616 + 509892


#p&l
total_revenue=817423516
total_revenue_operations=783167536
other_income=34255980
goods_cost=159743992
purchase_trade_stock=250654998
employee_benefits=225833660
financial_cost=5756631
other_cost=92092717

direct_expenses= goods_cost + purchase_trade_stock 
indirect_expenses= employee_benefits + financial_cost + other_cost
profit_before_tax=81458738
total_expenses=735964778
net_profit_loss=75242874
interest=10 * short_term_debt / 100

non_current_assets=total_assets-current_assets
total_debt = short_term_debt + long_term_debt
total_equity = share_capital + Reserves 



def company_details():
    print("Company:",comapany)
    print("Financial Year:",year)

#Current ratio = Current Assets / Current Liabilities
#Quick Ratio = (Cash + Marketable Securities + Receivables) / Current Liabilities
#Cash ratio = (Cash + Short Term Marketable Securities) / Current Liabilities
#Working Capital = Current Assets – Current Liabilities

def liquidity_ratios():
    current_ratio = current_assets / current_liabilities
    quick_ratio =  ( current_assets - inventory ) / current_liabilities
    cash_ratio = ( current_assets - inventory - Short_term_receivables ) / current_liabilities
    working_capital = current_assets - current_liabilities

    print("current ratio:",current_ratio)
    print("Quick ratio:",quick_ratio)
    print("Working Capital:",working_capital)

    if current_ratio < 1:
        print("Current Ratio is less than 1:Running out of cash issues / problems")
        print("Organizatio Category:Bad Organizations")
    elif current_ratio >= 1 and current_ratio < 2:
        print("Current Ratio is less than 2:Running out of cash issues / problems")
        print("Organization Category:entrapped Organizations")
    elif current_ratio >=2 and current_ratio <=3:
        print("Current Ratio is good")
    else:
        print("Current Ratio is too high, suspicous point")
    
    if quick_ratio < 1:
        print("Quick Ratio is less than 1: Running out of cash issues / problems")
    elif quick_ratio >=1 and quick_ratio <=2:
        print("Quick Ratio is good")
    else:
        print("Quick Ratio is too high, suspicous point")

    if working_capital < 0:
        print("Organization Category : Credibility Trap")
        print("Current Assets(CA) are less than Current liabilities(CL)")


#Debt to equity = Total debt / Total equity 
#Debt to assets = Total debt / Total assets 
#Assets to equity = Total assets / total equity
#Interest coverage ratio = Operating income (or EBIT) / Interest expense 

#leverage ratios
def solvencty_ratios():
    debt_to_equity = total_debt / total_equity
    debt_to_asset = total_debt / total_assets
    asset_to_equity = total_assets / total_equity
    int_coverage_ratio= (total_revenue-total_expenses)/interest

    print("debt_to_equity:",debt_to_equity)
    print("debt_to_asset:",debt_to_asset)
    print("asset to equity:",asset_to_equity)
    print("Int coverage ratio:",int_coverage_ratio)
    if debt_to_equity < 1 :
        print("debt_to_equity less than 1: is good")
    else:
        print("debt_to_equity more than 1:  is bad")

    if debt_to_asset < 0.5 :
        print("debt_to_asset less than 0.5 :is good")
    else:
        print("debt_to_asset more than 0.5 : is bad")

    if int_coverage_ratio <= 2:
        print("Int coverage ratio : is less than 2: bad")
    else:
        print("Int coverage ratio : is more than 3: good")
           
#Net Income / Total Assets = Return on Assets %
#Net Income / Average Shareholder’s Equity = Return on Equity %
#Net Operating Profit ÷ Capital Employed × 100 
#Capital Employed = Equity share capital, Reserve and Surplus, Debentures    
#and long-term Loans Capital Employed = Total Assets – Current Liability

# Formula: Gross Profit ÷ Sales × 100 
#Gross Profit= Sales + Closing Stock – op stock – Purchases – Direct Expenses
# direct_expnses

#Net Profit ÷ Sales × 100 
#Net Profit = Gross Profit + Indirect Income – Indirect Expenses 
# direct_expenses + indirect expenses

#PAT = net_profit == PAT (botoom line)/ Sales(top line) * 100

def profitability_ratios():
    Return_on_assets= ( net_profit_loss / total_assets )* 100
    Return_on_equity= ( net_profit_loss / total_equity ) * 100
    Return_on_capital_employed= (net_profit_loss / ( total_equity + total_debt ))*100

    gross_profit = ((total_revenue - other_income - direct_expenses)/ (total_revenue - other_income)) * 100
    operation_profit = ((total_revenue - other_income - direct_expenses - indirect_expenses)/ (total_revenue - other_income)) * 100
    pat_profit = (net_profit_loss / (total_revenue - other_income)) * 100

    print("Gross Profit:",gross_profit)
    print("Operation Profit:",operation_profit)
    print("Net Profit: PAT%",pat_profit)
    print("Reurn on Assets(ROA):",Return_on_assets)
    print("Reurn on Equity(ROE):",Return_on_equity)
    print("Reurn on Capital Employed (ROCE):",Return_on_capital_employed)

    if Return_on_assets <= 15:
        print("Reurn on Assets(ROA): less than 15: bad")
    else:
        print("Reurn on Assets(ROA): more than 15: good")
    
    if Return_on_equity <= 15:
        print("Reurn on Equity(ROE): less than 15: bad")
    else:
        print("Reurn on Equity(ROE): more than 15: good")
    
    if Return_on_capital_employed <= 15:
        print("Reurn on Capital Employed (ROCE): less than 15: bad")
    else:
        print("Reurn on Capital Employed (ROCE): more than 15: good")

#total asset turn-over ratio
def efficiency_ratios():
    total_asset_turn_over= ((total_revenue - other_income ) /total_assets)
    fixed_asset_turn_over= ((total_revenue - other_income ) /fixed_assets)
    days_inventory = 365 / ((total_revenue - other_income ) /inventory)
    days_receivables = 365 / ((total_revenue - other_income)/Short_term_receivables)
    days_payables = 365 / ((total_revenue - other_income)/trade_payables)
    
    print("Total Asset Turnover:",total_asset_turn_over)
    print("Fixed Asset Turnover:",fixed_asset_turn_over)
    print("Days of Inventory:",days_inventory)
    print("Days Receivables :",days_receivables)
    print("Days Payables :",days_payables)


if __name__ == "__main__":
    company_details()
    liquidity_ratios()
    solvencty_ratios() #levearge ratios
    profitability_ratios()
    efficiency_ratios()
