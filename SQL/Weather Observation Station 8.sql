select distinct city from station where (lower(substr(city,1,1)) in ('a','i','u','e','o')) and
(lower(substr(city,length(city),length(city))) in ('a','i','u','e','o'));
