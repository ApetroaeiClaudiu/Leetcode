SELECT distinct 
    logs1.num as ConsecutiveNums 
FROM 
    logs logs1,
    logs logs2,
    logs logs3
WHERE 
    logs1.id = logs2.id+1 AND 
    logs2.id = logs3.id+1 AND 
    logs1.num = logs2.num AND 
    logs2.num = logs3.num
