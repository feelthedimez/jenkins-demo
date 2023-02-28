from behave import *

@given(u'that I want to test two number')
def step_impl(context):
    print("Adding 2 numbers")


@when(u'I add 2 and 5')
def step_impl(context):
    context.result = 2 + 5


@then(u'I should get 7')
def step_impl(context):
    
    assert context.result == 7, "Result validation"