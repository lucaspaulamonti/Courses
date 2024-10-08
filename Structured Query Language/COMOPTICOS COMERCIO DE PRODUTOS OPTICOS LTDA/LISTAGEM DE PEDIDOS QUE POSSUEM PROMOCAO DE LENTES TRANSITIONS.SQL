SELECT
    DISTINCT
        PEDID.EMPCODIGO,
        PEDID.PEDDTEMIS,
        PEDID.ID_PEDIDO,
        PEDID.PEDCODIGO,
        PEDID.CLICODIGO,

        CLIEN.CLIRAZSOCIAL,
		
        PEDID.PEDSITPED,
        PEDID.TPCODIGO,
        PEDID.FISCODIGO1,
        PEDID.PDFCODIGO,
        PEDID.PEDVRTOTAL
		
FROM PEDID
    LEFT JOIN PDPRD ON PEDID.ID_PEDIDO = PDPRD.ID_PEDIDO
    LEFT JOIN PRODU ON PDPRD.PROCODIGO = PRODU.PROCODIGO
    LEFT JOIN PEDIDPROMO ON PEDID.ID_PEDIDO  = PEDIDPROMO.ID_PEDIDORIGINAL
                         OR  PEDID.ID_PEDIDO = PEDIDPROMO.ID_PEDIDPROMOCAO
    LEFT JOIN CLIEN ON PEDID.CLICODIGO = CLIEN.CLICODIGO
	
WHERE
    PEDID.PEDDTEMIS BETWEEN *@#DATE#DATAINICIAL@ AND @#DATE#DATAFINAL@
    AND PEDID.PEDSITPED != 'C'
    AND PRODU.GLCODIGO = 'T'
    AND (
            (
                PEDID.ID_PEDIDO = PEDIDPROMO.ID_PEDIDORIGINAL
             )

            OR

            (
                PEDID.ID_PEDIDO = PEDIDPROMO.ID_PEDIDPROMOCAO
                AND PEDIDPROMO.ID_PROMO NOT IN (
                    SELECT PROMO.ID_PROMO FROM PROMO
                    WHERE PROMO.DESCRICAO LIKE '%EM DROBO%'
                    )
             )

            OR

            (
                PEDIDPROMO.ID_PEDIDPROMO IS NULL
             )
        )
		
ORDER BY
    PEDID.EMPCODIGO,
    PEDID.ID_PEDIDO
;
