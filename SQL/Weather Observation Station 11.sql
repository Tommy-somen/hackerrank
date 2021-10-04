select distinct city from station where (lower(substr(city,1,1)) not in ('a','i','u','e','o')) or
(lower(substr(city,length(city),length(city))) not in ('a','i','u','e','o'));
