select city, length(city) from station where length(city) = (select max(length(city)) from station);
select city, length(city) from (select city, length(city) from station where length(city) = (select min(length(city)) 
from station) order by 1) where rownum = 1;
