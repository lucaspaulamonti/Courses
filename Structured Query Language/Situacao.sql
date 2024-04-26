select
     clien.clicodigo
    ,clien.clicnpjcpf
    ,clien.clirazsocial
    ,clinet.netendereco
    ,endcli.endendereco
    ,endcli.endnr
    ,endcli.endcomple
    ,cidade.cidnome
    ,cidade.ciduf

    ,case situacao.sittipo
        when 'I' then 'INATIVO'
        when 'A' then 'ATIVO'
        when 'R' then 'RESTRITO'
        when 'B' then 'BLOQUEADO'
        else 'ATIVO'
    end as situacao

from
    clien
    left join clinet    on clien.clicodigo  = clinet.clicodigo
    left join endcli    on clien.clicodigo  = endcli.clicodigo
    left join cidade    on endcli.clicodigo = cidade.cidcodigo
    left join sitcli    on clien.clicodigo  = sitcli.clicodigo
    left join situacao  on sitcli.sitcodigo = situacao.sitcodigo

where
    (
        (
            (
                sitcli.sitdata = (
                                    select max(sitcli2.sitdata)
                                    from sitcli sitcli2
                                    where sitcli2.clicodigo = clien.clicodigo
                                    )
            )
        and
            (
                sitcli.sitseq  = (
                                    select max(sitcli3.sitseq)
                                    from sitcli sitcli3
                                    where sitcli3.clicodigo = clien.clicodigo
                                    and sitcli3.sitdata = sitcli.sitdata
                                    )
            )
        )
    or (sitcli.sitcodigo is null)
    )

order by
     situacao.sittipo
    ,clien.clicodigo
;
