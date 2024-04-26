execute block
returns (
    /*
        Retornos do Pedido de Cliente Control.
    */
    codigoEmpresaControl integer,
    dataEmissaoControl date,
    idPedidoControl integer,
    codigoClienteControl integer,
    nomeClienteControl varchar(255),

    /*
        Retornos do Pedido de Cliente Original.
    */
    codigoEmpresaOriginal integer,
    dataEmissaoOriginal date,
    idPedidoOriginal integer,
    codigoClienteOriginal integer,
    nomeClienteOriginal varchar(255),

    /*
        Retornos do Histórico do Pedido de Cliente Control.
    */
    codigoLocalizacaoControl integer,
    nomeLocalizacaoControl varchar(30),
    dataLocalizacaoControl date,
    horaLocalizacaoControl time
    )
as
    /*
        Inicialização de variáveis: Origem de Pedido: Control; Código da Empresa: Matriz; e Situação do Pedido: Aberto.
    */
    declare variable dataEmissaoInicial date = @#date#dataEmissao@;
    declare variable constOrigemPedido char(1) = 'L';
    declare variable constCodigoEmpresa integer = 1;
    declare variable constSituacaoPedido char(1) = 'A';
begin
    for
        select
            /*
                Consultas do Pedido de Cliente Control.
            */
            pedcontrol.empcodigo,
            pedcontrol.peddtemis,
            pedcontrol.id_pedido,
            pedcontrol.clicodigo,
            upper(clicontrol.clirazsocial),

            /*
                Consultas do Pedido de Cliente Original.
            */
            pedoriginal.empcodigo,
            pedoriginal.peddtemis,
            pedoriginal.id_pedido,
            pedoriginal.clicodigo,
            upper(clioriginal.clirazsocial),

            /*
                Consultas do Histórico do Pedido de Cliente Control.
            */
            acocontrol.lpcodigo,
            upper(localped.lpdescricao),
            cast(acocontrol.apdata as date),
            cast(acocontrol.aphora as time)
        from pedid pedcontrol
            left join pedxped           on pedcontrol.id_pedido  = pedxped.id_peddes
            left join clien clicontrol  on pedcontrol.clicodigo  = clicontrol.clicodigo
            left join pedid pedoriginal on pedxped.id_pedori     = pedoriginal.id_pedido
            left join clien clioriginal on pedoriginal.clicodigo = clioriginal.clicodigo
            left join acoped acocontrol on pedcontrol.id_pedido  = acocontrol.id_pedido
            and acocontrol.apcodigo = (
                /*
                    Seleção da última localização do pedido.
                */
                select max(acoped.apcodigo) from acoped
                where acoped.apdata >= :dataEmissaoInicial
                and acoped.id_pedido = pedcontrol.id_pedido
            )
            left join localped          on acocontrol.lpcodigo   = localped.lpcodigo
        where
            /*
                Condições de filtro para selecionar os pedidos desejados.
            */
            pedcontrol.peddtemis >= :dataEmissaoInicial
            and pedcontrol.pedorigem = :constOrigemPedido
            and pedcontrol.empcodigo = :constCodigoEmpresa
            and pedcontrol.pedsitped = :constSituacaoPedido
        order by
            pedcontrol.id_pedido

        into
            /*
                Atribuição dos resultados da consulta do Control às variáveis de retorno.
            */
            :codigoEmpresaControl,
            :dataEmissaoControl,
            :idPedidoControl,
            :codigoClienteControl,
            :nomeClienteControl,
			
            /*
                Atribuição dos resultados da consulta do Original às variáveis de retorno.
            */
            :codigoEmpresaOriginal,
            :dataEmissaoOriginal,
            :idPedidoOriginal,
            :codigoClienteOriginal,
            :nomeClienteOriginal,

            /*
                Atribuição dos resultados da consulta do Histórico às variáveis de retorno.
            */
            :codigoLocalizacaoControl,
            :nomeLocalizacaoControl,
            :dataLocalizacaoControl,
            :horaLocalizacaoControl
        do begin
            suspend;
        end
end 
