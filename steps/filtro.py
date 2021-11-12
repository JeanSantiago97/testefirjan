from behave import *
from pages.firjan_ordenacao import *

firjan_ordenacao = Firjan_ordenacao()


# Ordem A-Z
@given('Que abro o menu de ordenação A-Z')
def step_impl(context):
    firjan_ordenacao.menu()


@when('Seleciono a opção A-Z')
def step_impl(context):
    firjan_ordenacao.order_alphabetic_az()


@then('Devo visualizar os resultados de A-Z')
def step_impl(context):
    # firjan_principal.get_btn_mostrarmais()
    firjan_ordenacao.test_order_az()


# Ordem Z-A
@given(u'que abro o menu de ordenação Z-A')
def step_impl(context):
    firjan_ordenacao.menu()


@when(u'seleciono a opção Z-A')
def step_impl(context):
    firjan_ordenacao.order_alphabetic_za()


@then('Devo visualizar os resultados de Z-A')
def step_impl(context):
    firjan_ordenacao.test_order_za()


# Mais Recente
@given(u'que abro o menu de ordenação Mais recentes')
def step_impl(context):
    firjan_ordenacao.menu()


@when(u'seleciono a opção Mais recentes')
def step_impl(context):
    firjan_ordenacao.order_recent()


@then('Devo visualizar os resultados por Mais recentes')
def step_impl(context):
    firjan_ordenacao.test_order_recent()


# Mais Antigo
@given(u'que abro o menu de ordenação Mais antigos')
def step_impl(context):
    firjan_ordenacao.menu()


@when(u'seleciono a opção Mais antigos')
def step_impl(context):
    firjan_ordenacao.order_old()


@then('Devo visualizar os resultados por Mais antigos')
def step_impl(context):
    firjan_ordenacao.get_dates()
