# 表达式： 一条具有明确执行结果的代码语句 如：1+1 name = "张三"
print("1*1的结果是：%d" % (1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))


name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stck_price_daily_growth_factor = 1.2
growth_days = 7

finally_stck_price = stock_price * stck_price_daily_growth_factor ** growth_days

print(f"公司：{name}，股票代码：{stock_code}，当前股价{stock_price}")
print("每日增长系数：%.1f，经过%d天的增长后，股价达到了:%.2f" % (stck_price_daily_growth_factor,growth_days,finally_stck_price))