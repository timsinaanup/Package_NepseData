What is this Package For?

   This Package provides live data of Nepal Share Index.
   Including last Transaction Price, It provides Close Price, Open, High, Low and Volume .

For Single Stock Detail:
 - Import this Package
        import NepseData as nd
 
 - Now call a method named get_data as below:
        nd.get_data("NABIL")
    
    OUTPUT:
        ({'ticker': 'NABIL'},
        {'last_transaction_price': 804.0},
        {'Change in Points': -4.0},
        {'Percentage_Change': -0.5},
        {'Opening Price': 815.0},
        {'High': 815.0},
        {'Low': 803.5},
        {'Volume': 58542.0})

For Multiple Stock Data:
    - Import this Package
        import NepseData as nd

    -Create a list of stocks and empty list for appending data
        StockList = ["ADBL","JBBL","SHINE"]
        StockData = []

    - Going through stocks and appending each data in empty list:
        for stock in StockList:
            StockData.append(nd.get_data(stock))

    - Printing Collected data
        print(StockData)
    
    OUTPUT: 
        [({'ticker': 'ADBL'}, {'last_transaction_price': 310.0}, {'Change in Points': -1.1}, {'Percentage_Change': -0.35}, {'Opening Price': 312.0}, {'High': 313.0}, {'Low': 309.0}, {'Volume': 14709.0}),
         ({'ticker': 'JBBL'}, {'last_transaction_price': 274.0}, {'Change in Points': -1.0}, {'Percentage_Change': -0.36}, {'Opening Price': 270.0}, {'High': 276.5}, {'Low': 270.0}, {'Volume': 4740.0}), 
         ({'ticker': 'SHINE'}, {'last_transaction_price': 325.3}, {'Change in Points': -3.7}, {'Percentage_Change': -1.12}, {'Opening Price': 333.8}, {'High': 333.8}, {'Low': 325.0}, {'Volume': 30419.0})]
