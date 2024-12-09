Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I click on the "Encode" option in the settings
    And I input the "message" into the text box labeled "Type message here"
    And I select the correct shift or key for the encoded message
    Then I click the "translate_message" button
    Then I should see the encoded message displayed on the screen



Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I click on the "Decode" option in the settings
    And I input the "encoded message" into the text box labeled "Type message here"
    And I select the correct shift or key for the encoded message
    Then I click the "translate_message" button
    Then I should see the decoded message displayed on the screen