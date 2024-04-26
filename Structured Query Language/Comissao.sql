execute block
returns (
     id integer
    ,dataEmissao timestamp
    ,dataSaida timestamp
    ,clienteCodigo integer
    ,funcionarioCodigo integer
    ,funcionarioNome varchar (40)
    ,zonaCodigo integer
    ,zonaDescricao varchar (30)
    ,cidadeUf char(2)
    ,marcaCodigo integer
    ,produtoCodigo char(14)
    ,produtoDescricao varchar(255)
    ,produtoTipo char(1)
    ,quantidade integer
    ,valorUnitario double precision
    ,descontoItem numeric (15,2)
    ,descontoPedido numeric (15,2)
    ,descontoTotal numeric (15,2)
    ,valorUnitarioLiquido double precision
    ,comissaoPercentual numeric (15,2)
    ,comissaoValor double precision)

as
	declare variable i double precision;
	declare variable loop integer;
	declare variable empresa integer;
	declare variable tempSequencial integer;
	declare variable tempId integer;
	declare variable totalFinalidade double precision;
	declare variable totalPedido integer;
	declare variable idPedidoAuxiliar integer;                                                                                  

	declare variable dataSaidaInicial date = @#date#dataSaidaInicial@;
	declare variable dataSaidaFinal date = @#date#dataSaidaFinal@;
	declare variable vendedor integer = @#integer#vendedor@;

begin

    descontoTotal 			= 0;
    valorUnitarioLiquido 	= 0;
    i 						= 0;
    comissaoPercentual 		= 0;
    comissaoValor 			= 0;
    totalFinalidade 		= 0;
    totalPedido 			= 0;
    idPedidoAuxiliar 		= 0;

    for
        select
             pedid.id_pedido
            ,pedid.peddtemis
            ,pedid.peddtsaida
            ,pedid.clicodigo
			
            ,clien.funcodigo
            ,funcio.funnome
            ,endcli.zocodigo
            ,zona.zodescricao
            ,cidade.ciduf
			
            ,produ.marcodigo
            ,pdprd.procodigo
            ,produ.prodescricao
            ,produ.protipo
            ,pdprd.pdpqtdade
            ,pdprd.pdppcounit
            ,pdprd.pdppcdescto
            ,pedid.pedpcdescto
			
        from pedid
            left join  clien    on clien.clicodigo  = pedid.clicodigo
            left join  endcli   on endcli.clicodigo = clien.clicodigo
            left join  zona     on zona.zocodigo    = endcli.zocodigo
			
            inner join pdprd    on pdprd.id_pedido  = pedid.id_pedido
			
            left join  produ    on produ.procodigo  = pdprd.procodigo
            left join  funcio   on funcio.funcodigo = clien.funcodigo
            left join  cidade   on endcli.cidcodigo = cidade.cidcodigo
			
        where
            pedid.peddtsaida between :dataSaidaInicial and :dataSaidaFinal
            and clien.funcodigo = :vendedor
            and pdprd.pdplcfinan = 'S'
            and pedid.pedsitped != 'C'
            and pedid.peddtsaida is not null

        union all

        select
             pedid.id_pedido
            ,pedid.peddtemis
            ,pedid.peddtsaida
            ,pedid.clicodigo
			
            ,clien.funcodigo
            ,funcio.funnome
            ,endcli.zocodigo
            ,zona.zodescricao
            ,cidade.ciduf
            ,'00'
			
            ,pdser.sercodigo
            ,servi.serdescricao
            ,servi.sertipo
            ,pdser.pdsqtdade
            ,pdser.pdsvalor
            ,pdser.pdspcdescto
            ,pedid.pedpcdesctoser
			
        from pedid
            left join  clien    on clien.clicodigo  = pedid.clicodigo
            left join  endcli   on endcli.clicodigo = clien.clicodigo
            left join  zona     on zona.zocodigo    = endcli.zocodigo
            inner join pdser    on pdser.id_pedido  = pedid.id_pedido
            left join  servi    on servi.sercodigo  = pdser.sercodigo
            left join  funcio   on funcio.funcodigo = clien.funcodigo
            left join  cidade   on endcli.cidcodigo = cidade.cidcodigo
			
        where
            pedid.peddtsaida between :dataSaidaInicial and :dataSaidaFinal
            and clien.funcodigo = :vendedor
            and pdser.pdslcfinan = 'S'
            and pedid.pedsitped != 'C'
            and pedid.peddtsaida is not null
			
        order by
            1

    into
        :id,:dataEmissao,
        :dataSaida,
        :clienteCodigo,
        :funcionarioCodigo,
        :funcionarioNome,
        :zonaCodigo,
        :zonaDescricao,
        :cidadeUf,
        :marcaCodigo,
        :produtoCodigo,
        :produtoDescricao,
        :produtoTipo,
        :quantidade,
        :valorUnitario,
        :descontoItem,
        :descontoPedido

    do begin

        --Calculo do total de cada item do pedido:
        descontoTotal = :descontoItem + :descontoPedido;
        i = (:quantidade * :valorUnitario) - ((:quantidade * :valorUnitario) * (:descontoItem / 100));
        valorUnitarioLiquido = i - (i * (:descontoPedido / 100));

        --Se a marca for 75, comissão = 50%, senão, comissão = 15%:
            if (:marcaCodigo = 75) then
            begin
                comissaoPercentual = 50 - :descontoTotal;
            end
            else
            begin
                comissaoPercentual = 15;
            end

        --Se o protipo = M e ciduf = MS, COMISSÃO = 100%:
            if (:produtoTipo = 'M' and :cidadeUf = 'MS') then
            begin
                comissaoPercentual = 100;
            end 

        --Se percentual de comissão for > 0, haverá comissão, senão, não haverá:
            if (:comissaoPercentual > 0) then
            begin
                comissaoValor = :valorUnitarioLiquido * (:comissaoPercentual / 100);
            end
            else
            begin
                comissaoValor = 0;
            end

            totalFinalidade = :totalFinalidade + :comissaoValor;

            if (:idPedidoAuxiliar <> :id  ) then
            begin
                totalPedido = :totalPedido + 1;
                idPedidoAuxiliar = :id;
            end                                                                                                                                

            suspend;

        --Zera variaveis para o loop:
            descontoTotal 		 	= 0;
            valorUnitarioLiquido 	= 0;
            i 						= 0;
            comissaoPercentual 		= 0;
            comissaoValor 			= 0;

            end

    id  				 = :totalPedido;
    dataEmissao 		 = null;
    dataSaida 			 = null;
    clienteCodigo 		 = null;
    funcionarioCodigo 	 = null;
    funcionarioNome 	 = null;
    zonaCodigo 			 = null;
    zonaDescricao 		 = null;
    cidadeUf 			 = null;
    marcaCodigo 		 = null;
    produtoCodigo 		 = null;
    produtoDescricao 	 = null;
    produtoTipo 		 = null;
    quantidade 		     = null;
    valorUnitario 		 = null;
    descontoItem 		 = null;
    descontoPedido 		 = null;
    descontoTotal 		 = null;
    valorUnitarioLiquido = null;
    comissaoPercentual 	 = null;
    comissaoValor 		 = :totalFinalidade;
	
    suspend;

end
