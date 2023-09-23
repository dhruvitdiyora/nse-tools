# nse-tools
List of scripts to fetch data from nseindia

1. fii-dii-data-fetch.py - to download fii dii clients daily activity csv
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   Client - Retail Investors like you and me

    DII - Domestic Institutional Investors - Local mutual funds, insurance companies, local pension funds, and banking and financial institutions. For example : LIC
         DII does not actively participate in FnO. They provide the initial liquidity. So does not matter much anyways.
    
    FII - Foreign Institutional Investors - Investment fund or an investor based outside of a nation who invests in that nation’s assets. They can be anything from Hedge Funds, Foreign Mutual Funds,Sovereign Wealth Funds, Pension Funds.
    
    PROs - Prop Traders - Traders who trades stocks, bonds, currencies, commodities, their derivatives, or other financial instruments with the firm's own money. The main difference between the Institutions and Prop traders is that Institutions invest the clients' money and take a share of profit out of it whereas PROs use their own money and keep the whole profit.
    
    OI - The total number of outstanding derivative contracts, such as options or futures that have not been settled.
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   It consists of all the current positions the market players have

    After that it is just basic number crunching
    
    I keep yesterday's data and today's data. Calculate the total positions of Today's Index Options. 
    Consider + means long, and - means short.
    We know long call = long, short call = short
    long put = short, short put = long
    
    So to calculate the total positions, first calculate the total calls i.e. Index Call Options Long  - Index Call Options Short
    If the number comes out to be -ve , it means that call was shorted more than it was longed. And if it is +ve then call longs were more than call shorts. 
    
    Same with total puts i.e. Index Put Options Long  - Index Put Options Short
    If the number comes out to be -ve , it means that put was shorted more than it was longed. And if it is -ve, then put longs were more than put shorts. 
    
    Then to calculate the Total Index Options, 
    Subtract the number of total calls and total puts that we calculated earlier. i.e "total calls - total puts"
    
    Now if the number comes out to be -ve, then we are short as "Total Puts is greater than Total Calls" where either
    Puts were bought in loads making the second variable +ve
    OR
    Calls were shorted to the ground making the first variable -ve by a margin
    Or both
    
    Now if the number comes out to be +ve, then we are long as "Total Calls is greater than Total Puts" where either
    Calls were bought in loads making the first variable +ve
    OR
    Puts were shorted to the ground making the second variable -ve by a margin and thus adding it by simple maths
    OR
    
    Or both*
    
    Then for Net, It is TODAY's Total Index Options - YESTERDAYS's Total Index Options
   ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

