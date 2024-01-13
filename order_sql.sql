with tick as
(select symbol,lastPrice,askPrice1,bidPrice1,datetime,
substr(cast(datetime as string),1,16) as  minute,
volume,
case when lastPrice=askPrice1 then (volume-lag(volume,1,volume) over(partition by symbol order by datetime)) else 0 end bidVolume,
case when lastPrice=bidPrice1 then (volume-lag(volume,1,volume) over(partition by symbol order by datetime)) else 0 end askVolume,
lag(volume,1,volume) over(partition by symbol order by datetime),
(volume-lag(volume,1,volume) over(partition by symbol order by datetime))
from ticket
order by datetime ),
tick2 as (select 
symbol,
minute,
max(lastPrice) over (partition by symbol, minute) as maxPrice,
min(lastPrice) over (partition by symbol, minute) as minPrice,
first_value(lastPrice) over(partition by symbol, minute order by datetime ) as openPrice,
last_value(lastPrice) over(partition by symbol, minute order by datetime ) as closePrice,
lastPrice as Price,
bidVolume,
askVolume
from tick)
select 
symbol,
minute,
Price,
max(maxPrice) as maxPrice,
max(minPrice) as minPrice,
max(openPrice) as openPrice,
max(closePrice) as closePrice,
sum(bidVolume) as bidVolume,
sum(askVolume) as askVolume
from tick2
group by 1,2,3
order by 1,2,3
