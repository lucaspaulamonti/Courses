# Triggers:
SELECT RDB$TRIGGER_NAME
FROM RDB$TRIGGERS
WHERE RDB$SYSTEM_FLAG = 0
ORDER BY 1
;

# Procedures:
SELECT RDB$PROCEDURE_NAME
FROM RDB$PROCEDURES
WHERE RDB$SYSTEM_FLAG = 0
ORDER BY 1
;

# Tables:
SELECT RDB$RELATION_NAME
FROM RDB$RELATIONS
WHERE COALESCE(RDB$SYSTEM_FLAG, 0) = 0
AND RDB$RELATION_TYPE = 0
ORDER BY 1
;

# Versão do Firebird:
SELECT RDB$GET_CONTEXT('SYSTEM', 'ENGINE_VERSION') FROM RDB$DATABASE;
