Feature: Verify WishList and My-cart Functionality of a shopping portal
"""
In order to verify WishList and My-cart Functionality of a shopping website works
As an user
When I add 4 items from the wishlist,
I should be able to view on my wishlist

When i want to add the lowest price item ,
I should be able to add to my cart
"""
  @smoke @Wishlist @regression
  Scenario: Add four items in the wishlist
    """
      STEPS:

      1. Add four different products to my wishlist
      2. Click on Wishlist


      VERIFICATION: User should be presented  four selected items in the wishlist
    """
    Given I add four different products to my wishlist
    When I view my wishlist table
    Then I find total four selected items in my wishlist

  @smoke @Mycart @regression
  Scenario: Ablility to add the lowest priced item in mycart
    """
      STEPS:

      1. Search of any items
      2. Select the lowest to highest sort dropdown list
      4. select the first item which is lowest and add to my cart
      5. Click on my cart

      VERIFICATION: User should be presented with the selected item when click on My cart
    """


    When I search for the lowest price product
    And I am able to add lowest price items to my card
    Then I am able to verify the item in my cart