select
    pedid.empcodigo,
    pedid.peddtemis,
    pedid.id_pedido,
    pedid.pedsitped,
    tbfis.fiscfop,
    pedid.peddtroman,
    pdprd.procodigo,
    produ.prodescricao,

    coalesce(
        (
            select first 1 pdprd2.procodigo from pdprd pdprd2
            where pedid.id_pedido = pdprd2.id_pedido
            and pdprd2.procodigo in ('8530','8531','8532')
        ), ''
    ) as tratamentoCodigo,

    coalesce(
        (
            select first 1 pdprd2.pdpdescricao from pdprd pdprd2
            where pedid.id_pedido = pdprd2.id_pedido
            and pdprd2.procodigo in ('8530','8531','8532')
        ), ''
    ) as tratamentoDescricao,

    clien.clicnpjcpf,
    clien.clirazsocial
    
from pedid
    left join pdprd     on pedid.id_pedido  = pdprd.id_pedido
    left join produ     on pdprd.procodigo  = produ.procodigo
    left join clien     on pedid.clicodigo  = clien.clicodigo
    left join nvalores  on pdprd.procodigo  = nvalores.procodigo
    left join tbfis     on pedid.fiscodigo1 = tbfis.fiscodigo
    
where
    pedid.peddtemis between @#DATE#dataInicial@ and @#DATE#dataFinal@
    and(
        pedid.pedsitped = 'F'
        or (
            pedid.pedsitped = 'A'
            and pedid.peddtsaida is not null
        )
    )
    and tbfis.fiscfop in ('5.101', '5.102', '6.101', '6.102')
    and nvalores.grcodigo = 6
    
order by
    pedid.id_pedido
;
