from behave import *
from pages.firjan_principal import *
from nose.tools import assert_equal

firjan_principal = Firjan_principal()


@given(u'que acesso o site da firjan')
def step_impl(context):
    firjan_principal.access_page("https://www.firjan.com.br/pagina-inicial.htm")


@given(u'que pesquiso pela palavra Firjan')
def step_impl(context):
    firjan_principal.get_input()


@when(u'clico no botão pesquisar')
def step_impl(context):
    firjan_principal.get_button()


@then(u'devo visualizar os resultados')
def step_impl(context):
    assert_equal(firjan_principal.get_el_result(), "firjan")
