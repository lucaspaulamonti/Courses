select
    distinct
        pedid.empcodigo,
        pedid.peddtemis,
        pedid.id_pedido,
        pedid.pedcodigo,
        pedid.clicodigo,

        clien.clirazsocial,
		
        pedid.pedsitped,
        pedid.tpcodigo,
        pedid.fiscodigo1,
        pedid.pdfcodigo,
        pedid.pedvrtotal
		
from pedid
    left join pdprd on pedid.id_pedido = pdprd.id_pedido
    left join produ on pdprd.procodigo = produ.procodigo
    left join pedidpromo on pedid.id_pedido  = pedidpromo.id_pedidoriginal
                         or  pedid.id_pedido = pedidpromo.id_pedidpromocao
    left join clien on pedid.clicodigo = clien.clicodigo
	
where
    pedid.peddtemis between *@#DATE#dataInicial@ and @#DATE#dataFinal@
    and pedid.pedsitped != 'C'
    and produ.glcodigo = 'T'
    and (
            (
                pedid.id_pedido = pedidpromo.id_pedidoriginal
             )

            or

            (
                pedid.id_pedido = pedidpromo.id_pedidpromocao
                and pedidpromo.id_promo not in (
                    select promo.id_promo from promo
                    where promo.descricao like '%EM DROBO%'
                    )
             )

            or

            (
                pedidpromo.id_pedidpromo is null
             )
        )
		
order by
    pedid.empcodigo,
    pedid.id_pedido
;
