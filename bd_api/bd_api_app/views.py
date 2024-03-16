from rest_framework import viewsets
from .models import Cidade, Bairro, Cliente, Fornecedor, Funcionario, Endereco, Estado, Produto, EntradaMercadoria, EntradaMercadoria_Produto, Venda, VendaProduto, MetodoPagamento, Venda_MetodoPagamento, NotaFiscal, Caixa, Conta, Caixa_DiaCaixa, DiaCaixa, Pagamento, EntradaMercadoria_MetodoPagamento
from .serializers import ClienteSerializer, FornecedorSerializer, FuncionarioSerializer, EstadoSerializer, CidadeSerializer, BairroSerializer, EnderecoSerializer, ProdutoSerializer, EntradataMercadoriaSerializer, EntradataMercadoriaProdutoSerializer, VendaSerializer, VendaProdutoSerializer, MetodoPagamentoSerializer, VendaMetodoPagamentoSerializer, NotaFiscalSerializer, CaixaSerializer, ContaSerializer, CaixaDiaCaixaSerializer, DiaCaixaSerializer, PagamentoSerializer, EntradaMercadoriaMetodoPagamentoSerializer

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class BairroViewSet(viewsets.ModelViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class EntradaMercadoriaViewSet(viewsets.ModelViewSet):
    queryset = EntradaMercadoria.objects.all()
    serializer_class = EntradataMercadoriaSerializer

class EntradaMercadoriaProdutoViewSet(viewsets.ModelViewSet):
    queryset = EntradaMercadoria_Produto.objects.all()
    serializer_class = EntradataMercadoriaProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaProdutoViewSet(viewsets.ModelViewSet):
    queryset = VendaProduto.objects.all()
    serializer_class = VendaProdutoSerializer

class MetodoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPagamento.objects.all()
    serializer_class = MetodoPagamentoSerializer

class VendaMetodoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = Venda_MetodoPagamento.objects.all()
    serializer_class = VendaMetodoPagamentoSerializer

class NotaFiscalViewSet(viewsets.ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer

class DiaCaixaViewSet(viewsets.ModelViewSet):
    queryset = DiaCaixa.objects.all()
    serializer_class = DiaCaixaSerializer

class Caixa_DiaCaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa_DiaCaixa.objects.all()
    serializer_class = CaixaDiaCaixaSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class EntradaMercadoriaMetodoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = EntradaMercadoria_MetodoPagamento.objects.all()
    serializer_class = EntradaMercadoriaMetodoPagamentoSerializer