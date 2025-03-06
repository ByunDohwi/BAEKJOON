SELECT FI.ID, FNI.FISH_NAME, FI.LENGTH
FROM FISH_INFO AS FI
JOIN FISH_NAME_INFO AS FNI ON FI.FISH_TYPE = FNI.FISH_TYPE
WHERE FI.LENGTH = (SELECT MAX(LENGTH) FROM FISH_INFO WHERE FISH_TYPE = FI.FISH_TYPE)
ORDER BY ID;