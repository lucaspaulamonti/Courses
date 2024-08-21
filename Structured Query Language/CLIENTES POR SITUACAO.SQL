SELECT
     CLIEN.CLICODIGO
    ,CLIEN.CLICNPJCPF
    ,CLIEN.CLIRAZSOCIAL
    ,CLINET.NETENDERECO
    ,ENDCLI.ENDENDERECO
    ,ENDCLI.ENDNR
    ,ENDCLI.ENDCOMPLE
    ,CIDADE.CIDNOME
    ,CIDADE.CIDUF

    ,CASE SITUACAO.SITTIPO
        WHEN 'I' THEN 'INATIVO'
        WHEN 'A' THEN 'ATIVO'
        WHEN 'R' THEN 'RESTRITO'
        WHEN 'B' THEN 'BLOQUEADO'
        ELSE 'ATIVO'
    END AS SITUACAO

FROM
    CLIEN
    LEFT JOIN CLINET    ON CLIEN.CLICODIGO  = CLINET.CLICODIGO
    LEFT JOIN ENDCLI    ON CLIEN.CLICODIGO  = ENDCLI.CLICODIGO
    LEFT JOIN CIDADE    ON ENDCLI.CLICODIGO = CIDADE.CIDCODIGO
    LEFT JOIN SITCLI    ON CLIEN.CLICODIGO  = SITCLI.CLICODIGO
    LEFT JOIN SITUACAO  ON SITCLI.SITCODIGO = SITUACAO.SITCODIGO

WHERE
    (
        (
            (
                SITCLI.SITDATA = (
                                    SELECT MAX(SITCLI2.SITDATA)
                                    FROM SITCLI SITCLI2
                                    WHERE SITCLI2.CLICODIGO = CLIEN.CLICODIGO
                                    )
            )
        AND
            (
                SITCLI.SITSEQ  = (
                                    SELECT MAX(SITCLI3.SITSEQ)
                                    FROM SITCLI SITCLI3
                                    WHERE SITCLI3.CLICODIGO = CLIEN.CLICODIGO
                                    AND SITCLI3.SITDATA = SITCLI.SITDATA
                                    )
            )
        )
    OR (SITCLI.SITCODIGO IS NULL)
    )

ORDER BY
     SITUACAO.SITTIPO
    ,CLIEN.CLICODIGO
;
