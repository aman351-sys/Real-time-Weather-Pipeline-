SELECT * FROM public.weather_records_8july

-- 1) ALERT OPERATIONAL 
 select distinct city,temperature,wind_speed ,
 case 
 when temperature >= 28 and wind_speed >= 18 then 'high heat and risk'
 when wind_speed >15 then 'high wind speed'
 when temperature > 29 then 'exreame heat wave '
 else 'clear'
 end as risk_flag
from weather_records_8august 
 
order by wind_speed desc , time_saved  desc ;
 




-- 2) CITY ON WIND RANK 

with min_operation as (
select city ,
DATE_TRUNC('minute', time_saved::timestamp) as op_min ,
round(avg(wind_speed):: numeric,2) as avg_windspeed 
from weather_records_8august
group by city , DATE_TRUNC('minute', time_saved::timestamp) 
),
ranked as (select city,op_min,avg_windspeed,
dense_rank() over(  partition by op_min order by  avg_windspeed desc) as wind_rank
from min_operation 
) select city,op_min,avg_windspeed,wind_rank from ranked ;








 




