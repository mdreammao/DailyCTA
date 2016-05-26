import pypyodbc as odbc 
cn = odbc.connect('DSN=CTA;UID=sa;PWD=666666')
cursor = cn.cursor()
sql = 'SELECT top 100 [ttime],[cp],S1,SV1,B1,BV1,ts,OpenInterest,tt FROM [TradeMarket201305].[dbo].[MarketData_RB1310_SHF]'
cursor.execute(sql)
tmp = cursor.fetchall()
cn.close()