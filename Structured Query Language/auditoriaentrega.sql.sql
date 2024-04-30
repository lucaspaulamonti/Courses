execute block
returns (
    codigoEmpresa int,
    dataEmissao date,
    idPedido int,
    codigoCliente int,

    razaoCliente varchar(50),
    diaEntrega date,
    horaEntrega time,
    cidadeNome varchar(25),
    cidadeUf char(2),

    codigoProduto char(14),
    descricaoProduto varchar(50),
    quantidadeProduto integer,
    valorUnitario double precision,
    valorTotalProduto double precision,
    valorTotalPedido double precision,
    cfopProduto char(7),

    descicaoAcompanhamento varchar(50)
)
as

    declare variable dataEmissaoInicial date = @#date#dataEmissaoInicial@;
    declare variable dataEmissaoFinal date = @#date#dataEmissaoFinal@;

begin
    for
        select
            pedid.empcodigo,
            pedid.peddtemis,
            pedid.id_pedido,
            pedid.clicodigo,

            trim(upper(left(clien.clirazsocial, 50))),
            pedid.pedpzentre,
            pedid.pedhrentre,
            trim(upper(left(cidade.cidnome, 25))),
            cidade.ciduf,

            pdprd.procodigo,
            trim(upper(left(pdprd.pdpdescricao, 50))),
            cast(trunc(pdprd.pdpqtdade, 0) as integer),
            pdprd.pdpunitliquido,
            cast(pdprd.pdpunitliquido * pdprd.pdpqtdade as double precision),
            cast(pedid.pedvrtotal as double precision),
            tbfis.fiscfop,

            localped.lpdescricao

        from pedid
            left join clien     on pedid.clicodigo  = clien.clicodigo
            left join endcli    on pedid.clicodigo  = endcli.clicodigo
                                and pedid.endent    = endcli.endcodigo
            left join cidade    on endcli.cidcodigo = cidade.cidcodigo
            left join pdprd     on pedid.id_pedido  = pdprd.id_pedido
            left join acoped    on pedid.id_pedido  = acoped.id_pedido
                                and acoped.apcodigo = (
                                    select max(acoped2.apcodigo) from acoped acoped2
                                    where pedid.id_pedido = acoped2.id_pedido
                                )
            left join localped  on acoped.lpcodigo = localped.lpcodigo
            left join tbfis on pdprd.fiscodigo = tbfis.fiscodigo

        where
            pedid.peddtemis >= :dataEmissaoInicial
            and pedid.peddtemis <= :dataEmissaoInicial
            and pedid.pedsitped != 'C'
            and exists (
                select 1 from acoped acoped3
                where acoped3.apdata >= :dataEmissaoInicial
                and acoped3.lpcodigo in (3, 5, 177, 14, 65)
                and pedid.id_pedido = acoped3.id_pedido
            )
            order by
                pedid.id_pedido

        into
            :codigoEmpresa,
            :dataEmissao,
            :idPedido,
            :codigoCliente,
            :razaoCliente,
            :diaEntrega,
            :horaEntrega,
            :cidadeNome,
            :cidadeUf,
            :codigoProduto,
            :descricaoProduto,
            :quantidadeProduto,
            :valorUnitario,
            :valorTotalProduto,
            :valorTotalPedido,
            :cfopProduto,
            :descicaoAcompanhamento

       do begin
        suspend;
       end
end 

