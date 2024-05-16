select ID , CASE WHEN NTILE(4) over (order by SIZE_OF_COLONY desc) = 1 then 'CRITICAL'
WHEN NTILE(4) over (order by SIZE_OF_COLONY desc) = 2 then 'HIGH'
WHEN NTILE(4) over (order by SIZE_OF_COLONY desc) = 3 then 'MEDIUM'
else 'LOW' END as COLONY_NAME
from ecoli_data

order by ID