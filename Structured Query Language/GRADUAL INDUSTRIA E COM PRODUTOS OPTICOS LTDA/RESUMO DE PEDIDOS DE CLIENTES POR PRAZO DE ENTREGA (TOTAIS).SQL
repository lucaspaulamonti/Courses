EXECUTE BLOCK
RETURNS (
    TOTALENTREGAS INTEGER,
    QUANTIDADE_DENTRO_PRAZO INTEGER,
    PORCENTAGEM_DENTRO_PRAZO DECIMAL(4,2),
    QUANTIDADE_FORA_PRAZO INTEGER,
    PORCENTAGEM_FORA_PRAZO DECIMAL(4,2)
)
AS
    DECLARE VARIABLE DATA_EMISSAO_INICIAL DATE = @#DATE#DATA_EMISSAO_INICIAL@;
    DECLARE VARIABLE DATA_EMISSAO_FINAL DATE = @#DATE#DATA_EMISSAO_FINAL@;
    DECLARE VARIABLE DATA_ATUAL DATE = CURRENT_DATE;
BEGIN
    FOR

        SELECT
								
            COUNT(*) TOTALENTREGAS,
								
            SUM(
                IIF(
                    PEDID.PEDPZENTRE >=
                    IIF(
                        PEDID.PEDDTSAIDA IS NOT NULL,
                        PEDID.PEDDTSAIDA, CAST(:DATA_ATUAL AS TIMESTAMP)
                    ), 1, 0
                ) 
            ) ENTREGADENTROPRAZO,
												
            (
                SUM(
                    IIF(
                        PEDID.PEDPZENTRE >=
                        IIF(
                            PEDID.PEDDTSAIDA IS NOT NULL,
                            PEDID.PEDDTSAIDA, CAST(:DATA_ATUAL AS TIMESTAMP)
                        ), 1, 0
                    ) 
                ) * 100 / COUNT(*)
            ) PORCENTAGEMDENTRO,

            SUM(
                IIF(
                    PEDID.PEDPZENTRE <
                    IIF(
                        PEDID.PEDDTSAIDA IS NOT NULL,
                        PEDID.PEDDTSAIDA, CAST(:DATA_ATUAL AS TIMESTAMP)
                    ), 1, 0
                ) 
            ) ENTREGAFORAPRAZO,
												
            (
                SUM(
                    IIF(
                        PEDID.PEDPZENTRE <
                        IIF(
                            PEDID.PEDDTSAIDA IS NOT NULL,
                            PEDID.PEDDTSAIDA, CAST(:DATA_ATUAL AS TIMESTAMP)
                        ), 1, 0
                    ) 
                ) * 100 / COUNT(*)
            ) PORCENTAGEMFORA

        FROM
            PEDID
        WHERE
            PEDID.PEDDTEMIS BETWEEN :DATA_EMISSAO_INICIAL AND :DATA_EMISSAO_FINAL
            AND PEDID.PEDSITPED != 'C'
            AND PEDID.PEDPZENTRE IS NOT NULL
            AND PEDID.PEDORIGEM IN (
                'A', 'D', 'E', 'L', 'M', 'P',
                'Q', 'R', 'T', 'W', 'X', 'Z'
            )

        INTO
            :TOTALENTREGAS,
            :QUANTIDADE_DENTRO_PRAZO,
            :PORCENTAGEM_DENTRO_PRAZO,
            :QUANTIDADE_FORA_PRAZO,
            :PORCENTAGEM_FORA_PRAZO

    DO BEGIN
        SUSPEND;
    END
END
;
