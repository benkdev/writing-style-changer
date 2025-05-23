import unittest
from unittest.mock import patch, MagicMock
from style_changer import change_style

class TestStyleChanger(unittest.TestCase):

    @patch('style_changer.client.chat.completions.create')
    def test_change_style(self, mock_create):
        # Configure the mock response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = MagicMock()
        mock_response.choices[0].message.content = "Mocked styled text."
        mock_create.return_value = mock_response

        # Call the function
        text_to_change = "This is a test text."
        style_to_apply = "Test Style"
        result = change_style(text_to_change, style_to_apply)

        # Assert the return value
        self.assertEqual(result, "Mocked styled text.")

        # Assert that the create method was called with the correct model
        mock_create.assert_called_once_with(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Pretend you are an expert author."},
                {"role": "user", "content": f"Change the style of this document to {style_to_apply}: {text_to_change}"}
            ]
        )

if __name__ == '__main__':
    unittest.main()
