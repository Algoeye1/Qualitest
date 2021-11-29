# -*- coding: UTF-8 -*-

from behave import step, given, then

from features.support.actions.pageaction import PageAction


from utils.assertutils import Assert

# ===============================================================================================
# STEP DEFINITIONS:
# ===============================================================================================


@given(u'I add four different products to my wishlist')
def step_impl(context):
    # Save the references of actions and page actions object in context.scenario
    # So that We can use the same object references in other steps
    context.scenario.page_action = PageAction(context)
    context.scenario.page_action.add_wishlist()




@step(u'I view my wishlist table')
def step_impl(context):
    context.scenario.wishlist_action = PageAction(context)

    context.scenario.wishlist_action.view_wish_list()





@then(u'I find total four selected items in my wishlist')
def step_impl(context):
    Assert.assert_true(context.scenario.Page.is_Bikini_wishlist_displayed(),
                       "Bikini  is not displayed in wishlist!")
    Assert.assert_true(context.scenario.Page.is_hardtop_displayed(),
                       "HardTop  is not displayed in wishlist!")
    Assert.assert_true(context.scenario.Page.is_poloshirt_displayed(),
                       "Polo Shirt  is not displayed in wishlist!")
    Assert.assert_true(context.scenario.Page.is_singleshirt_displayed(),
                       "Single Shirt  is not displayed in wishlist!")

@step(u'I search for the lowest price product')
def step_impl(context):
    context.scenario.mycart_action = PageAction(context)

    context.scenario.search_lowest_price_product()




@step(u'I am able to add lowest price items to my card')
def step_impl(context):
    context.scenario.mycart_action = PageAction(context)

    context.scenario.add_mycart()


@then(u'I am able to verify the item in my cart')
def step_impl(context):
    Assert.assert_true(context.scenario.Page.is_singleshirt_displayed(),
                       "Single Shirt  is not displayed in wishlist!")