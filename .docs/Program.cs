using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        decimal[] valores = new decimal[] { 180m, 1200m, 0m, 4900m, 478m, 787m, 10m, 400m, 1200m };
        long[] numerosDeConta = new long[] { 938485762, 347586970, 2147483649, 675869708, 238596054, 573659065, 210385733, 674038564, 563856300 };

        AcessoDados acessoDados = new AcessoDados(numerosDeConta, valores);
        var TRANSACOES = new Transacao[] {
            new Transacao { CorrelationId = 1, DateTime = "09/09/2023 14:15:00", ContaOrigem = numerosDeConta[0], ContaDestino = numerosDeConta[2], Valor = 150 },
            new Transacao { CorrelationId = 2, DateTime = "09/09/2023 14:15:05", ContaOrigem = numerosDeConta[2], ContaDestino = numerosDeConta[2], Valor = 149 },
            new Transacao { CorrelationId = 3, DateTime = "09/09/2023 14:15:29", ContaOrigem = numerosDeConta[2], ContaDestino = numerosDeConta[3], Valor = 1100 },
            new Transacao { CorrelationId = 4, DateTime = "09/09/2023 14:17:00", ContaOrigem = numerosDeConta[3], ContaDestino = numerosDeConta[6], Valor = 5300 },
            new Transacao { CorrelationId = 5, DateTime = "09/09/2023 14:18:00", ContaOrigem = numerosDeConta[4], ContaDestino = numerosDeConta[7], Valor = 1489 },
            new Transacao { CorrelationId = 6, DateTime = "09/09/2023 14:18:20", ContaOrigem = numerosDeConta[5], ContaDestino = numerosDeConta[8], Valor = 49 },
            new Transacao { CorrelationId = 7, DateTime = "09/09/2023 14:19:00", ContaOrigem = numerosDeConta[0], ContaDestino = numerosDeConta[2], Valor = 44 },
            new Transacao { CorrelationId = 8, DateTime = "09/09/2023 14:19:01", ContaOrigem = numerosDeConta[5], ContaDestino = numerosDeConta[3], Valor = 150 },
        };

        var executor = new ExecutarTransacaoFinanceira(acessoDados);
        foreach (var transacao in TRANSACOES)
        {
            executor.Transferir(transacao);
        }
    }
}

class Transacao
{
    public int CorrelationId { get; set; }
    public string DateTime { get; set; }
    public long ContaOrigem { get; set; }
    public long ContaDestino { get; set; }
    public decimal Valor { get; set; }
}

class ExecutarTransacaoFinanceira
{
    private readonly AcessoDados _acessoDados;

    public ExecutarTransacaoFinanceira(AcessoDados acessoDados)
    {
        _acessoDados = acessoDados;
    }

    public void Transferir(Transacao transacao)
    {
        var contaOrigem = _acessoDados.GetSaldo<ContaSaldo>(transacao.ContaOrigem);
        var contaDestino = _acessoDados.GetSaldo<ContaSaldo>(transacao.ContaDestino);

        if (contaOrigem.Saldo >= transacao.Valor)
        {
            if (contaDestino == null) throw new Exception("Conta de destino não encontrada");
            contaOrigem.Saldo -= transacao.Valor;
            contaDestino.Saldo += transacao.Valor;
            Console.WriteLine($"Transação número {transacao.CorrelationId} foi efetivada com sucesso! Novos saldos: Conta Origem: {contaOrigem.Saldo} | Conta Destino: {contaDestino.Saldo}");
        }
        else
        {
            Console.WriteLine($"Transação número {transacao.CorrelationId} foi cancelada por falta de saldo");
        }
    }
}

class ContaSaldo
{
    public ContaSaldo(long conta, decimal saldo)
    {
        Conta = conta;
        Saldo = saldo;
    }

    public long Conta { get; set; }
    public decimal Saldo { get; set; }
}

class AcessoDados
{
    private readonly long[] _numerosDeConta;
    private List<ContaSaldo> _tabelaSaldos;

    public AcessoDados(long[] numerosDeConta, decimal[] saldosIniciais)
    {
        _numerosDeConta = numerosDeConta;
        _tabelaSaldos = new List<ContaSaldo>();
        for (int i = 0; i < numerosDeConta.Length; i++)
        {
            _tabelaSaldos.Add(new ContaSaldo(numerosDeConta[i], saldosIniciais[i]));
        }
    }

    public ContaSaldo GetSaldo<T>(long id)
    {
        return _tabelaSaldos.Find(x => x.Conta == id);
    }

    public bool Atualizar<T>(T dado)
    {
        try
        {
            var item = (dado as ContaSaldo);
            var index = _tabelaSaldos.FindIndex(x => x.Conta == item.Conta);
            if (index != -1)
            {
                _tabelaSaldos[index] = dado as ContaSaldo;
                return true;
            }
            else
            {
                Console.WriteLine("Conta não encontrada para atualização.");
                return false;
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
            return false;
        }
    }
}
