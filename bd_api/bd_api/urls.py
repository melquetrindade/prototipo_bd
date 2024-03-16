from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from bd_api_app.views import ClienteViewSet, FornecedorViewSet, FuncionarioViewSet, EstadoViewSet, CidadeViewSet, BairroViewSet, EnderecoViewSet, ProdutoViewSet, EntradaMercadoriaViewSet, EntradaMercadoriaProdutoViewSet, VendaViewSet, VendaProdutoViewSet, MetodoPagamentoViewSet, VendaMetodoPagamentoViewSet, NotaFiscalViewSet, CaixaViewSet, Caixa_DiaCaixaViewSet, DiaCaixaViewSet, ContaViewSet, PagamentoViewSet, EntradaMercadoriaMetodoPagamentoViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'bairros', BairroViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'entradasMercadorias', EntradaMercadoriaViewSet)
router.register(r'entradasMercadoriasProdutos', EntradaMercadoriaProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'vendasProdutos', VendaProdutoViewSet)
router.register(r'metodosPagamentos', MetodoPagamentoViewSet)
router.register(r'vendasMetodosPagamentos', VendaMetodoPagamentoViewSet)
router.register(r'notasFiscais', NotaFiscalViewSet)
router.register(r'contas', ContaViewSet)
router.register(r'caixas', CaixaViewSet)
router.register(r'diasCaixas', DiaCaixaViewSet)
router.register(r'caixasDiasCaixas', Caixa_DiaCaixaViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'entradasMercadoriasMetodosPagamentos', EntradaMercadoriaMetodoPagamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
